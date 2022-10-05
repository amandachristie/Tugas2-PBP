# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

## **Link**

🔗[**Todolist**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist)

🔗[**Login**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist/login/)

🔗[**Register**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist/register/)

🔗[**Create Task**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist/create-task/)

🔗[**Logout**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist/logout/)

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

## Implementasi Checklist

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

![image](https://user-images.githubusercontent.com/87993867/192826727-7b734ae3-9129-406a-b736-feb01def56e0.png)
![image](https://user-images.githubusercontent.com/87993867/192826740-e74a29eb-55fc-43a6-a801-e3626b12ac16.png)

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


# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

## 🎨 _Inline, Internal,_ dan _External_ CSS 

Terdapat 3 cara untuk menambah CSS ke file HTML dari website kita, yaitu _inline, internal,_ dan _external_ CSS. 

**1. Inline CSS (_inline tag of_ HTML)**. Inline CSS kita gunakan untuk menambahkan _style attribute_ pada tag HTML tertentu. Berikut contohnya: 

```<h1 style="color:red; font-size:14px">Hello World!</h1>```

**Kelebihan:** 

1. Lebih mudah digunakan jika ingin memberikan style pada elemen HTML tertentu saja.
2. Karena prioritasnya lebih tinggi daripada internal dan external style, inline CSS berguna jika kita ingin melakukan perubahan atau perbaikan pada style dengan cepat

**Kekurangan:**
1. Kurang efektif untuk penerapan style pada banyak tag HTML karena harus memberikan style attribute pada setiap tag HTML
2. Jika kita menerapkan banyak style dengan inline CSS, maka struktur file HTML kita akan terlihat berantakan

**2. Internal CSS (_inside_ HTML)**. Internal style kita gunakan dengan mendefinisikan kode CSS di dalam tag `<style>`, di dalam `<head>` HTML. Untuk merujuk pada kode CSS, kita bisa menggunakan ID, class, atau hanya element saja. Contoh:
```
...
<head>
<style>
    .content{
    font-size:12px;
    font-family: ‘Arial’;
    }
</style>
</head>

<body>
    <p class="content">Menggunakan element pada internal style</p>
</body>
...
```
**Kelebihan:**

1. Lebih mudah digunakan untuk satu halaman HTML memiliki tampilan yang unik
2. Tidak perlu membuat file CSS secara terpisah

**Kekurangan:**
1. Meningkatkan _loading time_ pada website karena _styling_ langsung ditambahkan pada file HTML

**3. External CSS (_separated file_)**. External CSS digunakan dengan menambahkan kode CSS pada file CSS terpisah dari file HTML, yaitu `<file-name>.css.` Setiap halaman HTML harus menyertakan referensi ke file css tersebut di dalam elemen `<link>`, di dalam `<head>`. Misalnya, kita membuat file css pada folder yang sama dengan file HTML kita dengan nama `style.css`. Agar styling apda file tersebut dapat kita gunakan, kita perlu memasukkan link sebagai berikut:
```
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```
**Kelebihan:**

1. Karena file CSS terpisah, struktur file HTML bisa terlihat lebih rapi.
2. Style kode CSS yang sama bisa digunakan untuk banyak file HTML dari halaman web kita sehingga lebih efisien.

**Kekurangan:**
1. Halaman website akan butuh waktu untuk mengakses _styling_ yang digunakan dari file CSS sehingga halaman belum tampil dengan sempurna hingga file CSS diakses. 

## 👩🏻‍💻 Tag HTML5

1. `<audio>`        : Menyisipkan audio
2. `<canvas>`       : Menyisipkan area yang dapat digunakan untuk menggambar grafik
3. `<dialog>`       : Menyisipkan dialog box atau subwindow
4. `<figcaption>`   : Menyisipkan caption untuk sebuah figure
5. `<footer>`       : Mendefinisikan bagian footer dari halaman
6. `<header>`       : Mendefinisikan bagian header dari halaman
7. `<nav>`          : Mendefinisikan link navigasi
8. `<menuitem>`     : Mendefinisikan list command yang dapat dipilih user
9. `<figure>`       : Menyisipkan gambar yang diilustrasikan
10. `<main>`        : Mendefinisikan bagian utama atau dominant content dari halaman

## 👆🏻 Tipe-tipe CSS selector

Terdapat 3 jenis selector pada CSS, yaitu:
1. **ID Selectors** menggunakan ID pada tag sebagai selectornya. Pada kode CSS-nya, selector diawali dengan `#`. 

2. **Classes Selectors** menggunakan class pada tag sebagai selectornya. Pada kode CSS-nya, selector diawali dengan `.`

3. **Element Selector** menggunakan tag HTML sebagai selectornya untuk mengubah style yang terdapat dalam tag tersebut.

Ketiga CSS selector di atas sudah diurutkan berdasarkan level prioritasnya. Berikut contoh penggunaan CSS Selector. 
```
...
<head>
<style>
    p{
        font-size:12px;
        font-family: ‘Arial’;
    }

    #heading{
        color: maroon;
        margin-left: 40px;
    }
    .content-section{
        color: alice;
        text-decoration: line-through;
    }
</style>
</head>
...
```
Pengaplikasian pada tag HTML

```
<body>
    <div class="content-section"> <!-- menggunakan class selector -->
        <h1 id="heading">Menggunakan id selector</h1>
        <p>Menggunakan element selector</p>
    </div>
</body>
```

## 🎊 Implementasi Checklist dan BONUS
Kustomisasi template HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

**✅ Kustomisasi template untuk halaman login, register, dan create-task semenarik mungkin.**

Pada tugas 5, saya melakukan kustomisasi template dengan menggunakan External CSS. 
1. Membuat folder `static` pada folder `todolist`. 
2. Di dalam folder tersebut, saya membuat file CSS. 
3. Setiap halaman website saya memiliki file CSS-nya masing-masing dengan nama `login.css`, `create_task.css`, `register.css`, dan `todolist.css`.
4. Di dalam setiap file CSS tersebut saya mendefinisikan class dan element styling yang saya inginkan untuk halaman website saya, misalnya `.items`, `.card-body`, `.message`, dan sebagainya. 
5. Pada file CSS, saya ingin menggunakan font yang tersedia di Google Font, maka saya mengimport url CSS dari font tersebut.
6. Agar style pada file CSS tersebut dapat diakses oleh file HTML saya, maka saya harus menambahkan potongan kode berikut di file HTML saya:
```
<head>
    {% load static %}
    <link rel="stylesheet" href="{% static 'todolist.css' %}">
</head>
```
Melalui potongan kode di atas, file HTML akan me-_load_ static, kemudian melalui tag link, file HTML saya mengakses stylesheet dari file `<nama-file>.css`.

**✅ Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).**

Untuk melakukan kustomisasi pada halaman todolist, saya menggunakan External CSS. Karena kita ingin menggunakan cards, maka saya membuat class `.card` pada file `todolist.css` dengan style sebagai berikut. 
```
.card {
    box-shadow: 0 10px 8px 5px rgba(0,0,0,0.2);
    background-color: rgb(255, 254, 255);
    transition: 0.3s;
    border-radius: 10px;
    padding: 10px; 
    margin: 10px;
}
```
Agar setiap card menampilkan satu task, maka kita gunakan class card di dalam perulangan pada task di file HTML. 
```
...
{% for task in todolist %}
<div class="card">
    {% if task.is_finished == False %}
        <p class="task-title">{{task.title}}</p>
        <p class="task-desc">{{task.description}}</p>
        ...
    {% endif %}
</div>
...
{% endfor %}
```
Dapat kita lihat pada potongan kode di atas, class card membungkus isi task yang didapatkan setiap iterasi dari todolist. 

**✅ Membuat keempat halaman yang dikustomisasi menjadi responsive.**

1. Mengatur `viewport`. Agar halaman website bisa responsive, kita harus memasukkan tag meta viewport pada bagian head dari file HTML. Tag meta viewport memberikan instruksi kepada browser untuk mengontrol dimensi dan skala halaman website. 
2. Mengatur _value_ dari meta viewport ` content="width=device-width`. Nilai ini menginstruksikan halaman untuk menyesuaikan lebar halaman dalam pixel yang tidak bergantung pada perangkat. Hal ini membuat halaman dapat merender konten sesuai dengan ukuran layar.
3. Menambahkan value `initial-scale=1.0` menginstruksikan browser untuk menjaga ukuran CSS _pixels_ dan _device-independent pixels_ berukuran 1:1 sehingga halaman website tetap dapat dilihat dalam mode _landscape. _

Pada folder Tugas2-PBP, terdapat folder `templates` yang berisi file `base.html`. Di dalam file tersebut telah ditambahkan tag meta viewport sebagai berikut.
```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Karena semua file HTML pada aplikasi todolist sudah meng-_extend_ file `base.HTML` sehingga kita tidak perlu lagi memasukkan tag meta viewport pada setiap file HTML.

4. Untuk menyesuaikan ukuran konten pada viewport agar sesuai dengan area pandang user, saya membuat flexbox pada CSS dengan menambahkan potongan kode class berikut. 
```
.items {
    display: flex;
    justify-content: center;
}
```
_Resource:_ https://web.dev/responsive-web-design-basics/ 

**✅ Menambahkan efek ketika melakukan hover pada cards di halaman utama todolist.**

Untuk menambahkan efek saat melakukan hover pada cards, kita dapat membuat class untuk hover pada kode CSS, dengan nama class tersebut adalah nama card yang digunakan ditambah `:hover`.
```
.card:hover {
    box-shadow: 0 8px 16px 0 #4158d0;
    background-color: #eef1fe;
}
```
Dengan potongan kode CSS di atas, pada saat kita melakukan hover pada card, card di halaman todolist akan berubah warna backgroundnya dan box-shadownya. 
