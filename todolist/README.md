# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

## **Link**

🔗[**/todolist**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist)

## Apa kegunaan {% csrf_token %} pada elemen `<form> ? 
## Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
## Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

## Proses Implementasi Checklist

✅ **Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.**
 
 Untuk membuat `django-app` bernama `todolist`, kita harus masuk ke direktori Tugas 2 PBP di _command prompt_ dan memberikan perintah berikut ini. 
 ```
 python manage.py startapp todolist
 ```
**✅ Menambahkan _path_ `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist.**

 Untuk menambahkan _path_ baru, kita dapat mengakses file `urls.py` yang berada pada folder `project-django` dan memasukkan _path_ `todolist` ke `urlpattern`.
 ```
 urlpatterns = [
 ...
 path('todolist/', include('todolist.urls')),
]
 ```

**✅ Membuat sebuah model Task yang memiliki atribut user, date, title, description**

Untuk membuat sebuah model Task, kita perlu mengakses file `models.py` di dalam folder `todolist`. Di dalam file tersebut, kita tambahkan kode untuk membuat class dan atribut yang dibutuhkan untuk setiap tipe data `user`, `date`, `title`, dan `description`.
 ```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # menghubungkan task dengan pengguna yang membuat task tersebut
    date = models.DateTimeField(auto_now_add=True) # mendeskripsikan tanggal pembuatan task
    title = models.CharField(max_length=225) # mendeskripsikan judul task
    description = models.TextField() # mendeskripsikan deskripsi task
    is_finished = models.BooleanField(default=False) # [BONUS] mendeskripsikan status penyelesaian task dengan default False (Belum Selesai)
 ```
Setelah itu, kita perlu menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
 
**✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**

**✅ Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task. **\

**✅ Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**

**✅ Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:**

 Untuk melakukan routing terhadap fungsi di `views.py` yang telah kita buat, kita harus menambahkan _path_ berikut ini ke `urlpatterns`di file `urls.py` pada folder todolist.
 ```
from django.urls import path
from todolist.views import delete_task, register, login_user, logout_user, todolist, create_task, update_status

app_name = 'todolist'

urlpatterns=[
    path('', todolist, name='todolist'), # http://localhost:8000/todolist berisi halaman utama yang memuat tabel task
    path('login/', login_user, name='login'), # http://localhost:8000/todolist/login berisi form login
    path('register/', register, name='register'), #  http://localhost:8000/todolist/register berisi form registrasi akun
    path('create-task/', create_task, name='create_task'), #  http://localhost:8000/todolist/create-task berisi form pembuatan tas
    path('update-status/<int:id>', update_status, name='update_status'), # [BONUS] mekanisme pembaruan status task
    path('delete-task/<int:id>', delete_task, name='delete_task'), # [BONUS] mekanisme penghapusan task
    path('logout/', logout_user, name='logout'), #  http://localhost:8000/todolist/logout berisi mekanisme logout
]
 ```
 
**✅ Melakukan _deployment_ ke Heroku** terhadap aplikasi todolist agar dapat diakses oleh publik melalui internet. Sebelum melakukan _deployment_, kita perlu membuat aplikasi di Heroku. Kemudian, informasi API key dan nama aplikasi yang telah dibuat, kita simpan dalam _settings-secret repository project_ kita sebagai data pribadi. Kemudian, pada _actions repository_, kita lakukan _deploy_ ke Heroku. Setelah berhasil, kita dapat mengakses link proyek aplikasi. Dalam hal ini, karena kita menggunakan aplikasi Heroku yang sama dengan tugas sebelumnya, kita tinggal melakukan _deploy_.

10. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

 Tambahkan atribut is_finished pada model Task (dengan default value False) dan buatlah dua kolom baru pada tabel task yang berisi status penyelesaian task dan tombol untuk mengubah status penyelesaian suatu task menjadi Selesai atau Belum Selesai.
 Tambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task.
