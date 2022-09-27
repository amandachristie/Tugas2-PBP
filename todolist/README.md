Apa kegunaan {% csrf_token %} pada elemen <form>? 
Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

  Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.

 Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

 Membuat sebuah model Task yang memiliki atribut sebagai berikut:

 user untuk menghubungkan task dengan pengguna yang membuat task tersebut.

Kamu dapat menggunakan tipe model models.ForeignKey dengan parameter User.

Untuk mempelajari lebih lanjut mengenai ForeignKey pada Django, silakan baca dokumentasi Django (atau silakan klik disini).

Untuk mempelajari lebih lanjut mengenai model User pada Django, silakan klik disini.

 date untuk mendeskripsikan tanggal pembuatan task.

 title untuk mendeskripsikan judul task.

 description untuk mendeskripsikan deskripsi task.

 Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

 Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

 Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

Dokumentasi Django mengenai Form dapat kamu baca disini.

 Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:

 http://localhost:8000/todolist berisi halaman utama yang memuat tabel task.
 http://localhost:8000/todolist/login berisi form login.
 http://localhost:8000/todolist/register berisi form registrasi akun.
 http://localhost:8000/todolist/create-task berisi form pembuatan task.
 http://localhost:8000/todolist/logout berisi mekanisme logout.
 Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

 Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
   Tambahkan atribut is_finished pada model Task (dengan default value False) dan buatlah dua kolom baru pada tabel task yang berisi status penyelesaian task dan tombol untuk mengubah status penyelesaian suatu task menjadi Selesai atau Belum Selesai.
 Tambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task.
