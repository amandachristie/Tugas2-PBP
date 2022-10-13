# Tugas 6: Javascript dan AJAX

Nama  : Amanda Christie Tarigan

NPM   : 2106751322

Kelas : D

## **Link**

🔗[**Todolist: New Version**](https://tugas2-pbp-amandachristie.herokuapp.com/todolist)


## 👆🏻 _Asynchronous Programming_ dan _Synchronous Programming_

_Asynchronous programming_ adalah model pemrograman yang menerapkan konsep non-blocking. Ketika suatu proses sedang berlangsung, proses lain dapat dieksekusi tanpa harus menunggu proses bersama. Oleh karena itu, program dapat berjalan secara paralel dan mengirim _multiple request_ ke server. 

Sementara, _synchronous programming_ merupakan model pemrograman yang berbalik dari _asynchronous_, yaitu menerapkan konsep blocking. Ketika suatu proses sedang berlangsung, proses lain tidak dapat dieksekusi hingga proses yang pertama selesai sehingga program hanya dapat mengirim _single request_ ke server. 

## 🤔 Paradigma Event-Driven Programming pada JavaScript dan AJAX

*Event-Driven Programming* adalah suatu paradigma pemrograman dengan alur program ditentukan oleh suatu event oleh user. Event adalah aksi atau kejadian yang terjadi pada halaman webiste dan dilakukan oleh pengguna, seperti button onclick, key pressed, on hover, dan sebagainya. Nantinya akan ada atribut atau method pada JavaScript dan AJAX yang akan meng-handle event tersebut. Contoh penerapan paradigma tersebut adalah sebagai berikut.

Pada saat, menekan button `Reset` maka program akan memanggil fungsi clearField untuk mengosongkan form modals.
```
<a><button class="button3" onclick="clearField()">Reset</button></a>
```

## 📤 Penerapan _Asynchronous Programming_ pada AJAX

AJAX membuat halaman website dapat diperbarui secara asinkronus di mana saat terjadi perubahan pada website, browser tidak perlu me-_reload_ seluruh halaman website terlebih dahulu. Oleh karena itu, saat AJAX mengirimkan request ke server, proses-proses lain dapat dieksekusi tanpa harus menunggu response dari server maupun satu proses selesai dieksekusi terlebih dahulu.

Berikut langkah-langkah penerapan _Asynchronous Programming_ pada AJAX.

- Menambahkan AJAX di awal program dengan memberikan tag `<scripts>` diakhir dengan `</scripts>`
- Menambahkan library AJAX di dalam tag `<head>` 
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```
- Memasukkan potongan kode dengan tag `$.ajax({...})`
- Memproses event dari user akan diproses ke AJAX saat user mengirimkan event tertentu pada server.
- Melakukan transfer data dan menampung segala *event* yang dikirimkan untuk kemudian diproses oleh AJAX.
- Dengan metode *asynchronous programming*, data yang berasal dari pengguna akan diproses secara *server-side scripting*.
- Hasilnya akan ditampilkan pada halaman website secara langsung dengan data baru di dalamnya.

## 👩🏻‍💻 Implementasi Checklist

### AJAX GET

**✅ Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.**
Untuk menampilkan data task dalam bentuk JSON, kita harus mengimpor modul yang diperlukan, yaitu `HttpResponse` dan `serializers`. Kemudian, kita perlu membuat fungis baru sebagai berikut. 
```
def show_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```

**✅ Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.** 
Setelah membuat fungsi pada view, kita harus melakukan routing terhadap fungsi tersebut dengan menambahkan path baru pada `urlpatterns` di file `urls.py` di folder `todolist`.
```
urlpatterns=[
    path('', todolist, name='todolist'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    ...
]
```

**✅ Lakukan pengambilan task menggunakan AJAX GET.**

1. Pada tugas 6, saya membuat template baru, yaitu todolist_ajax.html agar dapat membedakan perbedaan mengambil data dengan django views pada tugas sebelumnya dan mengambil data dengan AJAX GET. 
2. Menambahkan potongan kode library AJAX ke dalam kode program, pada head section.
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```
3. Membuat fungsi untuk mengambil data json sebagai berikut.
```
function getData(){
    $.get('/todolist/json/', function(data){
    generateTaskCard(data);
    })
};
```
4. Membuat fungsi untuk menampilkan data-data yang sudah diambil pada task card.  
        
### AJAX POST

**✅ Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.**

- Membuat tombol "Add Task" yang dapat men-trigger modal berisi form menambahkan task baru.

`<button class ="button1" type="button" data-bs-toggle="modal" data-bs-target="#add-new-task">Add Task</button>`

**✅ Buatlah view baru untuk menambahkan task baru ke dalam database.**

Membuat sebuah fungsi baru bernama `add_task` pada view untuk menambahkan task baru yang dibuat pada modal form.
```
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title, 
            description=description,
            is_finished=False
        )

        context = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
            }
        }

    return JsonResponse(context)
```

**✅ Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.**
Setelah membuat fungsi pada view, kita harus melakukan routing terhadap fungsi tersebut dengan menambahkan path baru pada `urlpatterns` di file `urls.py` di folder `todolist`.
```
urlpatterns=[
    ...
    path('add/', add_task, name='add_task'),
    ...
]
```

**✅ Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add.**

Setelah button add pada modal ditekan, maka kita akan menghubungkan modal dengan path `/todolist/add` dengan menggunakan AJAX POST sebagai berikut. Dapat dilihat bahwa di sini kita mengambil nilai yang disubmit, yaitu title dan description dari task tersebut.
```
$(document).on('submit', '#new-task', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/todolist/add/',
        data: {
        title: $('#title').val(),
        description: $('#description').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        action:'post',
        },
        dataType: 'json',
        success: function(data){
        console.log("Task is created successfully");
        getData();
        ...
        }
    })
})
```

**✅ Tutup modal setelah penambahan task telah berhasil dilakukan.**

Agar modal tertutup setelah penambahan task berhasil dilakukan, kita harus menambahkan potongan kode berikut untuk menyembunyikan modal, backdrop, dan mengosongkan kembali field dari modal untuk menambahkan task. 
 ```
...
$('#add-new-task').modal('hide');
$('.modal-backdrop').remove();
clearField()
...
```
**✅ Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.**

### Implementasi BONUS 🎊

#### AJAX DELETE

**✅ Buatlah kolom baru pada task dengan tombol Hapus.**

`<a href="/todolist/delete-task/${task.pk}"><button class="button3" onclick="deleteTask(${task.pk}) role="button">Delete</button></a>
`

**✅ Buatlah view baru yang menghapus task dengan ID tertentu.**
```
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/todolist")
 ```

**✅ Buatlah path /todolist/delete/{id} yang menerima ID dari path dan meneruskannya kepada view.**

Setelah membuat fungsi untuk menghaous pada view, kita harus melakukan routing terhadap fungsi tersebut dengan menambahkan path baru pada `urlpatterns` di file `urls.py` di folder `todolist`.

```
urlpatterns=[
    ...
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    ...
]
```

**✅ Buatlah fungsi JavaScript yang memanggil endpoint penghapusan task.**
```
function deleteTask(id){
    $.ajax({
        type: 'DELETE',
        url: '/todolist/delete-task/' + id,
        dataType: 'json',
        headers: {
            "X-CSRFTOKEN": "{{ csrf_token }}"
        },
        success: function(data){
        console.log("Successfully deleted!");
        getData();
        }
    })
}
```

**✅ Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.**
