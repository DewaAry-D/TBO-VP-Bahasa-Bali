# BaliSyntax – Balinese Sentence Parser (CYK Algorithm)

**BaliSyntax** adalah aplikasi parser kalimat Bahasa Bali yang menggunakan algoritma **CYK (Cocke-Younger-Kasami)**. Aplikasi ini dirancang untuk menganalisis struktur sintaksis kalimat Bahasa Bali, menentukan validitasnya berdasarkan tata bahasa (Grammar) yang telah didefinisikan, dan memvisualisasikan struktur pohon (parse tree) kalimat tersebut.

## 📂 Struktur Proyek

* **`main.py`**: Aplikasi utama berbasis GUI (Tkinter). Digunakan untuk input kalimat, pengecekan validitas, dan penggambaran pohon sintaksis secara visual.
* **`evaluasi.py`**: Skript untuk melakukan pengujian batch (banyak kalimat sekaligus) untuk menghitung akurasi parser terhadap pola kalimat yang diharapkan.
* **`rule.py`**: Berisi definisi *Context-Free Grammar* (CFG) dalam bentuk *Chomsky Normal Form* (CNF) dan Lexicon (kamus kata) Bahasa Bali.
* **`kalimat.py`** *(Diperlukan untuk evaluasi)*: File ini harus berisi list `daftar_kalimat` yang akan diuji oleh `evaluasi.py`.

## 🚀 Fitur Utama

1.  **Analisis Kalimat Tunggal (GUI)**:
    * Mengecek apakah kalimat valid (Diterima) atau invalid (Ditolak).
    * Mendeteksi pola kalimat (Contoh: S - P - O, P - S - Ket).
2.  **Visualisasi Parse Tree**:
    * Menggambar pohon sintaksis secara dinamis menggunakan Canvas.
    * Fitur *drag/pan* untuk menggeser tampilan pohon jika terlalu lebar.
3.  **Evaluasi Akurasi**:
    * Menghitung persentase akurasi parser terhadap dataset uji.
    * Menampilkan tabel perbandingan antara pola target dan pola yang terdeteksi.

## 🛠️ Instalasi

Pastikan Anda telah menginstal **Python 3.x**.

1.  **Clone atau Unduh repositori ini.**
2.  **Instal dependensi:**
    Aplikasi GUI menggunakan `tkinter` (biasanya sudah terinstal bersama Python). Untuk menjalankan skrip evaluasi, Anda perlu menginstal `pandas`.

    ```bash
    pip install -r requirements.txt
    ```

    *Catatan untuk pengguna Linux:* Jika `tkinter` belum ada, instal via terminal: `sudo apt-get install python3-tk`.

## 💻 Cara Penggunaan

### 1. Menjalankan Aplikasi GUI (`main.py`)
Gunakan ini untuk mencoba memasukkan kalimat satu per satu dan melihat struktur pohonnya.

```bash
python main.py
