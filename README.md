## Latihan 1

Pada Latihan 1, kita akan membahas mengenai program yang menggunakan fungsi `random()` untuk menampilkan **n** bilangan acak yang lebih kecil dari 0.5 dan nilai **n** diisi pada saat runtime. Berikut ini kode programnya:

![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/lat1.PNG)

Penjelasan :

 - Baris 1 membangkitkan nilai random menggunakan  fungsi `random()`
 - Baris 2 mendeklarasikan variabel **a** dan menginputkan nilai **N**, dan disini kita menginputkan nilai N=5.
 - Baris 3 mendeklarasikan variabel **jumlah** .
 - Baris 4 menggunakan perintah perulangan **for** berdasarkan jumlah perulangan pada baris ke-3.
 - Baris 5 mendeklarasikan variabel N yang menggunakan fungsi `random.uniform(0, 0.5)` yang berarti batas awal 0 dan batas akhir 0.5 atau bisa diartikan N lebih kecil dari 0.5.
 - Baris 6-7 menampilkan hasil output.
 
 Dan berikut ini outpunya:
 
 ![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/op1.PNG)

## Latihan 2

Pada Latihan 2 ini kita akan membahas program untuk menampilkan bilangan **terbesar** dari **n** buah data yang diinputkan. Berikut ini kode yang digunakan :

![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/lat2.PNG)

Penjelasan :

 - Baris 1-2 mendeklarasikan variabel **x** dan **Terbesar**.
 - Baris 3 mendeklarasikan perulangan **while not** terhadap variabel **x**, yaitu perulangan yang tak terhitung dan  dilakukan berdasarkan kondisi tertentu. Pada program ini menggunakan perulangan **while not** yang berarti perulangan yang jika diinputkan angka **0** akan berhenti.
 - Baris 4 mendeklarasikan variabel **n** dan menginputkan banyaknya data ke dalam variabel **n** oleh user.
 - Baris 5-7 mendeklarasikan kondisi **if** dan menggunakan pernyataan **continue** yang digunakan untuk melanjutkan pada iterasi selanjutnya pada kondisi tersebut.
 - Baris 8-9 mendeklarasikan kondisi **elif**  dan menggunakan pernyataan **break** yang berfungsi untuk menghentikan proses perulangan pada kondisi tersebut,
 - Baris 10 menampilkan bilangan terbesar .
 
 Output yang dihasilkan :
 
 ![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/op2.PNG)
 
## Program 1

Untuk program 1 ini, kita akan membahas mengenai program yang menghitung laba dan keuntungan seorang pengusaha yang menginvestasikan uangnya selama 8 bulan dengan modal awal 100 juta. Pada bulan ke-1 dan ke-2 belum mendapatkan laba (laba=0). Pada bulan ke-3 baru mulai mendapatkan laba sebesar 1% dan pada bulan ke-5 pendapatan meningkat 5%, namun pada bulan ke-8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%.
Berikut ini kode yang digunakan:

![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/program1.PNG)

Penjelasan :

 - Baris 1 mendeklarasikan variabel **modal** yang merupakan modal awal pengusaha tersebut sebesar 100000000 (100juta).
 - Baris 2-3 mendeklarasikan variabel **Laba** dan **Total_laba** .
 - Baris 4 melakukan perulangan dengan menggunakan perulangan **for** .
 - Baris 5 mendeklarasikan kondisi **if** yang menunjukkan untuk bulan 1-2 .
 - Baris 6-7 mendeklarasikan variabel **laba** dan **Total_laba**. Pada bulan ke-1 dan ke-2 belum mendapatkan laba, jadi laba=0.
 - Baris 8 menampilkan hasil pada kondisi tersebut.
 - Baris 9 mendeklarasikan kondisi **elif** untuk bulan 3-4.
 - Baris 10 mendeklarasikan variabel **laba** dan **Total_laba**. Pada bulan ke-3 dan ke-4 mulai mendapatkan laba sebesar 1%. Untuk menghitung laba yaitu **modal * presentase laba / 100**.
 - Melakukan perulangan sesuai dengan range pada kondisi tertentu.
 - Baris 21 menampilkan hasil akhir yaitu **Total laba**.
 
Output yang dihasilkan sebagai berikut:

![enter image description here](https://github.com/kameliacindy/labpy03/blob/master/img/oplaba.PNG)

