# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

## **Link**

🔗[**Todolist**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist)

## 🔐 Pentingnya potongan kode `{% csrf_token %}` pada elemen `<form>`
Suatu situs web dapat menerima serangan apabila tidak diproteksi. Salah satu serangan tersebut adalah CSRF (Cross Site Request Forgery). Untuk mengatasi serangan tersebut, Django memiliki sebuah _built in protection_, yaitu `csrf_token`. Kegunaannya adalah  memastikan keamanan seluruh data form POST request dari user ke server.  Proteksi ini menghasilkan token di server saat merender halaman sehingga saat ada permintaan yang masuk, akan diperiksa apakah permintaan tersebut berisis token. Jika tidak, maka tidak akan dieksekusi.

Apabila tidak menggunakan crsf_token, _attacker_ dapat menggunakan user’s authenticated state dan memaksa _end-user_ untuk mengeksekusi tindakan atau mengirimkan permintaan yang tidak sesuai dengan keinginan _user_ pada _web app_. Jika permintaan yang tidak diinginkan itu berhasil dieksekusi, serangan tersebut dapat membahayakan seluruh web app. 

## 🤔 Apakah kita dapat membuat elemen `<form>` secara manual? 

Tentu kita dapat membuat elemen `<form>` secara manual tanpa harus menggunakan generator, seperti {{form.as_table}}). Berikut gambaran besar cara membuatnya secara manual.

1. Membuat form di file HTML yang diawali dengan tag `<form>` dan diakhiri dengan tag `</form>`
2. Kemudian, tambahkan atribut action dan method. Atribut action befungsi untuk mengarahkan ke mana data form akan dikirimkan untuk diproses, sedangkan method berfungsi untuk menjelaskan bagaimana data isian form akan dikirim oleh web app dan berupa GET atau POST.
3. Agar dapat menerima input dari user, kita dapat menambahkan tag <input>.
4. Selanjutnya, kita dapat menambahkan tag atribut `name="<nama-variable>"` sehingga input dari _user_ dapat diambil oleh `views.py` dengan memanggil perintah HTTP Request.

## 📤 Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML

1. User memberikan input data sesuai yang diminta pada form di HTML.
2. Dengan menggunakan perintah `request.POST.get("<name>")`, input data dari user akan diterima oleh fungsi tujuan yang sesuai di `views.py`dan disimpan dalam suatu variabel.
3. Jika data pada form valid, maka fungsi tersebut akan menginisiasi object baru (misalnya, di create-task, menginisiasi object Task baru). 
4. Data object Task akan disimpan ke dalam database menggunakan perintah `<object>.save()`.
5. Untuk mengambil semua object Task sesuai dengan data milik user tertentu, fungsi utama pada `views.py` (misalnya, fungsi todolist) akan menggunakan perintah `Task.objects.filter(user_id=request.user.id)`. 
6. Semua data object Task akan dirender atau dikirimkan ke template HTML sebagai context. 
7. Untuk menampilkan setiap data Task di template HTML, akan dilakukan iterasi pada todolist. 

## Proses Implementasi Checklist

**✅ Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.**

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

Untuk membuat sebuah model Task, kita perlu mengakses file `models.py` di dalam folder `todolist`. Di dalam file tersebut, kita tambahkan kode untuk membuat class dan atribut yang dibutuhkan untuk setiap tipe data `user`, `date`, `title`, `description`, dan `is_finished`.
 ```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # menghubungkan task dengan pengguna yang membuat task tersebut
    date = models.DateTimeField(auto_now_add=True) # mendeskripsikan tanggal pembuatan task
    title = models.CharField(max_length=225) # mendeskripsikan judul task
    description = models.TextField() # mendeskripsikan deskripsi task
    is_finished = models.BooleanField(default=False) # **[BONUS]** mendeskripsikan status penyelesaian task dengan default False (Belum Selesai)
 ```
Setelah itu, kita perlu menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
 
**✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**

