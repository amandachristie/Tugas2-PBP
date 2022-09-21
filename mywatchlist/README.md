# Tugas 3: Pengimplementasian _Data Delivery_ Menggunakan Django
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

# **Link**

🔗[**HTML**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/html/)

🔗[**JSON**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/json/)

🔗[**XML**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/xml/)

## Perbedaan antara JSON, XML, dan HTML
**1. JSON (_JavaScript Object Notation_)** adalah format data ringan yang digunakan untuk menyimpan dan mengirim data dari sebuah server hingga dapat ditampilkan pada web page. JSON bersifat _self-describing_ sehingga sangat mudah untuk dimengerti. Format JSON berbentuk _text_ sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman. Data pada JSON disimpan dalam bentuk _key_ dan _value_.

  Contoh:
  ```
  {
      "watched":true,
      "title":"Everything Everywhere All At Once",
      "rating": 5,
      "release_date" : "2022-06-22",
      "review": "The best acid trip experience that can be felt once in a lifetime!"
  }
  ```

**2. XML (_Extensible Markup Language_)** adalah bahasa markup yang juga digunakan untuk menyimpan dan mengirim data. XML bersifat _self-descriptive_. Hal yang membedakan XML dengan JSON adalah formatnya. XML memiliki format yang mirip dengan HTML, yaitu informasi yang dibungkus di dalam _tag_. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. Perbedaan XML dan HTML adalah XML dirancang untuk fokus pada mengirim dan menyimpan data, sedangkan HTML dirancang untuk fokus menampilkan data.

  Contoh:
  ```
  <django-objects version="1.0">
    <object model="mywatchlist.mywatchlist" pk="1">
      <field name="watched" type="BooleanField">True</field>
      <field name="title" type="TextField">Mencuri Raden Saleh</field>
      <field name="rating" type="IntegerField">5</field>
      <field name="release_date" type="DateField">2022-08-25</field>
      <field name="review" type="TextField">A pretty well executed Indonesian Heist movie!</field>
    </object>
  ```

**3. HTML (_Hypertext Markup Language_)** adalah bahasa markup standar yang digunakan untuk membuat halaman web. Elemen-elemen pada HTML memberi tahu browser untuk menampilkan konten. HTML tidak memiliki sintaks penyimpanan dan pengiriman data, seperti JSON dan XML.

  Contoh:
  ```
  <h1>My Watchlist</h1>
  <p>The first movie I watched.</p>
  ```

## Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Perubahan data yang dinamis membuat aplikasi membutuhkan cara bagaimana agar dapat menyimpan data dari user ke dalam database dengan cepat. Hal ini dapat dilakukan dengan pemrosesan data secara masif sehingga diperlukan HTTP Protocols yang akan membantu developer melakukan pengiriman data dengan menggunakan method, seperti get, post, patch, dan delete. Dengan begitu, pentingnya data perantara untuk pertukaran data, seperti JSON dan XML. Melalui perantara ini, akan memudahkan user dan server dalam pengambilan data ke bagian backend dengan cepat. Dengan HTTP Protocols akan membantu developer untuk melakukan pengiriman data untuk menerima perintah dari suatu frontend tentang pemrosesan suatu data.

## Pengimplementasian Checklist
 ✅ Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu.
 ```
 python manage.py startapp mywatchlist
 ```
 
 ✅ Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist.
 ```
 urlpatterns = [
 ...
 path('mywatchlist/', include('mywatchlist.urls')),
]
 ```
 
 ✅ Membuat sebuah model MyWatchList
 ```
 class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
 ```
 
 ✅ Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas.
 ```
 [
  ...
 {
        "model":"mywatchlist.mywatchlist",
        "pk":2,
        "fields":{
            "watched": true,
            "title":"Avengers: Endgame",
            "rating": 4,
            "release_date" : "2019-04-24",
            "review": "Amazing finale, but a mess in some parts."
        }
    },
    {
        "model":"mywatchlist.mywatchlist",
        "pk":3,
        "fields":{
            "watched": true,
            "title":"Harry Potter and the Sorcerer's Stone",
            "rating": 4,
            "release_date" : "2001-12-19",
            "review": "Epic adaptation, there's nothing like the first in a series."
        }
    },
    {
    ...
 ]
 ```
 
 ✅ Menyajikan data yang telah dibuat sebelumnya dalam tiga format, yaitu HTML, JSON, dan XML.
 ```
 def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()

    watched = MyWatchList.objects.filter(watched=True).count()
    not_watched = MyWatchList.objects.filter(watched=False).count()
    
    message = ""

    # Showing message.
    if watched >= not_watched:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
    
    context = {
    'mywatchlist': data_mywatchlist,
    'message': message,
    'name': 'Amanda Christie Tarigan',
    'student_id': '2106751322'
    }
    return render(request, "mywatchlist.html", context)
 ```
 ```
 def show_mywatchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
 ```
 ```
 def show_mywatchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")
 ```
 
 ✅ Membuat routing sehingga data di atas dapat diakses melalui URL.
 ```
 from django.urls import path
from mywatchlist.views import show_mywatchlist, show_mywatchlist_json, show_mywatchlist_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
]
 ```
