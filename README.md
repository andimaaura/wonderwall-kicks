# Wonderwall Kicks - Django Project

# Link Website & Repository

Website sudah di deploy melalui PWS dan dapat diakses melalui:

[(https://andi-maura-wonderwallkicks.pbp.cs.ui.ac.id/)]

Kemudian berikut merupakan link repository dari projek Wonderwall Kicks:

[https://github.com/andimaaura/wonderwall-kicks]


#  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm merupakan form bawaan dari fitur Django yang telah menyediakan field username serta password, AuthenticationForm juga melakukan validasi apakah data tersebut sesuai dengan user di database. Melalui AuthenticationForm, developer tidak perlu menuliskan logika login baru lagi dari nol, karena Django telah menghubungkannya langsung dengan autentikasi bawaan. Proses verifikasi juga dilakukan secara otomatis dengan data data yang tersimpan pada database. Kelebihan utama dari AuthenticationForm ialah kemudahan serta kecepatan implementasi. Pengembang apliksi bisa langsung menggunakan fiturnya tanpa harus membuat form secara manual, sehingga risiko risiko kesalahan validasi dapat dihindari. Selain itu, form ini juga terjamin aman karena sudah mengikuti standar dari Django. Integrasi langsung dengan autentikasi bawaan menjadikan AuthenticationForm solusi terbaik pada aplikasi yang membutuhkan sistem login sederhana.

Dibalik kelebihan itu, ada kekurangan dari AuthenticationForm, yakni kurang fleksibel. AuthenticationForm secara default hanya mendukung login dengan field username serta password. Apabila ingin membuat login dengan email, nomor HP, verifikasi OTP, perlu dilakukan kustomisasi khusus untuk membuat form sendiri. AutheticationForm juga lebih berfokus pada fungsi autentikasi bukan pada UI/UX. Jadi, apabila developer ingin menciptakan pengalaman login yang lebih user-friendly, developer akan melakukan kustomisasi khusus pada form. Selain itu, AutheticationFOrm tidak terlalu cocok untuk autentikasi kompleks karena belum bisa terintegrasi dengan sistem login eksternal.

#  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi dan otorisasi adalah dua konsep yang berbeda. Autentikasi sendiri merupakan proses verifikasi identitas user, untuk memastikan bahwa ketika ia login itu memang benar user yang sedang login. Contohnya ketika user login dengan username dan password, apabila data yang dimasukkan valid dan sesua dengan database maka proses autentikasi berhasil dan pengguna dianggap valid. Kemudian, otorisasi sendiri merupakan proses menentukan apa saj ayang boleh dilakukan oleh pengguna setelah ia berhasil melalui proses autentikasi. Misal, apabila ia seorang admin maka ia bisa menambah atau menghapus data, atau pengguna hanya bisa melihat data. Namun, pada kode belum diimplementasikan sistem admin dan pengguna

Django mengimplementasikan autentikasi melalui fitur bawaan berupa fungsi serta class, authenticate() yang berguna untuk verifikasi data kredensial user, kemudian login() dan logout() untuk menentukan status loogin user, serta AuthenticationForm yakni fitur login bawaan dari Django. Kemudian, pada otorisasi Django menyediakan sistem permission serta grup yang bisa diatur sesuai kebutuhan pengembang. Misalnya decorator @permission_required, jadi decorator ini digunakan untuk mengatur hak akses yang lebih spesifik seperti apakah dia user biasa atau admin. Atau decorator @Login_required jadi digunakan untuk membatasi fitur-fitur yang dapat diakses setelah user melakukan login

#  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies serta sessions adalah mekanisme penting yang mengelola data pengguna pada web. Cookies merupakan data kecilyang disimpan pada sisi klien, yakni browser pengguna. Kelebihan dari cookies adalah ia sederhana, mudah untuk digunakan, dan dapat diakses melalui domain tertentu. Cookies juga memungkinkan server untuk menyimpan preferensi dari pengguna tanpa harus menyimpan banyak data pada database server. Tetapi, cookies memiliki kekurangan yakni limit penyimpanan data sekitar 4KB, selain itu cookies juga rentan mengalami pencurian data jika tidak diamankan dengan benar misal lewat XSS attack.

Kemudian,session merupakan penyimpanan data pada server, browser hanya menyimpan session ID dalam bentuk cookie. Kelebihannya ialah lebih aman, karena informasi penting atau sensitif tidak langsung tersimpan pada browser pengguna, kapasitas penyimpanannya juga besar. Session sangat cocok untuk menyimpan data yang kompleks. Namun, kekurangannya ialah session membutuhkan sumber daya tambahan dari sisi server, yang akan menjadi beban tambahan apabila user sangat banyak. Session juga tetap bergantung pada session ID, sehingga kalau cookies dicuri, keamanan tetap terganggu

#  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default, cookies tak sepenuhnya aman. Cookies sangat mudah mengalami serangan seperti XSS maupun hijacking. Selain itu, cookie standar juga dapat diakses melalui javascript, sehingga menaikkan risiko kebocoran data. Dalam mengatasi hal ini, Django melakukan beberapa mekanise bawaan. Django tidak menyimpan data sensitif langsung pada cookie browser, melainkan hanya menyimpan session ID yang merujuk pada data di database server. Django juga memberikan atribut pendukung keamanan pada cookie, seperti HttpOnly yang mencegah javascript untuk mengakses cookie, kemudian Secure yang memastikan bahwa cookie hanya dikirim melalui koneksi HTTPS, kemudian SESSION_COOKIE_AGE yang mengatur masa berlaku cookie agar tidka terlalu lama trsimpan, serta proteksi CSRF yang dapat mencegah cerangan Cross-Site Request Forgery

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1)  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.

Langkah awal yang dilakukan adalah membuat sistem registrasi. login, serta logout untuk user sehingga pengguna dapat mengakses web sesuai dari status login mereka. Saya memanfaatkan UserCreationForm fitur bawaan Django yang telah menyediakan validasi dasar sehingga user hanya perlu mendaftarkan useername dan password. Kemudian, untuk login saya meanfaatkan AutheticationForm yang kemudian dilakukan autentikasi dengan fungsi login(). Apabila data yang dimasukkan benar, maka user akan langsung diarahkan ke halaman utama. Selain itu, saya juga menambahkan cookie last login yang dapat dilihat user pada homepage dari web saya. Kemudian fungsi logout(), apabila user ingin keluar maka cookie dari sesi tersebut akan dihapus agar sesi pengguna benar benar berakhir

2) Membut dua akun pengguna dan dummy data

Setelah proses login berhasil, saya membuat dua akun pengguna pada server lokal untuk keperluan uji coba, keduanya saya beri 3 produk dummy dengan model Product yang telah dibuat sebelumnya. Proses ini saya jalankan dengan melakukan python manage.py runserver kemudian mengisi data data yang diperlukan. Dengan cara tersebut saya emastikan tiap user memiliki produknya sendiri sesuai yang telah dibuat.

3) Menghubungkan model product dengan user

Agar data produk dengan user yang membuat/pemiliknya benar benar terhubung saya membuat relasi antara Product dengan User. Caranya ialah dengan menambahkan field user berupa ForeignKey pada model Product. Selanjutnya dilakukan migrasi agar struktur basis data terbarui. Saya juga mengupdate fungsi tambah produk, sehinga sistem langsung menctata secara otomatis siapa pemilik produk tersebut. Aplikasi tidak hanya menampilkan keseluruhan produk namun dapat memisahkan data berdasarkan siapa pemilik produk tersebut sesuai siapa yang sedang login

4) Menampilkan detail informasi pengguna dan menggunakan cookie last login

Saya menambahkan detail informasi pengguna ynag sedang login kemuian menambahkan cookie last_login yang disimpan pada homepage utam asebagai informasi tambahan untuk user. Setelah user berhasil login, saya membuat sistem agar menciptakan cookie baru yang berisi mengenai informasi waktu terakhir kali pengguna melakukan login. Yang kemudian disajikan dalam bentuk string sehingga mudah dibaca. Kemudian saat halaman utama ditampilkan, ditambahkan logika untuk mengambil last_login dari cookie. Jika cookie ada maka informasi akan ditampilkan.
