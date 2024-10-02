# Tugas 2

## 1. Step-by-step implementasi checklist untuk membuat project:

### a. Membuat sebuah proyek Django baru.

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


### b. Membuat aplikasi dengan nama main pada proyek tersebut.
mengaktifkan venv dengan langkah yang telah disebutkan di checklist a, kemudian membuat aplikasi main dengan line:
```
python manage.py startapp main
```
### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
menambahkan string 'main' ke dalam list INSTALLED_APPS dalam settings.py

### d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: name, price, description
mengimport package models ke dalam models.py dalam folder main, kemudian membuat class dengan nama Product, dengan atribut bernama name, price, and description.
```
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField()
```
lalu melakukan migrasi model untuk melacak perubahan model yang terjadi

### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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
### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
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

### g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
membuat proyek baru di PWS, mencatat credentials, menambahkan tautan PWS ke ALLOWED_HOSTS project, mengikuti langkah-langkah dalam PWS untuk men-deploy local project ke proyek PWS.

## 2. Bagan request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan Django](https://i.imghippo.com/files/btdOg1726025205.png)
Pertama, client mengirimkan request ke web server. Web server kemudian meneruskan request ke URLs. URLs kemudian meneruskan request ke views yang berkesesuaian. Setelah view menerima request, views akan meneruskan ke models untuk memperoleh data yang dibutuhkan. Lalu, data diteruskan ke templates, dan disesuaikan dalam templates. Setelah memperoleh tampilan yang sesuai, response diteruskan oleh views.py kembali ke web server. Response kemudian diberikan ke client.

## 3. Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Terdapat beberapa alasan mengapa framework Django dijadikan permulaan pembelajaran, antara lain:
### a. Penggunaan yang mudah
Django dirancang dengan prinsip "batteries included", yang berarti kebanyakan fitur Django siap digunakan tanpa diperlukannya penambahan konfigurasi lain. Framework Django diciptakan dengan struktur yang jelas dan terorganisir, contohnya MVT, sehingga lebih mudah dipahami dan diimplementasikan.
### b. Dokumentasi yang komprehensif
Terdapat sangat banyak dokumentasi yang berisikan langkah demi langkah penggunaan Django. Pengguna dapat mengakses dokumentasi yang tersedia _online_ kapan pun dan di mana pun. Akibatnya, Django semakin mudah untuk dipahami.
### c. Komunitas yang luas
Django digunakan oleh sangat banyak orang. Dengan demikian, banyak forum diskusi _online_ yang ditujukan khusus untuk membahas framework ini. Apabila pengguna menghadapi kesulitan, kemungkinan besar orang lain telah menghadapi masalah yang sama dan solusinya telah dibagikan dalam sebuah forum diskusi _online_.

## 4. Alasan model pada Django disebut sebagai ORM
Django disebut sebagai ORM (Object-Relational Mapping) karena memiliki fungsi sebagai penghubung objek Python dengan database relasional (PostgreSQL, MySQL, SQLite, dll.) dengan cara yang efisien dan otomatis.


# Tugas 3

## 1. Pentingnya Implementasi Data Delivery dalam Sebuah Platform
Secara definisi, _data delivery_ adalah proses pemindahan data dari satu titik ke titik lainnya. Salah satu contoh _data delivery_ adalah penggunaan API pada platform. Adapun alasan perlunya diimplementasikan _data delivery_, antara lain:
**a. _User-experience_ yang baik:** Sistem _data delivery_ yang mumpuni diperlukan oleh sebuah platform agar pengguna dapat memperoleh informasi yang diinginkan secara tepat waktu, seperti konten terbaru, preferensi pengguna, dan data transaksi.
**b. Integrasi dengan layanan lain:** Kebanyakan platform bergantung kepada layanan pihak ketiga, seperti sistem pembayaran, _tools_ analitik, dsb. _Data delivery_ sangat krusial bagi layanan-layanan ini untuk dapat berfungsi dengan baik.
**c. Pemrosesan data _real-time_:** Pemrosesan data _real-time_ penting agar fitur-fitur kebanyakan platform dapat berfungsi, seperti notifikasi, pembaruan grafik (co: harga saham), dll. Sistem _data delivery_ yang efektif dan efisien penting agar fitur-fitur ini dapat berfungsi semestinya.

