from tabulate import tabulate

# Dummy Data Gudang
# Struktur data = kode: [nama, jenis, jumlah, satuan, supplier, kategori]
gudang = {
    "G001": ["Kertas A4", "Alat Tulis", 250, "rim", "Toko Sinar Abadi", "ATK"],
    "G002": ["Pulpen Hitam", "Alat Tulis", 100, "pcs", "Toko Pena Jaya", "ATK"],
    "G003": ["Stapler", "Peralatan Kantor", 35, "unit", "PT OfficeMart", "Peralatan"],
    "G004": ["Amplop Coklat", "Alat Tulis", 500, "pcs", "Toko Kertas Utama", "ATK"],
    "G005": ["Kabel LAN", "Elektronik", 60, "meter", "Toko Jaringan Mandiri", "IT Support"],
    "G006": ["Tinta Printer", "Cairan", 20, "botol", "CV PrintMax", "Perlengkapan"],
    "G007": ["Mouse Wireless", "Elektronik", 25, "unit", "PT Techno", "IT Support"],
    "G008": ["Notebook", "Alat Tulis", 150, "buku", "Toko Sinar Abadi", "ATK"],
    "G009": ["Penghapus", "Alat Tulis", 200, "pcs", "Toko Pena Jaya", "ATK"],
    "G010": ["CD Blank", "Media Penyimpanan", 75, "pcs", "PT Digital Store", "Arsip"]
}

riwayat_transaksi = []

# === INPUT & KONFIRMASI ===
def input_kode(prompt):
    while True:
        kode = input(prompt).upper()
        if not kode.isalnum():
            print("Kode hanya boleh huruf dan angka.")
        elif len(kode) < 4:
            print("Kode minimal 4 karakter.")
        else:
            return kode

def input_teks(prompt):
    while True:
        teks = input(prompt)
        if teks:
            return teks
        print("Input tidak boleh kosong.")

def input_angka(prompt):
    while True:
        try:
            angka = int(input(prompt))
            if angka < 0:
                print("Angka harus bilangan bulat positif.")
            else:
                return angka
        except ValueError:
            print("Input harus angka.")

def konfirmasi(prompt):
    while True:
        jawab = input(prompt + " (y/n): ").lower()
        if jawab in ['y', 'n']:
            return jawab == 'y'
        print("Masukkan hanya 'y' (yes) atau 'n' (no).")

