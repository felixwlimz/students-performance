# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. 
Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Hal tersebut menjadi masalah yang cukup serius bagi institusi, karena dapat mempengaruhi reputasi serta akreditasi dari institusi tersebut 

### Permasalahan Bisnis

Jaya Jaya Institut menghadapi tingkat dropout mahasiswa yang cukup tinggi setiap tahunnya. 
Kondisi ini menjadi perhatian serius karena dapat berdampak langsung terhadap reputasi institusi,
efektivitas proses belajar-mengajar, serta efisiensi penggunaan sumber daya.

Permasalahan bisnis yang dihadapi antara lain :

- Tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikan tepat waktu atau berhenti di tengah jalan, 
yang berdampak pada reputasi institusi serta akreditasi kampus. 

- Kurangnya pemahaman tentang faktor-faktor yang menyebabkan mahasiswa dropout, 
sehingga sulit untuk mengambil tindakan pencegahan yang efektif.

- Tidak adanya sistem ataupun metode yang dapat mengidentifikasi mahasiswa yang beresiko tinggi untuk dropout, 
yang menyebabkan keterlambatan dalam mengatasi masalah oleh kampus. 

- Efek finansial dan operasional akibat dropout, seperti kehilangan pendapatan dari biaya kuliah,
  serta pemborosan sumber daya yang telah dikeluarkan untuk mahasiswa tersebut.

Dengan memahami secara jelas permasalahan ini, Jaya Jaya Institut dapat menyusun kebijakan dan strategi berbasis data untuk menekan angka dropout dan meningkatkan kualitas pendidikan secara menyeluruh.



### Cakupan Proyek

Cakupan proyek ini adalah sebagai berikut:

1. **Eksplorasi Data dan Pemahaman Data** menganalisis dataset yang ada untuk memahami pola dan karakteristik mahasiswa 

2. **Prapemrosesan Data** - Membersihkan nilai yang hilang dan Encoding nilai untuk analisis lebih lanjut 

3. **Analisis Faktor penyebab dropout** :
- Menggunakan teknik statistik dan visualisasi untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap dropout mahasiswa

4. **Pembuatan Business Dashboard** : Visualisasi dalam bentuk data dan bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab dropout mahasiswa

5. **Pembuatan Model Prediksi** : Membangun model machine learning untuk memprediksi mahasiswa yang berpotensi dropout

6. **Kesimpulan dan Rekomendasi** : Menarik kesimpulan dari analisis dan memberikan rekomendasi praktis untuk mengurangi dropout mahasiswa



### Persiapan

1. Sumber Data 
Sumber data yang digunakan dalam proyek ini adalah [Jaya Jaya Institut Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md).

2. Mempersiapkan Enviroment Pengembangan : 

- Jalankan Setup Enviroment pada Anaconda dengan mengunakan perintah berikut : 
```
conda create --name main-ds python=3.9 
conda activate main-ds
pip install -r requirements.txt
```
- Setup enviroment pada Shell/ Terminal dengan menggunakan perintah berikut 

```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

```

3. Menjalankan notebook.ipynb

- Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file requirements.txt untuk melihat dependensi yang dibutuhkan).
- Jalankan seluruh isi file notebook.ipynb menggunakan Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.

4. **Menjalankan dashboard Metabase** : Untuk melihat isi dashboard secara langsung, dapat menggunakan metabase dengan bantuan Docker (pastikan Docker sudah terinstall).

- Untuk menjalankan metabase ketik perintah berikut 
`docker pull metabase/metabase:v0.46.4`

- Untuk menjalankan container metabse pada perintah berikut : 
`docker run -p 3000:3000 --name metabase metabase/metabase`

- Login ke metabase menggunakan username dan password berikut : 
  email : root@mail.com
  password : felix12345

## Business Dashboard
z
Hasil dari analisis data dan visualisasi yang telah dilakukan dapat dilihat pada dashboard Metabase yang telah dibuat.
Dari hasil analisis tersebut disajikan dalam bentuk dashboard yang memudahkan perusahaan untuk melihat dashboard secara realtime : 

