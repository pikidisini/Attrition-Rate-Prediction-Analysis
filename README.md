# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan tersebut memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Untuk mencegah hal ini semakin parah, manajer departemen HR ingin mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, dibutuhkan juga business dashboard untuk membantu memonitor berbagai faktor tersebut.

### Permasalahan Bisnis

1. Kesulitan dalam pengelolaan karyawan yang berimbas pada tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan).
2. Manajer departemen HR ingin mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.
3. Dibutuhkan business dashboard untuk membantu memonitor berbagai faktor tersebut.

### Cakupan Proyek

1. Mencari tahu apa saja faktor penyebab tingginya "Attrition" rate di perusahaan Jaya Jaya Maju.
2. Membangun sistem prediktif untuk mendeteksi potensi risiko keluar.
3. Membangun business dashboard menggunakan Metabase untuk memantau faktor-faktor utama attrition secara visual.

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv

#### Setup environment:

##### Windows

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
##### Linux/Mac

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

##### Conda

```
conda create --name attrition-ds python=3.10.6
conda activate attrition-ds
pip install -r requirements.txt
```

## Business Dashboard

Dalam proyek ini, saya juga membangun business dashboard yang memungkinkan manajer HR untuk memonitor berbagai faktor yang mempengaruhi attrition rate. Dashboard ini dibuat menggunakan Metabase. Dashboard beserta database instance telah di ekspor pada `metabase.db.mv.db` yang disimpan pada direktori `metabase-data` dan telah disediakan file `docker-compose.yml` pada direktori utama untuk menjalankan dashboard.

### Jalankan Dashboard Metabase Docker

1. Install Docker Download & install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Jalankan Metabase Container
   ```
   docker-compose up -d
   ```
3. Buka di Browser: http://localhost:3000
4. Untuk menghentikan Container
   ```
   docker-compose down
   ```
   
- **Email**: root@mail.com  
- **Password**: root123

Dashboard ini menyajikan visualisasi mengenai:

- Attrition Rate Meter: Menampilkan tingkat atau score attrition secara kesuluruhan
- Attrition Rate berdasarkan Over Time: Menampilkan nilai attrition berdasarkan status over time karyawan.
- Attrition Rate berdasarkan Stock Option Level: Menampilkan nilai attrition berdasarkan level stock option dari karyawan.
- Attrition Rate berdasarkan Monthly Income: Menampilkan nilai attrition berdasarkan rentang pendapatan karyawan.
- Attrition Rate berdasarkan Masa Kerja: Menampilkan nilai attrition rate berdasarkan rentang masa kerja karyawan.
- Attrition Rate berdasarkan Job Role: Menampilkan Nilai attrition rate berdasarkan posisi atau role karyawan.

Parameter atau Variabel tersebut diambil berdasarkan hasil pelatihan model terhadap temuan fitur fitur penting dan temuan pada proses eksplorasi data.

## Conclusion

Setelah melakukan eksplorasi data dan membangun model prediktif, beberapa faktor yang mempengaruhi tingginya attrition rate di perusahaan Jaya Jaya Maju dapat diidentifikasi, seperti:

1. Pendapatan bulanan yang paling rendah memiliki tingkat attrition yang tinggi, disebabkan oleh ketidaksesuaian pendapatan dengan standar industri.
2. Status Overtime Karyawan yang sering bekerja lembur cenderung lebih tinggi attrition-nya, mengindikasikan kemungkinan beban kerja berlebih atau kompensasi lembur yang tidak memadai.
3. Stock option level mempengaruhi tingginya nilai attrition pada karyawan dengan level stock yang rendah. Kurangnya kepemilikan saham membuat karyawan merasa kurang terlibat secara jangka panjang.
4. Masa jabatan rendah memiliki tingkat attrition yang tinggi, disebabkan oleh kuranganya jaminan karir dalam perusahaan untuk mendorong kesejahteraan untuk karyawan.
5. Posisi atau Role Sales Representative memiliki skala attrition yang tinggi. mengindikasikan perlunya peninjauan terhadap beban kerja dan kompensasi pada posisi ini.

### Rekomendasi Action Items (Optional)

Berikut beberapa rekomendasi untuk perusahaan Jaya Jaya Maju guna mengurangi attrition rate:

- Meningkatkan program kesejahteraan karyawan: Berdasarkan analisis, karyawan dengan pendapatan bulanan lebih rendah, job role tertentu, serta masa jabatan yang pendek cenderung lebih sering keluar. Perusahaan dapat mempertimbangkan untuk meningkatkan kesejahteraan karyawan, seperti penyesuaian gaji, kebijakan dan atau manfaat lainnya.
- Program retensi untuk karyawan baru: Karyawan yang baru bergabung dengan perusahaan cenderung memiliki risiko tinggi untuk keluar. Program orientasi dan mentoring dapat membantu meningkatkan retensi mereka.
- Menerapkan kebijakan Employee Stock Option yang lebih mudah diakses dan menguntungkan. Hal ini akan meningkatkan rasa memiliki karyawan terhadap perusahaan, mendorong loyalitas, dan menyelaraskan kepentingan karyawan dengan pemegang saham.


## Cara Menjalankan proses prediksi

Untuk melakukan prediksi pada data baru, pastikan data baru disimpan pada direktori yang sama dengan direktori proyek. terdapat dua cara untuk menjalankan prediksi:

### Melalui `script.sh` menggunakan Git Bash

1. Pastikan anda sudah menginstal [Git Bash](https://git-scm.com/downloads).
2. Buka direktori proyek tempat 'script.sh' berada.
3. Jalankan `./script.sh` menggunakan Git Bash.

### Melalui CMD atau PowerShell langsung

1. Buka Terminal CMD atau PowerShell
2. jalankan perintah ini:
    ```
    docker build -t attrition-app .
    docker run attrition-app
    ```
Hasil prediksi akan muncul di direktori yang sama (utama) dengan nama `predicted_attrition.csv`
