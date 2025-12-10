# sipgia_pencatatan_gizi.py
# Fitur Pencatatan Gizi Harian - SIPGIA
# Menggunakan operasi file dan module sederhana

import os

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

def login(username, password):
    """Fungsi login user"""
    users = baca_database_user()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

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

# Jalankan program
if __name__ == "__main__":
    main()