# === READ MENU ===
def tampilkan_barang():
    if not gudang:
        print("Gudang kosong.")
        return
    headers = ["Kode", "Nama", "Jenis", "Jumlah", "Satuan", "Supplier", "Kategori"]
    rows = [[kode, *data] for kode, data in gudang.items()]
    print("\nDaftar Barang:")
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def cari_barang():
    keyword = input_teks("Masukkan kata kunci pencarian: ").lower()
    hasil = [
        [kode, *data]
        for kode, data in gudang.items()
        if keyword in kode.lower()      # kode barang
        or keyword in data[0].lower()   # nama barang
        or keyword in data[1].lower()   # jenis barang
        or keyword in data[4].lower()   # supplier
        or keyword in data[5].lower()   # kategori
    ]
    if hasil:
        headers = ["Kode", "Nama", "Jenis", "Jumlah", "Satuan", "Supplier", "Kategori"]
        print("\nHasil Pencarian:")
        print(tabulate(hasil, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Tidak ditemukan.")

def tampilkan_riwayat():
    if not riwayat_transaksi:
        print("Belum ada riwayat transaksi.")
    else:
        headers = ["Jenis", "Kode", "Nama", "Jenis Barang", "Jumlah", "Satuan", "Petugas"]
        print("\nRiwayat Transaksi Barang:")
        print(tabulate(riwayat_transaksi, headers=headers, tablefmt="fancy_grid"))

# === CREATE MENU ===
def tambah_barang():
    kode = input_kode("Masukkan kode barang: ")
    if kode in gudang:
        print("Kode sudah digunakan.")
        return
    nama = input_teks("Masukkan nama barang: ")
    jenis = input_teks("Masukkan jenis barang: ")
    jumlah = input_angka("Masukkan jumlah stok: ")
    satuan = input_teks("Masukkan satuan: ")
    supplier = input_teks("Masukkan nama supplier: ")
    kategori = input_teks("Masukkan kategori: ")

    print(f"\nData yang akan ditambahkan:\nKode: {kode}, Nama: {nama}, Jenis: {jenis}, Jumlah: {jumlah}, Satuan: {satuan}, Supplier: {supplier}, Kategori: {kategori}")
    if konfirmasi("Apakah Anda yakin ingin menambahkan data ini?"):
        gudang[kode] = [nama, jenis, jumlah, satuan, supplier, kategori]
        print("Barang berhasil ditambahkan.")
    else:
        print("Penambahan dibatalkan.")

# === UPDATE MENU ===
def ubah_barang():
    tampilkan_barang()
    kode = input_kode("Masukkan kode barang yang ingin diubah: ")
    if kode not in gudang:
        print("Barang tidak ditemukan.")
        return
    bagian = input_teks("Bagian yang ingin diubah (kode/nama/jenis/stok/satuan/supplier/kategori/semua): ").lower()

    if bagian == 'kode':
        kode_baru = input_kode("Kode baru: ")
        if kode_baru in gudang:
            print("Kode baru sudah ada.")
            return
        if konfirmasi(f"Anda akan mengubah kode barang {kode} menjadi {kode_baru}. Apakah Anda yakin ingin melanjutkan?"):
            gudang[kode_baru] = gudang[kode]
            del gudang[kode]
            print("Kode barang diperbarui.")
    elif bagian in ['nama', 'jenis', 'satuan', 'supplier', 'kategori']:
        index = {'nama':0, 'jenis':1, 'satuan':3, 'supplier':4, 'kategori':5}[bagian]
        data_baru = input_teks(f"Masukkan {bagian} baru: ")
        if konfirmasi(f"Anda akan mengubah data {bagian} {gudang[kode][index]} menjadi {data_baru}. Apakah Anda yakin ingin melanjutkan?"):
            gudang[kode][index] = data_baru
            print(f"{bagian.capitalize()} diperbarui.")
    elif bagian == 'stok':
        data_baru = input_angka("Jumlah stok baru: ")
        if konfirmasi(f"Anda akan memperbarui jumlah stok {gudang[kode][2]} menjadi {data_baru}. Apakah Anda yakin ingin melanjutkan?"):
            gudang[kode][2] = data_baru
            print("Stok diperbarui.")
    elif bagian == 'semua':
        nama = input_teks("Nama baru: ")
        jenis = input_teks("Jenis baru: ")
        jumlah = input_angka("Jumlah baru: ")
        satuan = input_teks("Satuan baru: ")
        supplier = input_teks("Supplier baru: ")
        kategori = input_teks("Kategori baru: ")
        if konfirmasi("Semua data akan diperbarui. Apakah Anda yakin ingin melanjutkan?"):
            gudang[kode] = [nama, jenis, jumlah, satuan, supplier, kategori]
            print("Semua data diperbarui.")
    else:
        print("Bagian tidak dikenali.")

def barang_masuk():
    tampilkan_barang()
    kode = input_kode("Kode barang yang akan ditambahkan stok: ")
    if kode in gudang:
        jumlah = input_angka(f"Jumlah {gudang[kode][0]} masuk: ")
        petugas = input_teks("Nama petugas (tidak boleh kosong): ")
        if konfirmasi(f"Data barang {kode} - {gudang[kode][0]} {jumlah} {gudang[kode][3]} akan dicatat, Apakah Anda yakin ingin mencatat barang masuk ini?"):
            gudang[kode][2] += jumlah
            riwayat_transaksi.append(["Masuk", kode, gudang[kode][0], gudang[kode][1], jumlah, gudang[kode][3], petugas])
            print("Barang masuk dicatat.")
        else:
            print("Transaksi dibatalkan.")
    else:
        print("Kode tidak ditemukan.")

def barang_keluar():
    tampilkan_barang()
    kode = input_kode("Kode barang yang akan dikurangi stoknya: ")
    if kode in gudang:
        jumlah = input_angka(f"Jumlah {gudang[kode][0]} keluar: ")
        petugas = input_teks("Nama petugas (tidak boleh kosong): ")
        if jumlah > gudang[kode][2]:
            print("Stok tidak mencukupi.")
            return
        if konfirmasi(f"Data barang {kode} - {gudang[kode][0]} {jumlah} {gudang[kode][3]} akan dicatat, Apakah Anda yakin ingin mencatat barang keluar ini?"):
            gudang[kode][2] -= jumlah
            riwayat_transaksi.append(["Keluar", kode, gudang[kode][0], gudang[kode][1], jumlah, gudang[kode][3], petugas])
            print("Barang keluar dicatat.")
        else:
            print("Transaksi dibatalkan.")
    else:
        print("Kode tidak ditemukan.")

# === DELETE MENU ===
def hapus_barang():
    tampilkan_barang()
    kode = input_kode("Masukkan kode barang yang ingin dihapus: ")
    if kode in gudang:
        if konfirmasi(f"Data barang {kode} - {gudang[kode][0]} akan dihapus. Apakah Anda yakin ingin melanjutkan?"):
            del gudang[kode]
            print("Barang dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Barang tidak ditemukan.")

# === MAIN MENU ===
def menu():
    while True:
        print("\n=== WAREHOUSE MANAGEMENT SYSTEM ===")
        print("1. Tampilkan Barang")        # Read
        print("2. Tambah Barang")           # Create
        print("3. Ubah Barang")             # Update
        print("4. Hapus Barang")            # Delete
        print("5. Barang Masuk")            # Update
        print("6. Barang Keluar")           # Update
        print("7. Lihat Riwayat Transaksi") # Read
        print("8. Cari Barang")             # Read
        print("9. Keluar")                  # Exit
        pilihan = input("Pilih menu (1–9): ")

        if pilihan == '1':
            tampilkan_barang()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            ubah_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            barang_masuk()
        elif pilihan == '6':
            barang_keluar()
        elif pilihan == '7':
            tampilkan_riwayat()
        elif pilihan == '8':
            cari_barang()
        elif pilihan == '9':
            if konfirmasi("Apakah Anda yakin ingin keluar dari program?"):
                print("Program selesai.")
                break
        else:
            print("Pilihan tidak valid. Masukkan angka 1–9.")

menu()