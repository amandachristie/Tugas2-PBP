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

## Pengimplementasian Checklist
