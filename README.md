# Step-by-step implementasi checklist untuk membuat project:

## a. Membuat sebuah proyek Django baru.

Membuat repo baru di github, dihubungkan ke direktori lokal, membuat dan mengaktifkan venv dengan 2 line berikut:
```
python -m venv env
env\Scripts\activate
```
Kemudian, lakukan pip install, dengan melakukan instalasi dependencies berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
lalu membuat proyek django bernama faw_apparel dengan line berikut:
```
django-admin startproject faw_apparel .
```
dan menambahkan localserver dengan meng-edit ALLOWED_HOSTS di settings.py


## b. Membuat aplikasi dengan nama main pada proyek tersebut.
mengaktifkan venv dengan langkah yang telah disebutkan di checklist a, kemudian membuat aplikasi main dengan line:
```
python manage.py startapp main
```
## c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
menambahkan string 'main' ke dalam list INSTALLED_APPS dalam settings.py

## d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: name, price, description
mengimport package models ke dalam models.py dalam folder main, kemudian membuat class dengan nama Product, dengan atribut bernama name, price, and description.
```
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField()
```
lalu melakukan migrasi model untuk melacak perubahan model yang terjadi

## e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
mengimpor render dalam views.py, kemudian membuat fungsi show_main yang menunjukkan nama aplikasi, nama diri, dan kelas. Hal ini dilakukan dengan menambahkan kode berikut:
```
def show_main(request):
  context = {
    'npm' : '2306123456',
    'name': 'Pak Bepe',
    'class': 'PBP E'
  }
  return render(request, "main.html", context)
```
kemudian, dalam folder main, dibuat folder templates yang berisi file main.html sebagai berikut:
```
<h1>{{ app_name }}</h1>
<h2>Name: </h2>
<p>{{ name }}</p>
<h2>Kelas: </h2>
<p>{{ class }}</p>
```
## f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
mengisi urls.py dalam main dengan kode berikut untuk mengonfigurasi URL yang berkaitan dengan aplikasi main:
```
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [path('', show_main, name='show_main'),]
```
melakukan impor
```
from django.urls import path, include
```
dalam urls.py project, kemudian menambahkan
```
path('', include('main.urls')),
```
ke dalam urlpatterns, sehingga rute URL dari aplikasi main terimpor ke project

## g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
membuat proyek baru di PWS, mencatat credentials, menambahkan tautan PWS ke ALLOWED_HOSTS project, mengikuti langkah-langkah dalam PWS untuk men-deploy local project ke proyek PWS.

# Bagan request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan Django](https://i.imghippo.com/files/btdOg1726025205.png)
Pertama, client mengirimkan request ke web server. Web server kemudian meneruskan request ke URLs. URLs kemudian meneruskan request ke views yang berkesesuaian. Setelah view menerima request, views akan meneruskan ke models untuk memperoleh data yang dibutuhkan. Lalu, data diteruskan ke templates, dan disesuaikan dalam templates. Setelah memperoleh tampilan yang sesuai, response diteruskan oleh views.py kembali ke web server. Response kemudian diberikan ke client.

# Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Terdapat beberapa alasan mengapa framework Django dijadikan permulaan pembelajaran, antara lain:
## 1. Penggunaan yang mudah
Django dirancang dengan prinsip "batteries included", yang berarti kebanyakan fitur Django siap digunakan tanpa diperlukannya penambahan konfigurasi lain. Framework Django diciptakan dengan struktur yang jelas dan terorganisir, contohnya MVT, sehingga lebih mudah dipahami dan diimplementasikan.
## 2. Dokumentasi yang komprehensif
Terdapat sangat banyak dokumentasi yang berisikan langkah demi langkah penggunaan Django. Pengguna dapat mengakses dokumentasi yang tersedia _online_ kapan pun dan di mana pun. Akibatnya, Django semakin mudah untuk dipahami.
## 3. Komunitas yang luas
Django digunakan oleh sangat banyak orang. Dengan demikian, banyak forum diskusi _online_ yang ditujukan khusus untuk membahas framework ini. Apabila pengguna menghadapi kesulitan, kemungkinan besar orang lain telah menghadapi masalah yang sama dan solusinya telah dibagikan dalam sebuah forum diskusi _online_.

# Alasan model pada Django disebut sebagai ORM
Django disebut sebagai ORM (Object-Relational Mapping) karena memiliki fungsi sebagai penghubung objek Python dengan database relasional (PostgreSQL, MySQL, SQLite, dll.) dengan cara yang efisien dan otomatis.