## 2. XML Vs Json
XML (_Extensible Markup Language_) dan JSON (JavaScript _Object Notation_) adalah format serialisasi data yang memperbolehkan pertukaran data antar aplikasi, platform, atau sistem. Apabila kita bekerja dengan tipe data yang berbeda-beda dan variabel yang banyak, maka XML lebih baik untuk digunakan. Hal ini dikarenakan XML memeriksa _error_ dalam data yang kompleks secara lebih efisien daripada JSON, karena XML memang difokuskan untuk menyimpan data dengan cara yang _machine-readable_. XML juga memiliki _tools_ dan _libraries_ yang sudah cukup berkembang dan dapat digunakan untuk sistem-sistem lawas yang masih digunakan. Sementara itu, JSON didesain untuk pertukaran data dengan format yang lebih sederhana dan efisien, sehingga memiliki performa dan kecepatan yang cenderung lebih tinggi. Dengan demikian JSON lebih diutamakan untuk API, aplikasi _mobile_, dan penyimpanan data, sementara XML lebih baik untuk data dengan struktur yang lebih kompleks dan membutuhkan pertukaran data.

Meski sama-sama memiliki kelebihan dan kekurangan, format JSON lebih umum digunakan daripada XML. Hal ini dikarenakan JSON tidak sekompleks XML dan tidak menggunakan struktur tags, sehingga lebih mudah dibaca dan dipahami oleh manusia. Format JSOn juga dapat menjadi representasi data yang sama dengan XML tetapi dengan ukuran file yang lebih kecil. Selain itu, JSON terkenal lebih aman dari XML, karena XML rentan terhadap modifikasi tanpa izin.

## 3. Method is_valid()
Method is_valid() dibutuhkan untuk memastikan bahwa data yang dimasukkan ke form sudah benar sebelum diproses lebih lanjut (misalnya disimpan ke database). Dengan cara ini, data yang tidak valid dapat ditangani (misalnya dengan menampilkan pesan kesalahan kepada pengguna) dan error atau hasil yang tidak diinginkan ketika memproses data yang tidak sesuai dapat dihindari.

## 4. Pentingnya csrf_token
csrf_token (Cross-Site Request Forgery token) dibutuhkan untuk memastikan bahwa permintaan yang dikirimkan oleh pengguna berasal dari sumber yang sah, yaitu aplikasi web itu sendiri. Django menggunakan CSRF token untuk memverifikasi bahwa setiap permintaan POST (atau metode HTTP lainnya yang mengubah data) berasal dari pengguna yang valid, bukan dari sumber eksternal yang berbahaya. Jika kita tidak menambahkan csrf_token pada form, aplikasi Django akan rentan terhadap serangan CSRF. Serangan CSRF biasanya memanfaatkan pengguna yang sudah login ke suatu aplikasi web yang tidak terlindungi. Penyerang bisa membuat sebuah halaman web atau email yang berisi elemen tersembunyi (seperti form atau permintaan AJAX) yang mengarahkan pengguna ke aplikasi target tanpa mereka sadari.

## 5. Step-by-step checklist
**Membuat input form:** membuat forms.py sebagai struktur utama form kemudian menyesuaikan views.py agar menampilkan form yang diinginkan. Setelah itu, dibuat berkas html form yang meng-extend html base untuk menampilkan form. Setelah itu, dibuat routing dari urls.py ke path-path yang berkaitan.
**Menambahkan 4 fungsi view:** dalam views.py, dibuat fungsi show_xml dan show_json yang me-return HttpResponse serialisasi dalam bentuk XML dan JSON. Kemudian, dengan cara yang sama, dibuat fungsi show_xml_by_id dan show_json_by_id yang menerima parameter pkid. Kedua fungsi ini me-return HttpResponse yang sudah difilter agar hanya menampilkan objek dengan id yang sesuai.
**Membuat routing url:** Menambahkan path setiap method ke urlpatterns dalam urls.py
```
...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
...
```

