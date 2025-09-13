**Implementasi Aplikasi BlueKick Sport**

**A. Membuat Proyek Django Baru**

1. Membuat repository di Github
2. Melakukan clone repository ke local
3. Menginisiasi virtual environment python di repo dengan `python -m venv env` dan diaktifkan dengan `source env/bin/activate`
4. Membuat requirements.txt dan melakukan instalasi secara rekursif dengan `pip install -r requirements.txt` untuk dependencies berikut:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
python-dotenv
```

5. Inisiasli proyek django dengan `django-admin startproject football_shop .`
6. Membuat `.env` dan `.env.prod` dan melakukan konfirgurasi databse dan credentials.
7. Melakukan modifikasi pada `settings.py` untuk menambahkan environment variables, setting ALLOWED_HOSTS untuk mengizinkan host yang dapat deploy, menambahkan konfigurasi PRODUCTION, dan menyesuaikan konfigurasi DATABASES.
8. Setelahnya lakukan migrasi dengan `python manage.py migrate`

**B. Membuat aplikasi dengan nama `main` pada proyek**

1. membuat aplikasi dengan `python manage.py startapp main`
2. Menambahkan daftar aplikasi main pada INSTALLED_APPS di `settings.py`

**C. Melakukan Routing pada proyek agar dapat menjalankan aplikasi `main`**

1. Menginisiasikan main pada INSTALLED_APPS di `settings.py`
2. Buat `urls.py` pada aplikasi main
3. Menginisiasikan root ke halaman `views.py` untuk bisa menjalankan aplikasi

**D. Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribute**

1. import models dari django ke dalam `models.py`
2. membuat class Product dengan parameter models.Model
3. Melakukan inisiasi variable yang sesuai dengan atribut wajib yang telah didefinisikan.

**E Membuat fungsi `views.py` dan dikembalikan dalam template HTML**

1. Membuat fungsi `def show_main(request)` pada views.py
2. Dalam `show_main`, berikan return berupa render dengan parameter request, `main.html`, db.
3. Buat folder templates yang berisi `index.html` dalam apps main, dan buat tampilan html di dalamnya.

**Membuat routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**

1. Inisiasi nama app dan pathnya pada `urls.py` di aplikasi main
2. import path dan include pada `urls.py` di folder project, lalu tambahkan route main di sana dengan `path([route], include('main.urls'))` untuk menampilkan aplikasi

**F. Melakukan deployment ke PWS**

1. Membuat project di PWS
2. Menyalin credentials berupa username dan password
3. Menginisiasikan environs sesuai dengan `.env.prods`
4. Menambahkan remote pws ke project dengan `git remote add pws https://pbp.cs.ui.ac.id/vazha.khayri/bluekicksport`
5. lalu push project ke pws dengan

```
git add .
git commit -m "Tugas 2"
git push pws master
```

6. Akan diminta username dan password, masukkan sesuai yang telah diberikan 6. Project di push dan secara otomatis terdeploy

**Bagan Request Client dari Django hingga Response**
![alt text](image.png)

**Peran `settings.py`**
`settings.py` merupakan tempat untuk melakukan konfigurasi project, dalam file tersebut kita dapat melakukan penyesuaian untuk project atau aplikasi yang kita buat, termasuk pengaturan environment, deployment, dan lain-lain.

**Kerja Migrasi Database Django**
Migrasi di django merupakan cara untuk membuat perubahan kepada model yang telah dibuat ke schema database.

Cara kerja migrasi

1. `makemigrations`, untuk membuat migrasi baru berdasarkan perubahan yang dibuat terhadap model
2. `migrate`, untuk memasang/melepas migrasi yg dibuat

Secara singkat migrasi bekerja dengan cara membuat tabel, ataupun kolom baru berdasarkan model yang dibuat atau attribute yang ditambah

**Kenapa Django untuk permulaan?**

- Django dipilih karena menggunakan bahasa python yang terkenal akan readability dan learning curve yang cocok untuk pemula

- Django memiliki dokumentasi yang lengkap dan komprehensif, menjelakan fungsi dengan jelas

- Filosofi "batteries-included" merupakan salah satu aspek utama kenapa Django cocok dijadikan framework untuk pemula, banyak tools yang disediakan secara built-in, seperti autentikasi dan admin panel yang bisa langsung dipakai.

**Feedback Dosen dan asdos tutorial 1**
Saya akan memberikan feedback yang sangat baik untuk kedua belah pihak

- Dosen, Kak Ilma membeirkan pengajaran yang baik, bukan hanya berpacu ke PPT saja, beliau seringkali menggambarkan konsep bagaimana framework Django bekerja denan detail dan memberikan penjelasan yang mudah dimengerti untuk orang yang belum pernah memakai django sebelumnya.

- Asdos sangat membantu, walaupun tutorial 1 dikerjakan secara online. Namun, saya pribadi mendapatkan kendala setelah mengerjakan tutorial 1, asdos secara cepat membalas keluhan saya walaupun waktu sudah malam dan memberikan langkah penyelesaian masalah yang sangat baik sehingga tutorial 1 saya kembali berfungsi.

---

<h1>TUGAS 3<h1/>
