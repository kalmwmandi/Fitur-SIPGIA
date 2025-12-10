# sipgia_pencatatan_gizi.py
# Fitur Pencatatan Gizi Harian - SIPGIA
# Menggunakan operasi file dan module sederhana

import os
import loginModule as lgn

# ============== FUNGSI DATABASE (FILE TXT) ==============

def baca_database_user(filename="database_user.txt"):
    """Membaca database user dari file txt"""
    users = []
    if os.path.exists(filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            data = line.strip().split("|")
            if len(data) >= 4:
                user = {
                    "username": data[0],
                    "password": data[1],
                    "nama": data[2],
                    "role": data[3]  # "user" atau "tenaga_kesehatan"
                }
                users.append(user)
    return users

def simpan_user(username, password, nama, role, filename="database_user.txt"):
    """Menyimpan user baru ke database"""
    file = open(filename, "a")
    file.write(f"{username}|{password}|{nama}|{role}\n")
    file.close()

def baca_catatan_gizi(filename="database_catatan_gizi.txt"):
    """Membaca semua catatan gizi dari file txt"""
    catatan = []
    if os.path.exists(filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            data = line.strip().split("|")
            if len(data) >= 7:
                item = {
                    "id": data[0],
                    "username": data[1],
                    "tanggal": data[2],
                    "makanan": data[3],
                    "kalori": data[4],
                    "protein": data[5],
                    "karbohidrat": data[6]
                }
                catatan.append(item)
    return catatan

def simpan_catatan_gizi(username, tanggal, makanan, kalori, protein, karbohidrat, filename="database_catatan_gizi.txt"):
    """Menyimpan catatan gizi baru ke database"""
    # Generate ID sederhana
    catatan = baca_catatan_gizi(filename)
    new_id = len(catatan) + 1
    
    file = open(filename, "a")
    file.write(f"{new_id}|{username}|{tanggal}|{makanan}|{kalori}|{protein}|{karbohidrat}\n")
    file.close()
    return True

def get_catatan_by_user(username, filename="database_catatan_gizi.txt"):
    """Mengambil catatan gizi berdasarkan username"""
    semua_catatan = baca_catatan_gizi(filename)
    catatan_user = []
    for c in semua_catatan:
        if c["username"] == username:
            catatan_user.append(c)
    return catatan_user

# ============== FUNGSI AUTENTIKASI ==============


def registrasi(username, password, nama, role="user"):
    """Fungsi registrasi user baru"""
    users = baca_database_user()
    for user in users:
        if user["username"] == username:
            return False  # Username sudah ada
    simpan_user(username, password, nama, role)
    return True

# ============== FUNGSI VALIDASI ==============

def validasi_data_gizi(tanggal, makanan, kalori, protein, karbohidrat):
    """Validasi kelengkapan inputan data gizi"""
    if tanggal == "" or makanan == "" or kalori == "" or protein == "" or karbohidrat == "":
        return False
    # Validasi angka
    try:
        float(kalori)
        float(protein)
        float(karbohidrat)
    except:
        return False
    return True

# ============== FUNGSI HITUNG GIZI ==============

def hitung_total_gizi_harian(catatan_list):
    """Menghitung total gizi dari list catatan"""
    total_kalori = 0
    total_protein = 0
    total_karbohidrat = 0
    
    for c in catatan_list:
        total_kalori += float(c["kalori"])
        total_protein += float(c["protein"])
        total_karbohidrat += float(c["karbohidrat"])
    
    return {
        "total_kalori": total_kalori,
        "total_protein": total_protein,
        "total_karbohidrat": total_karbohidrat
    }

# ============== FUNGSI TAMPILAN CLI ==============

def tampilkan_header():
    """Menampilkan header aplikasi"""
    print("\n" + "="*50)
    print("          SIPGIA - Sistem Informasi Gizi")
    print("           Pencatatan Gizi Harian")
    print("="*50)

def menu_utama():
    """Menampilkan menu utama"""
    print("\n--- MENU UTAMA ---")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

def menu_user(nama_user):
    """Menampilkan menu untuk user biasa"""
    print(f"\n--- DASHBOARD USER: {nama_user} ---")
    print("1. Pencatatan Gizi Harian")
    print("2. Lihat Riwayat Catatan Gizi")
    print("3. Lihat Total Gizi Hari Ini")
    print("4. Logout")
    pilihan = input("Pilih menu (1-4): ")
    return pilihan

def form_input_gizi():
    """Form untuk input data gizi harian"""
    print("\n--- FORM PENCATATAN GIZI HARIAN ---")
    tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
    makanan = input("Nama makanan: ")
    kalori = input("Jumlah kalori (kkal): ")
    protein = input("Jumlah protein (gram): ")
    karbohidrat = input("Jumlah karbohidrat (gram): ")
    
    return tanggal, makanan, kalori, protein, karbohidrat

def tampilkan_catatan(catatan_list):
    """Menampilkan daftar catatan gizi"""
    if len(catatan_list) == 0:
        print("\n[!] Belum ada catatan gizi.")
        return
    
    print("\n--- RIWAYAT CATATAN GIZI ---")
    print("-"*70)
    print(f"{'ID':<5}{'Tanggal':<15}{'Makanan':<20}{'Kalori':<10}{'Protein':<10}{'Karbo':<10}")
    print("-"*70)
    
    for c in catatan_list:
        print(f"{c['id']:<5}{c['tanggal']:<15}{c['makanan']:<20}{c['kalori']:<10}{c['protein']:<10}{c['karbohidrat']:<10}")
    
    print("-"*70)

# ============== PROGRAM UTAMA ==============

def main():
    """Fungsi utama program"""
    user_aktif = None
    
    while True:
        tampilkan_header()
        
        if user_aktif is None:
            # Belum login
            pilihan = menu_utama()
            
            if pilihan == "1":
                # Login
                user_aktif = lgn.login()
                if user_aktif:
                    pass
                    
            elif pilihan == "2":
                # Registrasi
                print("\n--- REGISTRASI ---")
                username = input("Username baru: ")
                password = input("Password: ")
                nama = input("Nama lengkap: ")
                
                if registrasi(username, password, nama):
                    print("\n[✓] Registrasi berhasil! Silakan login.")
                else:
                    print("\n[X] Registrasi gagal! Username sudah digunakan.")
                    
            elif pilihan == "3":
                print("\n[!] Terima kasih telah menggunakan SIPGIA. Sampai jumpa!")
                break
            else:
                print("\n[X] Pilihan tidak valid!")
        
        else:
            # Sudah login - tampilkan menu user
            pilihan = menu_user(user_aktif["nama"])
            
            if pilihan == "1":
                # Pencatatan Gizi Harian
                tanggal, makanan, kalori, protein, karbohidrat = form_input_gizi()
                
                # Validasi kelengkapan data
                if validasi_data_gizi(tanggal, makanan, kalori, protein, karbohidrat):
                    # Simpan ke database
                    if simpan_catatan_gizi(user_aktif["username"], tanggal, makanan, kalori, protein, karbohidrat):
                        print("\n[✓] Notifikasi: Anda berhasil menambah data gizi!")
                    else:
                        print("\n[X] Gagal menyimpan data.")
                else:
                    print("\n[X] Data tidak lengkap atau format angka salah. Silakan coba lagi.")
                    
            elif pilihan == "2":
                # Lihat Riwayat Catatan
                catatan_user = get_catatan_by_user(user_aktif["username"])
                tampilkan_catatan(catatan_user)
                
            elif pilihan == "3":
                # Lihat Total Gizi Hari Ini
                tanggal_hari_ini = input("Masukkan tanggal yang ingin dilihat (DD-MM-YYYY): ")
                catatan_user = get_catatan_by_user(user_aktif["username"])
                
                # Filter berdasarkan tanggal
                catatan_hari_ini = []
                for c in catatan_user:
                    if c["tanggal"] == tanggal_hari_ini:
                        catatan_hari_ini.append(c)
                
                if len(catatan_hari_ini) > 0:
                    total = hitung_total_gizi_harian(catatan_hari_ini)
                    print(f"\n--- TOTAL GIZI TANGGAL {tanggal_hari_ini} ---")
                    print(f"Total Kalori    : {total['total_kalori']} kkal")
                    print(f"Total Protein   : {total['total_protein']} gram")
                    print(f"Total Karbohidrat: {total['total_karbohidrat']} gram")
                else:
                    print(f"\n[!] Tidak ada catatan untuk tanggal {tanggal_hari_ini}")
                    
            elif pilihan == "4":
                # Logout
                print(f"\n[!] Logout berhasil. Sampai jumpa, {user_aktif['nama']}!")
                user_aktif = None
            else:
                print("\n[X] Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")

# Jalankan program
if __name__ == "__main__":
    main()
