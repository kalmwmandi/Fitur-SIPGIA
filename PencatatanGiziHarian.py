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



# Jalankan program
if __name__ == "__main__":
    main()
