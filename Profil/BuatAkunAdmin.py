from getpass import getpass
from Register import (
    valid_username,
    valid_password,
    valid_nama,
    baca_database_user,
    simpan_user
)

def buat_akun_admin():
    users = baca_database_user()

    while True:
        print("\n--- BUAT AKUN ---")
        print("1. Admin")
        print("2. Tenaga Kesehatan")
        print("3. Kembali")

        pilih = input("Pilih jenis akun: ")

        if pilih == "1":
            role = "admin"
            break
        elif pilih == "2":
            role = "tenaga_kesehatan"
            break
        elif pilih == "3":
            return
        else:
            print(">> Pilihan tidak valid.")

    while True:
        username = input("Username: ").strip()

        if username == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if valid_username(username) == False:
            print(">> Username hanya boleh huruf dan angka (tanpa simbol), harus terdiri dari 5-20 karakter.\n")
            continue

        userSudahAda = False
        for u in users:
            if u["username"] == username:
                userSudahAda = True
                break
        
        if userSudahAda == True:
            print(">> Username sudah digunakan, silakan ulangi.\n")
            continue

        break

    while True:
        password = getpass("Password: ")

        if password == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if valid_password(password) == False:
            print(">> Password minimal 8 karakter, harus ada huruf besar, kecil, angka, dan simbol.\n")
            continue

        break

    while True:
        nama = input("Nama lengkap: ").strip()

        if nama == "":
            print(">> Username, password, atau nama lengkap tidak boleh kosong.\n")
            continue

        if valid_nama(nama) == False:
            print(">> Nama tidak boleh mengandung angka atau simbol, harus terdiri dari 3-50 karakter.\n")
            continue

        break

    simpan_user(username, password, nama, role, "-", "-", "-")

    print(f"\n>> Akun {role.upper()} berhasil dibuat!.")