1. Distribusi Status perkawinan, Kelas, dan perpindahan 
2. Distribusi dropout berdasarkan gender, murid, performa, serta status mahasiswa
3. Distribusi umur, admisi dan kualifikasi mahasiswa

## Menjalankan Sistem Machine Learning

Untuk menjalankan sistem machine learning yang telah dibuat dapat dilakukan dengan langkah langkah sebagai berikut : 

[Link Dashboard](https://students-performance-1.streamlit.app/)


## Conclusion
Dari proyek ini kita telah berhasil menyelesaikan permasalahan yang dihadapi oleh Jaya Jaya Institut dengan melakukan analisis data, identifikasi faktor penyebab dropout, serta pembuatan model prediksi untuk mengurangi tingkat dropout mahasiswa.
Cakupan tersebut meliputi:

1. **Menentukan faktor-faktor yang menyebabkan siswa yang dropout**.
 - Nilai akademik yang rendah 
 - Kendala finansial 
 - Tingkat kehadiran yang rendah 
 Dashboard yang disediakan memvisualisasikan faktor-faktor ini secara interaktif sehingga memudahkan tim manajemen dalam melakukan pemantauan.


2. **Memprediksi siswa mana saja yang berpotensi tidak menyelesaikan pendidikannya**.
Model prediktif yang dikembangkan mampu mengidentifikasi mahasiswa yang berpotensi tidak menyelesaikan studinya dengan 
tingkat akurasi yang baik. Hal ini memungkinkan institusi untuk mengambil tindakan preventif, seperti memberikan bimbingan akademik, 
dukungan finansial, atau konseling.


3. **Meningkatkan performa mahasiswa agar mengurangi dropout**.  
Dari hasil analisis dan prediksi, kami beberapa rekomendasi strategis sebagai berikut:

- Menyediakan program pendampingan dan bimbingan belajar untuk mahasiswa dengan nilai dibawah rata rata.
- Memberikan beasiswa atau bantuan dana bagi mahasiswa yang kesulitan secara finansial.
- Meningkatkan keterlibatan mahasiswa dalam kegiatan kampus guna memperkuat keterikatan terhadap institusi dan memaksimalkan unit bagian Kemahasiswaan.

Dengan pendekatan ini, Jaya Jaya Institut dapat lebih proaktif dalam menurunkan tingkat dropout dan meningkatkan kualitas lulusan secara keseluruhan.

### Rekomendasi Action Items

Berikut adalah beberapa rekomendasi tindakan (action items) yang dapat dilakukan oleh Jaya Jaya Institut untuk mengatasi masalah tingginya tingkat dropout mahasiswa dan meningkatkan keberhasilan studi:

- **Mengembangkan sistem monitoring mahasiswa berbasis data**
Membangun dashboard atau sistem monitoring rutin dapat mendeteksi dini mahasiswa yang ingin melakukan dropout. 
dari faktor-faktor seperti performa akademik, kehadiran, keterlibatan dan faktor-faktor lainnya seperti sosial dan ekonomi. 

- **Program pendampingan akademik**
Menyediakan program pendampingan akademik bagi mahasiswa yang berisiko tinggi untuk dropout.

-**Memberikan dukungan finansial**
Memberikan bantuan finansial seperti beasiswa atau bantuan diskon uang kuliah untuk mahasiswa yang mengalami kesulitan ekonomi.

- **Meningkatkan keterlibatan mahasiswa**
Memaksimalkan unit bagian Kemahasiswaan dan memaksimalkan Organisasi kemahasiswaan untuk menentukan arah dan minat mahasiswa tersebut 

- **Pelatihan untuk dosen dan staf**
Melatih tenaga pengajar agar dapat lebih responsif terhadap tanda-tanda mahasiswa yang kesulitan dan memberikan intervensi tepat waktu melalui pendekatan yang lebih personal.