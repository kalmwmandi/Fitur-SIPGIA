import os
from getpass import getpass

DB_USER = "database_user.txt"

def valid_username(username):
    if len(username) < 5 or len(username) > 20:
        return False
    
    for i in username:
        if i >= 'A' and i <= 'Z':
            continue
        if i >= 'a' and i <= 'z':
            continue
        if i >= '0' and i <= '9':
            continue
        return False
    
    return True

def valid_password(password):
    if len(password) < 8:
        return False
    
    adaHurufBesar = False
    for i in password:
        if i >= 'A' and i <= 'Z':
            adaHurufBesar = True
            break
    
    if adaHurufBesar == False:
        return False
    
    adaHurufKecil = False
    for i in password:
        if i >= 'a' and i <= 'z':
            adaHurufKecil = True
            break
    
    if adaHurufKecil == False:
        return False
    
    adaAngka = False
    for i in password:
        if i >= '0' and i <= '9':
            adaAngka = True
            break
    
    if adaAngka == False:
        return False
    
    adaSimbol = False
    for i in password:
        if i >= 'A' and i <= 'Z':
            continue
        if i >= 'a' and i <= 'z':
            continue
        if i >= '0' and i <= '9':
            continue
        adaSimbol = True
        break
    
    if adaSimbol == False:
        return False
    
    return True

def valid_nama(nama):
    if len(nama) < 3 or len(nama) > 50:
        return False
    
    for i in nama:
        if i >= 'A' and i <= 'Z':
            continue
        if i >= 'a' and i <= 'z':
            continue
        if i == ' ':
            continue
        return False
    
    return True

def baca_database_user():
    if not os.path.exists(DB_USER):
        return []

    users = []
    with open(DB_USER, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) >= 7:
                user = {
                    "username": data[0],
                    "password": data[1],
                    "nama": data[2],
                    "role": data[3],
                    "kategori": data[4],
                    "tb": None,
                    "bb": None
                }

                if data[3] == "user":
                    if data[5] != "-" and data[6] != "-":
                        tbValid = True
                        for i in data[5]:
                            if i >= '0' and i <= '9':
                                continue
                            if i == '.':
                                continue
                            tbValid = False
                            break
                        
                        bbValid = True
                        for i in data[6]:
                            if i >= '0' and i <= '9':
                                continue
                            if i == '.':
                                continue
                            bbValid = False
                            break
                        
                        if tbValid == True and bbValid == True:
                            user["tb"] = float(data[5])
                            user["bb"] = float(data[6])

                users.append(user)
    return users

def simpan_user(username, password, nama, role, kategori, tb="-", bb="-"):
    with open(DB_USER, "a") as f:
        baris = username + "|" + password + "|" + nama + "|" + role + "|"
        baris = baris + kategori + "|" + str(tb) + "|" + str(bb) + "\n"
        f.write(baris)

def register():
    print("\n--- REGISTRASI ---")
    users = baca_database_user()

    while True:
        username = input("Username baru: ").strip()

        if username == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if not valid_username(username):
            print(">> Username hanya boleh huruf dan angka (tanpa simbol), harus terdiri dari 5-20 karakter.\n")
            continue

        usernameAda = False
        for i in users:
            if i["username"] == username:
                usernameAda = True
                break

        if usernameAda == True:
            print(">> Username sudah digunakan, silakan ulangi.\n")
            continue

        break

    while True:
        password = getpass("Password: ")

        if password == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if not valid_password(password):
            print(">> Password minimal 8 karakter, harus ada huruf besar, kecil, angka, dan simbol.\n")
            continue
        break

    while True:
        nama = input("Nama lengkap: ").strip()

        if nama == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if not valid_nama(nama):
            print(">> Nama tidak boleh mengandung angka atau simbol, harus terdiri dari 3-50 karakter.\n")
            continue
        break

    while True:
        print("\nDaftar sebagai:")
        print("1. Anak-anak")
        print("2. Ibu hamil")

        pilih = input("Pilih (1/2): ")

        if pilih == "1":
            kategori = "anak"
            break
        elif pilih == "2":
            kategori = "ibu_hamil"
            break
        else:
            print(">> Pilihan tidak valid.\n")

    while True:
        tb = input("\nTinggi badan (cm): ").strip()
        
        tbValid = True
        for i in tb:
            if i >= '0' and i <= '9':
                continue
            tbValid = False
            break
        
        if tbValid == False or len(tb) == 0:
            print(">> Tinggi badan tidak valid.")
            continue
        
        tbAngka = int(tb)
        if tbAngka < 50 or tbAngka > 250:
            print(">> Tinggi badan tidak valid.")
            continue
        
        tb = tbAngka
        break

    while True:
        bb = input("Berat badan (kg): ").strip()
        
        bbValid = True
        jumlahTitik = 0
        
        for i in bb:
            if i >= '0' and i <= '9':
                continue
            if i == '.':
                jumlahTitik = jumlahTitik + 1
                continue
            bbValid = False
            break
        
        if jumlahTitik > 1:
            bbValid = False
        
        if bbValid == False or len(bb) == 0:
            print(">> Berat badan tidak valid.")
            continue
        
        bbAngka = float(bb)
        if bbAngka <= 0 or bbAngka > 300:
            print(">> Berat badan tidak valid.")
            continue
        
        bb = bbAngka
        break

    simpan_user(username, password, nama, "user", kategori, tb, bb)
    print("\n>> Registrasi berhasil! Silakan login.")