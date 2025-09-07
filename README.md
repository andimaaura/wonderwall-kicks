# Wonderwall Kicks - Django Project

# Link Website & Repository

Website sudah di deploy melalui PWS dan dapat diakses melalui:
[(https://andi-maura-wonderwallkicks.pbp.cs.ui.ac.id/)]
Kemudian berikut merupakan link repository dari projek Wonderwall Kicks:
[https://github.com/andimaaura/wonderwall-kicks]


# Penjelasan step-by-step pengimplementasian checklist

1) Membuat projek django baru
        Sebelum membuat proyek, saya memastikan bahwa Python dan Django sudah terinstall di dalam komputer. Kemudian sesuai dengan yang dipelajari pada Tutorial 0, saya membuat virtual environment supaya paket Django dan dependensi lain tidak tercampur dengan sistem utama. Menggunakan perintah
        # python -m venv env
        # env\Scripts\activate

        Kemudian saya mendownload beberapa komponen atau modul yang diperlukan, selanjutnya setelah terdownload saya membuat projek baru Django dengan perintah
        # django-admin startproject wonderwall_kicks .
        Setelahnya django akan otomatis membuat struktur folder dengan file penting seperti settings.py, urls.py, manage.py, dan lain-lain. Kemudian saya akan membuat file .env dan .env.prod yang digunakan untuk menaruh kredensial database kemudian saya juga mengubah beberapa file file penting.

        Setelahnya saya mengecek apakah proyek berjalan dengan baik dengan mengetes menjalankan server lokal dengan perintah
        # python manage.py runserver

        Selanjutnya saya mengunggah proyek repositori saya ke Github sesuai dengan tutorial 0, saya juga menambahkan file gitignore agar file file yang sensitif tidak ikut di push ke repositori github

2)  Membuat aplikasi dengan nama main pada proyek tersebut.
       Setelah projek django berhasil dibuat, aplikasi akan dibuat dengan perintah
       # python manage.py startapp main

       Folder main nantinya akan berisi file-file penting seperti models.py, views.py, urls.py, dan lain-lain.

       Selanjutnya main ini akan ditambahkan pada INSTALLED_APS di settings.py yang berada pada direkotri utama agar django dapat mengenali aplikasi baru ini.

       

3) Melakukan routing agar aplikasi main dapat dijalankan
        Saya menghubungkan routing main di urls.py proyek utama menggunakan include('main.urls') agar halaman utama bisa diakses melalui browser


4) Membuat model Product di aplikasi main    
        Langkah berikutnya ialah mendefinisikan model Product di models.py. Terdapat beberapa atribut yang wajib ada yakni: name, price, description, thumbnail, category, dan is_featured. Kemudian saya menambahkan atribut opsional yakni stock agar data produk lebih lengkap.

        Setelah model dibuat, maka harus dilakukan migrasi database. Dengan menjalankan perintah:

        # python manage.py makemigrations
        # python manage.py migrate

5) Membuat fungsi di views.py
        Saya menambahkan fungsi show_main di views.py yang berfungsi untuk menampilkan nama aplikasi, nama saya, kelas saya, serta npm saya. Fungsi ini mengambil request dari cliend, kemudian menyiapkan data konteks yang nantinya akan dikirim ke template serta mengembalikan response HTML. Tidak lupa saya membuat template HTML didalam folder templates, serta menuliskan template agar dapat menampilkan aplikasi sederhana

6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat di views.py
        Kemudian saya membuat urls.py di folder main untuk memetakan URL ke fungsi show_main di views.py

        Dengan begitu ketika pengguna mengakses URL tsb, Django akan memanggil fungsi show_main dan menampilkan halaman yang sesuai

7)  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

        Setelah aplikasi Django selesai dibuat dan diuji melalui server lokal, saya melalukan deployment ke Pacil Web Service agar aplikasi dapat diakses melalui Internet. Dengan langkah-langkah yang sama seperti di tutorial 0 dan saya juga memastikan environment variable di proyek PWS sudah tersimpan baik

        Selanjutnya setiap ada perubahan, saya menyimpan seluruh perubahan ke GitHub dan PWS. Dengan cara:
        # git add .
        # git commit -m "Complete tutorial 1: Django MVT implementation"
        # git push origin master
        # git push pws master


# Bagan Hubungan Request Client ke web berbasis aplikadi Django

        Berikut merupakan bagan yang sudah saya buat, saya sajikan dalam bentuk link
        [https://image2url.com/images/1757237825274-315bbb4f-4af0-417f-a652-aa325f5107a7.png]

# Peran settings.py dalam proyek Django
        
        Dalam proyek Django, settings.py merupakan file yang berisi konfigurasi utama untuk proyek. Semua pengaturan penting yang mengatur proses Django berjalan ada disini. settings.py berfungsi untuk konfigurasi database, seperti menentukan jenis database yang digunakan, atau mengatur nama database, password, host, port, dan lain-lain. Kemudian di settings.py juga merupakan tempat menentukan aplikasi Django/aplikasi lain yang akan digunakan dalam proyek, nantinya Django akan otomatis memuat aplikasi saat menjalankan server. Selain itu settings.py juga berperan sebagai middleware atau "petugas jaga" buat request dan response, contoh seperti autentikasi, settings.py harus mengecek apakah user sudah login atau belum, dan lain-lain.

# Bagaimana cara kerja migrasi database di Django

        Migrasi sendiri merupakan cara Django mencocokkan struktur database dengan model yang telah dibuat di python. Misal kita punya model Product dengan kolom price dan stock. Migrasi inilah yang harus dilakukan agar di database tabel product punya kolom yang sesuai. Proses migrasi dilakukan apabila kita mengubah model di kode Python, dengan menjalankan perintah
        # python manage.py makemigrations

        Nantinya perintah ini akan membaca seluruh perubahan di model dan membuat file migrasi di folder migrations/. Jadi file ini berfungsi sebagai instruksi yang menyuruh database untuk mengubah tabel. Jadi baru bersifat perencanaan saja belum benar-benar diubah

        Kemudian setelah itu menjalankan perintah:
        # python manage.py migrate
        Saat perintah nya dijalankan, Django akan mulai membaca file migrasi tadi dan langsung melakukan perubahan pada database. Dia hanya membuat perubahan yang dipelrukan tanpa perlu merusak data lain. Sehingga kita tidak perlu membuat tabel manual dengan SQL

# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

        Django sering dipilih sebagai saran abelajar pengembangan software pertama karena Django sangat lengkap dan otomatis. Banyak hal-hal yang biasanya sangat sulit sudah disediakan pada Django seperti pengaturan database, routing URL, autentikasi, dll. Hal ini membuat pemula dapat belajar jauh lebih lancar. Selain itu, Django sudah memiliki banyak fitur bawaan sehingga kita sebagai pemula bisa membuat website yang lengkap hanya dengan sedikit kode. Kemudian, Django mempunyai struktur yang jelas serta konsisten, seluruh file dan folduer memiliki tempat masing-masing. Dan Django juga sangat familiar dikalangan para programmer sehingga banyak dokumentasi serta tutorial yang dapat dipelajari sehingga dapat mencari banyak forum apabila kebingungan

# Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

        Tutorial 1 sangat jelas dan terstruktur. Tutorial 1 sangat membantu untuk memahami alur kerja Django dari model, view, hingga template. Contoh kode yang diberikan pada web juga sangat membantu untuk memperdalam pemahaman. Secara keseluruhan tutorial ini sangat membantu untuk memahami dasar Django, praktik MVT, dan unit testing