import os
from getpass import getpass

DB_USER = "database_user.txt"

def valid_username(username):
    return username.isalnum()

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
    return all(c.isalpha() or c.isspace() for c in nama)

def baca_database_user():
    if not os.path.exists(DB_USER):
        return []

    users = []
    with open(DB_USER, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) >= 4:
                users.append({
                    "username": data[0],
                    "password": data[1],
                    "nama": data[2],
                    "role": data[3]
                })
    return users

def simpan_user(username, password, nama, role="user"):
    with open(DB_USER, "a") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
            f.write("\n")
        f.write(f"{username}|{password}|{nama}|{role}")


def register():
    print("\n--- REGISTRASI ---")
    users = baca_database_user()

    while True:
        username = input("Username baru: ").strip()

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

    simpan_user(username, password, nama)
    print("\n[✓] Registrasi berhasil! Silakan login.")
