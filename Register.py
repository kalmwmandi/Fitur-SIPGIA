# register.py
import os, re
from getpass import getpass

DB_USER = "database_user.txt"

def valid_username(username):
    if not username.isalnum():
        return False
    if len(username) < 5 or len(username) > 20:
        return False
    return True

def valid_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if password.isalnum():
        return False
    return True

def valid_nama(nama):
    if len(nama) < 3 or len(nama) > 50:
        return False
    return all(c.isalpha() or c.isspace() for c in nama)

def baca_database_user():
    if not os.path.exists(DB_USER):
        return []

    users = []
    with open(DB_USER, "r") as f:
        for line in f:
            data = line.strip().split("|")
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
                    try:
                        user["tb"] = float(data[5])
                        user["bb"] = float(data[6])
                    except:
                        user["tb"] = None
                        user["bb"] = None

                users.append(user)
    return users

def simpan_user(username, password, nama, role, kategori, tb="-", bb="-"):
    with open(DB_USER, "a") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
            f.write("\n")
        f.write(f"{username}|{password}|{nama}|{role}|{kategori}|{tb}|{bb}\n")


def register():
    print("\n--- REGISTRASI ---")
    users = baca_database_user()

    while True:
        username = input("Username baru: ").strip()

        if username == "":
            print("[X] Username tidak boleh kosong\n")
            continue

        if not valid_username(username):
            print("[X] Username hanya boleh huruf dan angka (tanpa simbol)\n")
            continue

        if any(u["username"] == username for u in users):
            print("[X] Username sudah digunakan, silakan ulangi\n")
            continue

        break

    while True:
        password = getpass("Password: ")

        if not valid_password(password):
            print("[X] Password minimal 8 karakter, harus ada huruf besar, kecil, angka, dan simbol\n")
            continue
        break

    while True:
        nama = input("Nama lengkap: ").strip()

        if not valid_nama(nama):
            print("[X] Nama tidak boleh mengandung angka atau simbol\n")
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
            print("[X] Pilihan tidak valid\n")

    while True:
        tb = input("Tinggi badan (cm): ").strip()
        if not tb.isdigit() or int(tb) < 50 or int(tb) > 250:
            print("[X] Tinggi badan tidak valid")
            continue
        tb = int(tb)
        break

    while True:
        bb = input("Berat badan (kg): ").strip()
        try:
            bb = float(bb)
            if bb <= 0 or bb > 300:
                raise ValueError
            break
        except ValueError:
            print("[X] Berat badan tidak valid")

    simpan_user(username, password, nama, "user", kategori, tb, bb)
    print("\n[✓] Registrasi berhasil! Silakan login.")

def normalisasi_nama(nama):
    # hapus spasi depan-belakang + jadikan 1 spasi
    nama = re.sub(r"\s+", " ", nama.strip())
    return nama