## 6. Keempat URL views dalam postman
**show_xml**
![show_xml](https://i.ibb.co.com/qFTpTxF/Screenshot-640.png)
**show_json**
![show_json](https://i.ibb.co.com/VLkxLJP/Screenshot-641.png)
**show_xml_by_id**
![show_xml_by_id](https://i.ibb.co.com/prVZ6GL/Screenshot-642.png)
**show_json_by_id**
![show_json_by_id](https://i.ibb.co.com/mFhVrvt/Screenshot-643.png)

# Tugas 4

## 1. HttpResponseRedirect() vs redirect()
**HttpResponseRedirect()** merupakan respon HTTP di Django yang mengarahkan pengguna ke URL lain. Fungsi ini mengembalikan objek respon dengan kode status HTTP 302 (Found) atau 301 (Moved Permanently). URL tujuan harus diberikan secara langsung sebagai argumen. Contohnya:
```
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some/url/')
```
**redirect()** adalah fungsi helper yang disediakan oleh Django dalam modul django.shortcuts. Fungsi ini lebih fleksibel karena dapat menerima berbagai argumen, antara lain:
* URL absolut atau relatif
* URL pattern name dan argumen posisional atau keyword untuk membangun URL menggunakan fungsi reverse()
* Objek yang memiliki metode get_absolute_url()
Contohnya:
```
from django.shortcuts import redirect

def my_view(request):
    return redirect('my-view-name', foo='bar')
```

## 2. Penghubungan model Product dengan User
Product dan User dihubungkan dengan cara menambahkan foreign key User ke Product. Hal ini dilakukan dengan menyisipkan potongan kode berikut dalam fungsi create_product:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

## 3. Authentication vs authorization
**Authentication:**
* Proses verifikasi identitas pengguna
* Dipastikan bahwa identitas yang dimasukkan sesuai dengan pengguna 
* Dalam konteks login, biasanya melibatkan pemeriksaan username dan password
**Authorization:**
* Proses menentukan hak akses atau izin yang dimiliki pengguna
* Menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna dalam sistem
* Contoh: dosen memiliki akses yang berbeda dengan mahasiswa di SCELE

## 4. Mengingat login & cookies
**Cara Django mengingat pengguna yang Login:**
* Menggunakan mekanisme session yang didukung oleh cookies
* Setelah pengguna berhasil login, Django membuat sesi baru dan menyimpan ID sesi tersebut dalam cookie dalam browser pengguna
* Setiap kali pengguna membuat permintaan baru, cookie ini dikirim kembali ke server, memungkinkan Django untuk mengidentifikasi pengguna
* Informasi sesi disimpan di server (database, cache, atau file), bukan di cookie, sehingga meningkatkan keamanan

**Kegunaan Lain dari Cookies:**
* Menyimpan preferensi pengguna (co: bahasa pilihan, tema tampilan)
* Mengingat keranjang belanja sebelum checkout (dalam platform _e-commerce_)
* Mengingat informasi login untuk sesi berikutnya, sehingga tidak perlu login lagi (co: Google)
* Mengumpulkan data untuk analisis perilaku pengguna (dengan consent)
* Menyajikan konten yang disesuaikan berdasarkan interaksi pengguna sebelumnya

**Keamanan Cookies:**
Tidak Semua Cookies Aman. Jika tidak dienkripsi, data sensitif dapat dicuri melalui serangan man-in-the-middle. Aplikasi yang rentan terhadap Cross-Site Scripting juga memungkinkan penyerang untuk mencuri cookies dan mengambil alih sesi pengguna. Cookies pihak ketiga juga dapat digunakan untuk pelacakan lintas situs yang mengganggu privasi.

## 5. Implementasi checklist
**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar:** Memanfaatkan fungsi login, logout, dan form dari django.contrib.auth untuk membuat fungsi yang sesuai di views.py
**Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal:** Melakukan input manual di website
**Menghubungkan model Product dengan User:** dengan foreign key

# Tugas 5

## 1. Urutan prioritas CSS selector
Ketika beberapa CSS selector berlaku pada satu elemen HTML, urutan prioritas ditentukan berdasarkan specificity dan urutan deklarasi. Aturan prioritas dalam CSS adalah sebagai berikut:
* **Inline style**
* **ID selectors**
* **Class selectors**
* **Element selectors**
* Jika dua selector memiliki specifity yang sama, maka yang ditulis terakhir akan diterapkan

## 2. Pentingnya responsive design
Responsive design penting karena perangkat yang digunakan untuk mengakses situs web sangat bervariasi, mulai dari _smartphone_, tablet, hingga komputer desktop dengan berbagai ukuran layar. Dengan menggunakan responsive design, tampilan dan fungsi situs web akan menyesuaikan diri secara otomatis sesuai dengan ukuran layar pengguna. Dengan demikian, user experience dapat ditingkatkan dan aksesibilitas menjadi lebih baik di setiap perangkat.
Contoh situs yang sudah menerapkan: X, Google, Youtube
Contoh situs yang belum menerapkan: Space Jam, LingsCars.com, dan situs-situs lama lainnya

## 3. Perbedaan margin, border, dan padding
Margin, border, dan padding merupakan tiga elemen yang saling terkait. Penjelasan masing-masing elemennya antara lain:
* Margin adalah ruang di luar elemen, yang mengatur jarak antara elemen tersebut dan elemen lainnya
* Border adalah garis di sekitar elemen, yang bisa memiliki ketebalan, warna, dan gaya tertentu (misalnya, solid, dashed)
* Padding adalah ruang di dalam elemen, yang mengatur jarak antara konten elemen dan batas border elemen tersebut

## 4. Konsep flexbox dan grid layout
Flexbox (Flexible Box Layout) adalah model _layout_ yang memungkinkan elemen untuk diatur secara dinamis dalam satu arah (horizontal atau vertikal) dan mendistribusikan ruang di antara flexbox secara efisien, walaupun ukuran elemen tidak diketahui sebelumnya. Sementara itu, grid layout adalah model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom (layout tabel). Layout ini memberikan kontrol untuk membuat tata letak yang kompleks dengan kemampuan untuk mengatur elemen di berbagai sel.

## 5. Implementasi step-by-step

### a. Implementasikan fungsi untuk menghapus dan mengedit product
#### Edit:
Pertama, diperoleh product dengan id yang sesuai menggunakan
```
product = Product.objects.get(pk=id)
```
Kemudian, dibuat form berikut
```
form = ProductEntryForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
```
Lalu ditambahkan statement return berikut
```
return render(request, "edit_product.html", context)
```
#### Delete:
Pertama, diperoleh product dengan id yang sesuai menggunakan
```
product = Product.objects.get(pk=id)
```
Kemudian, object product di-delete
```
product.delete()
```
Lalu di-return HttpResponseRedirect
```
return HttpResponseRedirect(reverse('main:show_main'))
```
#### Langkah selanjutnya:
Path delete dan edit ditambahkan ke urls.py, kemudian dibuat file html untuk fungsi edit product yang sesuai.

### b. Kustomisasi design
#### Navbar
Buat file navbar.html dalam root
```
<nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-center text-white">FawApparel</h1>
        </div>
        <div class="hidden md:flex items-center">
          {% if user.is_authenticated %}
            <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
      <div class="pt-2 pb-3 space-y-1 mx-auto">
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");

      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```
Kemudian, file-file html yang ber-navbar ditambahkan line include
```
{% include 'navbar.html' %}
```
#### Login, register, dan tambah product
Pertama, halaman login dikustomisasi
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
Kemudian halaman register
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
Tambah product
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
#### Daftar product
Pertama, dibuat file card_info.html yang akan menunjukkan informasi pengguna
```
<div class="bg-indigo-700 rounded-xl overflow-hidden border-2 border-indigo-800">
    <div class="p-4 animate-shine">
      <h5 class="text-lg font-semibold text-gray-200">{{ title }}</h5>
      <p class="text-white">{{ value }}</p>
    </div>
</div>
```
Kemudian, dibuat file card_product.html yang akan menunjukkan informasi produk
```
<div class="relative break-inside-avoid">
  <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-0 transition-transform duration-300">
    <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
      <h3 class="font-bold text-xl mb-2">{{product.name}} ({{product.price}})</h3>
      <p class="text-gray-600">{{product.time}}</p>
    </div>
    <div class="p-4">
      <p class="font-semibold text-lg mb-2">{{product.description}}</p>
      <p class="text-gray-700 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product.feelings}}</span>
      </p>
    </div>
  </div>
  <div class="absolute top-8 -right-0 flex space-x-1">
    <a href="{% url 'main:edit_product' product.pk %}" class="hover:bg-yellow-600 text-white rounded-xl p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product.pk %}" class="hover:bg-red-600 text-white rounded-xl p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</div>
```
Lalu main.py disesuaikan
```
<div class="relative break-inside-avoid">
  <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-0 transition-transform duration-300">
    <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
      <h3 class="font-bold text-xl mb-2">{{product.name}} ({{product.price}})</h3>
      <p class="text-gray-600">{{product.time}}</p>
    </div>
    <div class="p-4">
      <p class="font-semibold text-lg mb-2">{{product.description}}</p>
      <p class="text-gray-700 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product.feelings}}</span>
      </p>
    </div>
  </div>
  <div class="absolute top-8 -right-0 flex space-x-1">
    <a href="{% url 'main:edit_product' product.pk %}" class="hover:bg-yellow-600 text-white rounded-xl p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product.pk %}" class="hover:bg-red-600 text-white rounded-xl p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</div>
```
