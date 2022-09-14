# Tugas 2 Pemrograman Berbasis Platform
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

*🔗Link Aplikasi: https://tugas2-pbp-amandachristie.herokuapp.com/katalog/*

## *Request and Response Client* Berbasis Django

**Bagan**

**Penjelasan Proses**
1. Pada saat *client* membuka Django, maka proses ***request*** atau permintaan oleh *client* akan masuk ke dalam *web server* Django.
2. *Request* tersebut akan diproses melalui **urls.py**. Pada urls.py, terdapat definisi alamat url dan fungsi yang akan meng-*handle* setiap *route.*
3. Dari urls, *request* diteruskan ke **views.py** untuk melakukan pemrosesan permintaan, seperti mengambil data dan menyusun tampilan data pada template. Apabila terdapat proses yang membutuhkan database, views akan memanggil *query* ke **models**. *Query* adalah perintah yang digunakan untuk meminta akses data dari database. Pada direktori Tugas2-PBP, terdapat file db.sqlite. File tersebut adalah database yang terbentuk saat *migration.*
4. Kemudian, database akan mengembalikan hasil dari *query* tersebut ke models dan data di models akan diimport oleh views. 
5. Setelah pemintaan selesai diproses, hasil proses tersebut akan ditampilkan dalam HTML, yaitu di **template.**  
6. Terakhir, tampilan HTML akan dikembalikan ke django untuk ditampilkan ke user sebagai ***respons.***

## Mengapa Kita Menggunakan *Virtual Environment*?
*Virtual environment* digunakan untuk menjaga atau mengisolasi *dependencies* yang dibutuhkan oleh satu proyek terpisah dari proyek yang lain. Dengan menggunakan *virtual environment*, perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Misalnya, kita sedang mengerjakan dua proyek Python berbasis web yang berbeda. Proyek yang satu menggunakan Django versi 3.8, sedangkan proyek yang lain menggunakan Django versi 3.9. Pada kondisi tersebut, *virtual environment* akan sangat berguna untuk menjaga *dependencies* kedua proyek terpisah dan tidak terjadi konflik. Oleh karena itu, sebaiknya setiap proyek Django menggunakan virtual environment sendiri. 

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?
Tentu, kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Akan tetapi, ketika kita tidak menggunakan *virtual environment*, proyek yang kita kerjakan hanya dapat mengakses modul-modul dan library global suatu perangkat. Perlu diingat juga bahwa saat kita meng-*install dependencies* yang dibutuhkan dengan perintah pip install tanpa berada di *virtual environment*, proyek aplikasi lain juga dapat mengaksesnya karena sifatnya global. Selama kita sudah memastikan apakah versi modul global pada perangkat yang akan kita gunakan untuk menjalankan aplikasi dapat mendukung *dependencies* yang diperlukan oleh proyek, maka kita tetap dapat membuat aplikasi tersebut tanpa *virtual environment.*

## Proses Implementasi Konsep Model-View-Template
**1. Membuat fungsi di views.py**
Pada views.py, kita buat fungsi show_catalog yang menerima parameter request. Di dalam fungsi tersebut, setiap objek  dari CatalogItem disimpan dalam variabel data_katalog_item dengan memanggil CatalogItem.objects.all(). Data-data tersebut akan disimpan dalam sebuah dictionary bernama context yang memiliki 3 key, yaitu list_barang, nama, dan NPM. Fungsi ini akan mengembalikan fungsi render(request, "katalog.html", context) agar data-data katalog tersebut dirender. 
```
def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_item,
        'nama': 'Amanda Christie Tarigan',
        'NPM' : '2106751322'
    }
    return render(request, "katalog.html", context)
```

**2. Membuat sebuah routing untuk memetakan fungsi**
Untuk melakukan *routing* atau memetakan fungsi show_catalog yang telah dibuat pada views.py, kita perlu memodifikasi isi list urlpatterns, dengan menambahkan path baru. Sementara, pada urls.py di folder project_django, kita juga perlu menambahkan path dengan parameter "katalog/"  yang akan mengarahkan menuju alamat katalog.url.
```
urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]
```
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```

**3. Memetakan data yang didapatkan ke dalam HTML**
Pada bagian ini, kita ingin meload data-data dari database dan menampilkannya. Untuk memetakan data ke HTML, yang perlu kita modifikasi tentunya adalah file html, yaitu katalog.html. Untuk menampilkan name, student id, dan atribut-atribut item katalog, kita mengambil value dari key yang sebelumnya terdapat di dictionary context. 
```
<h5>Name: </h5>
<p>{{nama}}</p>

<h5>Student ID: </h5>
<p>{{NPM}}</p>
```
```
{% for barang in list_barang %}
<tr>
    <td>{{barang.item_name}}</td>
    <td>{{barang.item_price}}</td>
    <td>{{barang.item_stock}}</td>
    <td>{{barang.rating}}</td>
    <td>{{barang.description}}</td>
    <td>{{barang.item_url}}</td>
</tr>
{% endfor %}
```
**4. Melakukan deployment ke Heroku.** 
Langkah terakhir adalah melakukan *deployment* ke Heroku terhadap aplikasi katalog agar dapat diakses oleh publik melalui internet. Sebelum melakukan deployment, kita perlu membuat aplikasi di Heroku. Kemudian, informasi API key dan nama aplikasi yang telah dibuat, kita simpan dalam settrings-secret repository project kita sebagai data pribadi. Kemudian, pada ***actions repository***, kita lakukan *deploy* ke Heroku. Setelah berhasil, kita dapat mengakses *link* proyek aplikasi.
