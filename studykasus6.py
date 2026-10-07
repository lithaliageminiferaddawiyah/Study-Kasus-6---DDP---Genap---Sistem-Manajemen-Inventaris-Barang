import json
import os

path = r"D:\TUGAS\KULIAH\Praktikum\Study Kasus 6\daftar barang.json"

def muat_data_inventaris():
    if os.path.exists(path):
        try:
            with open(path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def simpan_ke_json(daftar_barang):
    """Fungsi untuk menyimpan seluruh data ke file JSON"""
    with open(path, "w") as file:
        json.dump(daftar_barang, file, indent=4)

def lihat_inventaris():
    """Instruksi 3: Fitur membaca dan menampilkan data barang"""
    stok_gudang = muat_data_inventaris()

    if not stok_gudang:
        print("\n[!] Belum ada data barang di gudang.\n")
        return

    print("\n" + "=" * 40)
    print("========DAFTAR INVENTARIS BARANG========")
    print("=" * 40)
    for index, item in enumerate(stok_gudang, start=1):
        print(f"{index}. {item['nama']} | Stok: {item['stok']} | Harga: Rp {item['harga']:,}")
    print("=" * 40 + "\n")

def tambah_barang_baru():
    """Instruksi 4 & 5: Fitur menambah data baru dan menyimpan/append ke file"""
    daftar_lama = muat_data_inventaris()

    print("\n--- FORM TAMBAH BARANG ---")
    nama_barang = input("Nama barang  : ")
    stok_barang = int(input("Jumlah stok  : "))
    harga_barang = int(input("Harga satuan : "))

    item_baru = {
        "nama": nama_barang,
        "stok": stok_barang,
        "harga": harga_barang
    }

    daftar_lama.append(item_baru)
    simpan_ke_json(daftar_lama)
    print(">> Barang berhasil ditambahkan dan disimpan!\n")

while True:
    print("=== SISTEM INVENTARIS TOKO KELONTONG ===")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang Baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        lihat_inventaris()
    elif pilihan == "2":
        tambah_barang_baru()
    elif pilihan == "3":
        print("\nTerima kasih, program selesai digunakan!")
        break
    else:
        print("\n[!] Pilihan tidak valid, silakan masukkan nomor 1, 2, atau 3.\n")