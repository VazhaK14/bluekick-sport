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

**C & D. Melakukan Routing pada proyek agar dapat menjalankan aplikasi `main`**

1. Membuat fungsi `def show_main` pada views.py
2. Menginisiasikan nama app dan pathnya pada `urls.py` di aplikasi main
3. import path dan include pada `urls.py` di folder project, lalu menambahkan route main di sana dengan `path('', include('main.urls'))`

**C. Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribute**

1. import models dari django ke dalam `models.py`
2. membuat class Product dengan parameter models.Model
3. Melakukan inisiasi variable yang sesuai dengan atribut wajib yang telah didefinisikan.

**E. Melakukan deployment ke PWS**

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

Akan diminta username dan password, masukkan sesuai yang telah diberikan 6. Project di push dan secara otomatis terdeploy
