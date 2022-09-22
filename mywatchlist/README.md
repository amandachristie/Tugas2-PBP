# Tugas 3: Pengimplementasian _Data Delivery_ Menggunakan Django
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

# **Link**

🔗[**HTML**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/html/)

🔗[**JSON**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/json/)

🔗[**XML**](https://tugas2-pbp-amandachristie.herokuapp.com/mywatchlist/xml/)

## Perbedaan antara JSON, XML, dan HTML
**1. JSON (_JavaScript Object Notation_)** adalah format data ringan yang digunakan untuk menyimpan dan mengirim data dari sebuah server hingga dapat ditampilkan pada _web page_. JSON bersifat _self-describing_ sehingga sangat mudah untuk dimengerti. Format JSON berbentuk _text_ sehingga kode untuk membaca dan membuat JSON banyak terdapat di banyak bahasa pemrograman. Data pada JSON disimpan dalam bentuk _key_ dan _value_.

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
Dalam mengembangkan suatu platform, ada kalanya kita perlu menyimpan dan mengirimkan data dari _stack_ yang satu ke _stack_ lainnya. Oleh karena itu, aplikasi membutuhkan cara untuk menyimpan data tersebut ke dalam database. Namun, bagian _back-end_ dan _front-end_ aplikasi tidak dapat berkomunikasi secara langsung sehingga dibutuhkan sebuah format yang dapat menjadi perantara pertukaran data, seperti yang umum digunakan antara lain HTML, XML, dan JSON. Dengan adanya _data delivery_, penyimpanan dan pengambilan data dari server dapat dilakukan dengan cepat.

## Pengimplementasian Checklist
 ✅ **Membuat suatu aplikasi baru bernama `mywatchlist` di proyek Django Tugas 2 pekan lalu.**
 
 Untuk membuat `django-app` bernama `mywatchlist`, kita harus masuk ke direktori Tugas 2 PBP di _command prompt_ dan memberikan perintah berikut ini. 
 ```
 python manage.py startapp mywatchlist
 ```
 
 ✅ **Menambahkan _path_ `mywatchlist` sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist.**
 
 Untuk menambahkan _path_ baru, kita dapat mengakses file `urls.py` yang berada pada folder `project-django` dan memasukkan _path_ `mywatchlist` ke `urlpattern`.
 ```
 urlpatterns = [
 ...
 path('mywatchlist/', include('mywatchlist.urls')),
]
 ```
 
 ✅ **Membuat sebuah model MyWatchList**

Untuk membuat sebuah model MyWatchList, kita perlu mengakses file `models.py` di dalam folder `mywatchlist`. Di dalam file tersebut, kita tambahkan kode untuk membuat class dan atribut yang dibutuhkan untuk setiap tipe data `watched`, `title`, `rating`, `release_date`, dan `review`.
 ```
 class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
 ```
Setelah itu, kita perlu menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
 
 ✅ **Menambahkan minimal 10 data untuk objek MyWatchList.**
Untuk menambahkan data untuk objek MyWatchList, kita harus membuat folder baru yang bernama `fixtures` di dalam folder `mywatchlist`. Kemudian, di dalam folder fixtures, kita membuat file JSON baru bernama `intial_mywatchlist_data.json` yang di dalamnya berisi daftar film. Data tersebut dituliskan dengan format berikut:
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
Kemudian, kita harus menjalankan perintah ```python manage.py loaddata initial_mywatchlist_data.json``` untuk memasukkan data tersebut ke dalam database Django lokal.
Di file `Procfile` yang sudah ada di direktori Tugas 2 PBP, kita harus menambahkan potongan kode `release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'`.

 ✅ **Menyajikan data yang telah dibuat sebelumnya dalam tiga format, yaitu HTML, JSON, dan XML.**
 
Untuk menyajikan data dalam ketiga format tersebut, kita harus membuat 3 fungsi di file `views.py` dalam folder `mywatchlist`, yaitu `show_mywatchlist`, `show_mywatchlist_json`, dan `show_mywatchlist_xml`.

`HTML`
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
 `JSON`
 ```
 def show_mywatchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
 ```
 `XML`
 ```
 def show_mywatchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")
 ```
 
 ✅ **Membuat routing sehingga data di atas dapat diakses melalui URL.**
 
Untuk melakukan routing terhadap fungsi di `views.py` yang telah kita buat sehingga nantinya halaman HTML, JSON, dan XML dapat ditampilkan melalui browser, kita harus menambahkan _path_ berikut ini ke `urlpatterns`.
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

## Pemeriksaan _Routes_ dengan Postman
1. `mywatchlist/html`

![Postman_HTML](https://user-images.githubusercontent.com/87993867/191651318-70398999-b97d-45d3-bc88-b107acfba80e.png)

2. `mywatchlist/json`

![Postman_JSON](https://user-images.githubusercontent.com/87993867/191651328-78a2243e-a3e1-4c9c-b191-7c5582253b43.png)

3. `mywatchlist/xml`

![Postman_XML](https://user-images.githubusercontent.com/87993867/191651333-82468fdd-ab0c-48e7-9f85-10e4e3452dd7.png)
