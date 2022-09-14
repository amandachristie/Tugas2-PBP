# Tugas 2 Pemrograman Berbasis Platform
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

*🔗Link Aplikasi: https://tugas2-pbp-amandachristie.herokuapp.com/katalog/*

## *Request Client and Response* Berbasis Django

**Bagan**

**Penjelesan Proses**
1. Pada saat *client* membuka Django, maka proses ***request*** atau permintaan oleh *client* akan masuk ke dalam *web server* Django.
2. *Request* tersebut akan diproses melalui **urls.py**. Pada urls.py, terdapat definisi alamat url dan fungsi yang akan meng-*handle* setiap *route.*
3. Dari urls, *request* diteruskan ke **views.py** untuk melakukan pemrosesan permintaan, seperti mengambil data dan menyusun tampilan data pada template. Apabila terdapat proses yang membutuhkan database, views akan memanggil *query* ke **models**. *Query* adalah perintah yang digunakan untuk meminta akses data dari database. Pada direktori Tugas2-PBP, terdapat file db.sqlite. File tersebut adalah database yang terbentuk saat *migration.*
4. Kemudian, database akan mengembalikan hasil dari *query* tersebut ke models dan data di models akan diimport oleh views. 
5. Setelah pemintaan selesai diproses, hasil proses tersebut akan ditampilkan dalam HTML, yaitu di **template.**  
6. Terakhir, tampilan HTML akan dikembalikan ke django untuk ditampilkan ke user sebagai ***respons.***

## Mengapa Kita Menggunakan *Virtual Environment*?
*Virtual environment* digunakan untuk menjaga atau mengisolasi *dependencies* yang dibutuhkan oleh satu proyek terpisah dari proyek yang lain. Dengan menggunakan *virtual environment*, perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Misalnya, kita sedang mengerjakan dua proyek Python berbasis web yang berbeda. Proyek yang satu menggunakan Django versi 3.8, sedangkan proyek yang lain menggunakan Django versi 3.9. Pada kondisi tersebut, *virtual environment* akan sangat berguna untuk menjaga *dependencies* kedua proyek terpisah dan tidak terjadi konflik. Oleh karena itu, sebaiknya setiap proyek Django menggunakan virtual environment sendiri. 

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Tentu, kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Akan tetapi, ketika kita tidak menggunakan virtual environment, proyek yang kita kerjakan hanya dapat mengakses modul-modul dan library global suatu perangkat. Perlu diingat juga bahwa saat kita meng-*install dependencies* yang dibutuhkan dengan perintah pip install tanpa berada di virtual environment, proyek aplikasi lain juga dapat mengaksesnya karena sifatnya global. Selama kita sudah memastikan apakah versi modul global pada perangkat yang akan kita gunakan untuk menjalankan aplikasi dapat mendukung *dependencies* yang diperlukan oleh proyek, maka kita tetap dapat membuat aplikasi tersebut tanpa virtual environment.

## Proses Implementasi Konsep Model-View-Template
