# Study-Kasus---6---DDP---Genap---Sistem-Manajemen-Inventaris-Barang
**Nama:** [Lithalia Geminifer Addawiyah]  
**NIM:** [2609116088 (Genap)]  
**Kelas:** [C]  
Program ini dirancang untuk mencatat dan mengelola ketersediaan stok barang pada toko kelontong berbasis bahasa pemrograman Python dan penyimpanan data berformat JSON.

---

## Deskripsi Singkat

Program ini berfungsi sebagai sistem pencatatan inventaris gudang interaktif. Seluruh data barang tersimpan secara permanen dalam file berformat JSON, sehingga data yang telah diinput tidak akan hilang ketika program dihentikan dan dijalankan kembali.

---

### Import Library
<img width="113" height="50" alt="image" src="https://github.com/user-attachments/assets/696b7499-d3ac-447d-8323-fa91e9768e20" />

Paling atas ada `import json` dan `import os`. Ini wajib soalnya programnya berinteraksi langsung sama file. Module `json` dipakai buat baca dan tulis data berformat JSON, sedangkan `os` dipakai buat ngecek apakah file-nya udah ada atau belum di komputer.

---

### Variabel path
<img width="646" height="40" alt="image" src="https://github.com/user-attachments/assets/28dae470-7d5a-490a-9336-624156208e73" />


Variabel `path` ini cuma variabel buat nyimpen lokasi (*path*) ke file `daftar barang.json` biar gampang diubah kalau mau. Tanda `r` di depannya (*raw string*) dipakai biar karakter backslash (`\`) gak dibaca sebagai *escape sequence*.
Di program ini path-nya:
`D:\TUGAS\KULIAH\Praktikum\Study Kasus 6\daftar barang.json`

---

### Fungsi muat_data_inventaris
<img width="396" height="194" alt="image" src="https://github.com/user-attachments/assets/844c9ea1-d767-42ba-9f0e-8392d7385e6e" />


Tugasnya buka file JSON terus ubah isinya jadi *list* Python yang bisa dipakai. Kalau filenya belum pernah ada atau isinya masih kosong/rusak (`JSONDecodeError`), dia bakal balikin *list* kosong `[]` aja biar gak error pas program dijalankan.

Cara kerjanya:
1. Ngecek apakah file ada dengan `os.path.exists(path)`.
2. Kalau ada, buka file lalu *parse* JSON pake `json.load(file)`.
3. Kalau file kosong/rusak (`JSONDecodeError`) atau gak ada, kembalikan *list* kosong `[]`.

---

### Fungsi simpan_ke_json(daftar_barang)
<img width="546" height="98" alt="image" src="https://github.com/user-attachments/assets/25cf8101-a255-4f96-a5bd-d54e7b65f8d1" />

Kebalikannya dari `muat_data_inventaris()`. Dia menulis ulang semua data ke dalam file berformat JSON. Nah ini bagian yang bikin data gak hilang walau programnya ditutup terus dibuka lagi.

Prosesnya:
1. Buka file dengan mode write (`"w"`).
2. Pakai `json.dump()` buat ubah *list* Python jadi format JSON terus simpan ke file.
3. `indent=4` itu biar struktur JSON-nya rapi dan mudah dibaca.

---

### Fungsi lihat_inventaris
<img width="899" height="326" alt="image" src="https://github.com/user-attachments/assets/a8a41c17-3840-4d60-ac2b-84c774677342" />


Manggil `muat_data_inventaris()` dulu buat ambil semua data barang dari file. Habis itu di-loop pake `enumerate()` biar tiap barang keprint satu-satu dengan nomor urut, jumlah stok, dan format harga.

Cara kerjanya:
1. Ambil data dari `muat_data_inventaris()`.
2. Kalau belum ada barang (*list* kosong), dia bakal bilang `[!] Belum ada data barang di gudang.`.
3. Kalau ada isinya, tampilkan header lalu lakukan perulangan `for index, item in enumerate(stok_gudang, start=1)` buat nyetak tiap barang.

---

### Fungsi tambah_barang_baru
<img width="753" height="414" alt="image" src="https://github.com/user-attachments/assets/6f3e0f64-d1bd-44aa-9e76-cf1b562b1fb7" />


Bertugas menerima input barang baru dari user, terus dimasukin ke dalam file JSON secara permanen.

Prosesnya:
1. Ambil data lama dulu dari file pakai `muat_data_inventaris()`.
2. Minta input nama barang, stok, dan harga (stok dan harga langsung diubah ke `int`).
3. Buat dictionary `item_baru` yang isinya `nama`, `stok`, dan `harga`.
4. Tambahkan dictionary tersebut ke *list* lama pakai `.append()`.
5. Panggil `simpan_ke_json()` buat menyimpan *list* yang udah diperbarui ke file JSON.

---

### Menu Utama (while True)
<img width="768" height="381" alt="image" src="https://github.com/user-attachments/assets/7466be48-db18-4c22-b354-99f4d2ea098c" />


Menjalankan program secara terus-menerus menggunakan `while True` supaya menu interaktif muncul terus sampai user memilih menu keluar.

Cara kerjanya:
1. Tampilkan opsi menu (1. Lihat Data Barang, 2. Tambah Barang Baru, 3. Keluar).
2. Minta input pilihan dari user.
3. Pakai percabangan `if-elif-else` buat menjalankan fungsi sesuai pilihan.
4. Kalau user pilih `"3"`, program bakal ngasih pesan penutup lalu berhenti lewat `break`.

### Penjelasan Hasil Run Program
<img width="1167" height="873" alt="image" src="https://github.com/user-attachments/assets/8ecd3b8d-0073-4376-8feb-efdc9c13a4b6" />

1. (Cek Awal): Program ngecek file, karena masih kosong muncul pesan barang belum ada.
2. (Tambah Barang): Input nama "Kipas", stok 1, dan harga 225000, lalu otomatis tersimpan ke file JSON.
3. (Cek Ulang): Data "Kipas" langsung tampil rapi lengkap dengan format harga Rp 225,000.
4. (Keluar): Program selesai dan berhenti dengan aman.

### Penjelasan Isi File JSON (daftar barang.json)
<img width="331" height="192" alt="image" src="https://github.com/user-attachments/assets/d7bfe718-0146-4cf6-950d-8370a709a7a3" />

1. Format Data: Data disimpan dalam bentuk list [] yang berisi dictionary {}.
2. Atribut Barang: Setiap barang menyimpan 3 kunci utama, yaitu "nama", "stok", dan "harga".   
3. Bukti Penyimpanan: Terbukti data "Kipas" berhasil masuk dan tersimpan secara permanen di file JSON. 