Kita membuat fungsi dengan nama `register.py`, `login_user`, `logout_user` pada file `views.py` yang menerima parameter request. Kemudian, kita harus meng-import modul-modul yang dibutuhkan pada bagian paling atas `views.py`. 
```
def register(request):
    form = UserCreationForm() # Menginisiasi form untuk membuat akun user

    if request.method == "POST": 
        form = UserCreationForm(request.POST) # Mengirim data user ke server
        if form.is_valid(): # Kondisi data form valid
            form.save() # Menyimpan data akun ke database
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login') # Mengarahkan ke halaman login
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
```
def login_user(request):
    if request.method == 'POST': 
        username = request.POST.get('username') # Mengambil data username
        password = request.POST.get('password') # Mengambil data password
        user = authenticate(request, username=username, password=password) # Mengautentikasi user
        if user is not None:
            login(request, user) # Melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # Membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # Membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```

**✅ Membuat halaman utama todolist.**

Kita membuat halaman utama todolist sebagai file HTML di folder `templates`. Pada halaman tersebut, terdapat:
1. Username pengguna dengan mengambil data username yang dirender dari fungsi todolist pada views.py. `<h1>Welcome, {{username}}!👋</h1>`
2. Tombol Tambah Task Baru 
```<button> <a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a></button>```
3. Tombol Logout
```<button><a href="{% url 'todolist:logout' %}">Logout</a></button>```
4. Tabel berisi tanggal pembuatan task, judul task, dan deskripsi task dengan format tabel dari HTML dan melakukan iterasi pada todolist.

**✅ Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**

Kita perlu membuat file `forms.py` di folder todolist dan mengimpor forms dari django. Kemudian, kita buat `class TaskForm` untuk data-data yang perlu dimasukkan pengguna sebagai berikut.
```
class TaskForm(forms.Form):
    judul = forms.CharField()
    deskripsi = forms.CharField(widget=forms.Textarea)
```
Kemudian, untuk menampilkan form yang sudah dibuat, masukkan tag `<form></form>` dan di antaranya, kita masukkan `{{ form }}.`

**✅ Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:**

Untuk melakukan routing terhadap fungsi di `views.py` yang telah kita buat, kita harus menambahkan _path_ berikut ini ke `urlpatterns`di file `urls.py` pada folder todolist.
 ```
from django.urls import path
from todolist.views import delete_task, register, login_user, logout_user, todolist, create_task, update_status

app_name = 'todolist'

urlpatterns=[
    path('', todolist, name='todolist'), # http://localhost:8000/todolist (halaman utama)
    path('login/', login_user, name='login'), # http://localhost:8000/todolist/login (form login)
    path('register/', register, name='register'), #  http://localhost:8000/todolist/register (form registrasi akun)
    path('create-task/', create_task, name='create_task'), #  http://localhost:8000/todolist/create-task (form pembuatan tas)
    path('update-status/<int:id>', update_status, name='update_status'), # [BONUS] mekanisme pembaruan status task
    path('delete-task/<int:id>', delete_task, name='delete_task'), # [BONUS] mekanisme penghapusan task
    path('logout/', logout_user, name='logout'), #  http://localhost:8000/todolist/logout (mekanisme logout)
]
 ```
 
✅**Melakukan _deployment_ ke Heroku**

Setelah melakukan add, commit, dan push ke repository, kita perlu melakukan _deployment_ ke Heroku terhadap aplikasi todolist agar dapat diakses oleh publik melalui internet. Dalam hal ini, karena kita menggunakan aplikasi Heroku yang sama dengan tugas sebelumnya, kita tinggal melakukan _deploy_. Setelah berhasil, kita dapat mengakses link proyek aplikasi. Dalam hal ini, karena kita menggunakan aplikasi Heroku yang sama dengan tugas sebelumnya, kita tinggal melakukan _deploy_.

**✅ Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**

### Implementasi BONUS 🎊
1. Tambahkan atribut is_finished pada model Task (dengan default value False) dan buatlah dua kolom baru pada tabel task yang berisi status penyelesaian task dan tombol untuk mengubah status penyelesaian suatu task menjadi Selesai atau Belum Selesai.
Button ubah status akan diproses oleh fungsi `update_status` dengan potongan kode berikut.
```
if updated_task.is_finished:
    updated_task.is_finished = False
else:
    updated_task.is_finished = True
```
Hasil perubahan status disimpan ke database dan dikembalikan ke todolist. 

2. Tambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task.
Button hapus akan diproses oleh fungsi `delete_task` dengan perintah `deleted_task.delete()`
