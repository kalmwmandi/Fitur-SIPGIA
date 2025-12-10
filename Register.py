import os

DB_USER = "database_user.txt"

def baca_database_user():
    if not os.path.exists(DB_USER):
        return []

    users = []
    with open(DB_USER, "r") as f:
        for line in f.readlines():
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
        f.write(f"{username}|{password}|{nama}|{role}\n")


def register():
    print("\n--- REGISTRASI ---")
    username = input("Username baru: ")
    password = input("Password: ")
    nama = input("Nama lengkap: ")

    users = baca_database_user()
    for u in users:
        if u["username"] == username:
            print("\n[X] Username sudah digunakan.")
            return False

    simpan_user(username, password, nama)
    print("\n[✓] Registrasi berhasil! Silakan login.")
    return True
