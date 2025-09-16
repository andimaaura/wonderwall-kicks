# Wonderwall Kicks - Django Project

# Link Website & Repository

Website sudah di deploy melalui PWS dan dapat diakses melalui:

[(https://andi-maura-wonderwallkicks.pbp.cs.ui.ac.id/)]

Kemudian berikut merupakan link repository dari projek Wonderwall Kicks:

[https://github.com/andimaaura/wonderwall-kicks]


# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Pada pengimplementasian sebuah platform, umumnya memerlukan komunikasi dengan sistem lain dengan memberikan data kepada pengguna dalam format tertentu. Hal tersebutlah yang membuat data delivery dibutuhkan dalam pengimplementasian sebuah platform. Dengan adanya data delivery, sebuah platform dapat mengirimkan data informasi yang diperlukan client (aplikasi mobile, web, dll) secara terstruktur da konsisten. Apabila tidak ada sistem data delivery yang baik, maka pengiriman informasi akan sulit untuk dilakukan serta rentan untuk menimbulkan berbagai kesalahan. Oleh karena itu, kita memerlukan data delivery dalam proses pengimplementasian platform

# Menurutmu mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON seringkali dianggap lebih unggul dibanding XML karena JSON memiliki sintaks yang sederhana, lebih ringkas, dan mudah difahami oleh manusia. JSON juga langsung kompatibel dengan javascript sehingga banyak digunakan dalam proyek aplikasi web.  Di sisi lain, XML juga memiliki kelebihan. XML mendukung skema yang lebih kompleks dan memungkinkan representasi data yang lebih terstruktur dengan atribut tambahan. Akan tetapi, XML memiliki kekurangan utama yakni strukturnya yang sangat panjang, sehingga ukuran data lebih besar dan lebih sulit dibaca dengan JSON. Oleh karena itu, menurut saya lebih baik JSON dibanding XML

JSON lebih populer dan meningkat pesat karena beberapa keunggulan JSON dibanding XML, seperti keefisiensian JSON yang tidak perlu menggunakan banyak tag seperti XML. Selain itu, sintaks JSON jauh lebih mudah dipahami, karena sintaks JSON menyerupai objek dalam bahasa pemrograman. Kemduian, JSON juga berintergrasi dengan JavaScript sehingga dapat mempermudah proses pengembangan aplikasi berbasis web. 


# Jelaskan fungsi dari method is_valid pada form Django dan memgapa kita membutuhkan method tersebut?

Method is_valid() pada form Django berfungsi untuk melakukan validasi data yang masuk melalui sebuah form. Variasinya meliputi mengecel apakah semua required field sudah terisi, mengecek apakah format datanya sudah sesuai, atau mengecek apakah aturan khusus yang berjalan kalau udah kaya untuk beebrapa hasil, is_valid() mengeluarkan output True. Kalau ada kesalahan bakal keluar False sampai bener sendriri. Tanpa method ini, data yang masuk bisa tidak sesuai dan dapat menyebabkan error saat data sedang digunakan atau mengakibatkan kerentanan keamanan. 

#  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token merupakan suatu sistem keamanan yang berfungsi untuk melindungi aplikasi dari serangan Cross-Site Request Forgery. Serangan CSRF merupakan serangan dimana penyerang memanfaatkan sesi login pengguna yang sedangaktif untuk melakukan tindakan berbahaya tanpa sepengetahuan pengguna. Penyerang dapat membuat halaman palsu yang mengirimkan permintaan ke server dengan memanfaatkan session user yang sedang login. Akibatnya, hal-hal berbahaya seperti perubahan data, penghapusan, atau transaksi dapat terjadi tanpa sepengetahuan dan izin pengguna. Melalui csrf_token, Django dapat memverifikasi apakah permintaan tersebut berasal dari form aplikasi, sehingga dapat mencegah serangan CSRF.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Berikut merupakan tahapan saya dalam mengimplementasikan checklist

1) Membuat views untuk data delivery

Saya menambahkan 4 fungsi views yang dapat mengembalikan data saya melalui format XML, JSON, XML berdasarkan ID, dan JSON berdasarkan ID. Saya menggunakan Django serializers yang dapat otomatis mengubah queryset dari model menjadi representasi data dalam bentuk format tertentu. Fungsi fungsi tersebut berguna untuk mengambil seluruh data model dan mengubahnya ke format yang telah ditentukan. Dengan adanya fungsi ini, sistem saya sudah memiliki kemampuan untuk mengirimkan data kepada client dengan format yang berbeda-beda

2) Menambahkan routing URL

Setelah membuat fungsi fungsi views tersebut, saya menambahhkan fungsi konfigurasi URL, agar fungsi views tersebut dapat diakses baik melalui brwser maupun tools seperti Postman. Pada files urls.py saya menambahkan path() yang mengubungkan masing masing view ke endpoint yang jelas misalnya, /xml/, /json/, dan seterusnya. Hal ini penting agar setiap endpoint memiliki jalur akses yang konsisten. Kemudian saya juga memastikan setiap path diberi nama sehingga bisa lebih mudah dipanggil dalam template apabila diperlukan.

3) Membuat halaman utama (list page)

Saya membuat template HTML yang dapat menapilkan seluruh objek dalam bentuk tabel. Pada setiap data saya telah memberikan tombol Detail agar pengguna dapat mengakses halaman Detail tiap-tiap produk berdasarkan ID. Saya juga menambahkan tombol Add pada halaman tersebut agar user/admin dapat menambahkan produk baru pada web. Halaman list ini berfungsi sebagai sarana atau wadah utama untuk mengakses seluruh fitur yang telah dibuat.

4) Membuat halaman form

Kemudian saya membuat halaman form yang dengan memanfaatkan Django Forms. Saya membuat file forms.py. Pada tombol submit add form, data yang masuk akan diperiksa dengan is_valid(). Jika data valid, maka data akan lanjut disimpan ke database, apabila tidak maka akan mengeluarkan pesan error. Hal ini bertujuan agar proses penambahan data berjalan aman, konsisten, dan terstruktur.

5) Membuat halaman detail dari tiap produk

Halaman ini dihubungkan melalaui button Detail yang ada pada list page. Saat ditekan, maka penggunaa akan diarahkan ke URL sesuai dengan ID objek dan kemudian views akan mengambil data berdasarkan ID tersebut. Template ehalama detail menunjukkan seluruh data informasi lengkap yang telah dipilih. Dengan begitu seluruh objek daat dilihat lebih spesifik bukan sekadar list umum.

# Screenshot request POSTMAN dengan method GET

1) XML
https://image2url.com/images/1758063617634-1758a061-db30-4fa7-853c-481e0445c8c4.png

2) JSON
https://image2url.com/images/1758063736775-d3111c74-06d7-4645-9c9c-39abda07164d.png


Demikian jawaban saya mengenai pertanyaan-pertanyaan pada Tugas 3. Sekian, dan terimakasih banyak Kakak Asdos.

