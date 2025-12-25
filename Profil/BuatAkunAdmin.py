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
            print("[X] Pilihan tidak valid")

    # ===== USERNAME =====
    while True:
        username = input("Username: ").strip()

        if not valid_username(username):
            print("[X] Username harus 5–20 huruf/angka")
            continue

        if any(u["username"] == username for u in users):
            print("[X] Username sudah digunakan")
            continue

        break

    # ===== PASSWORD =====
    while True:
        password = getpass("Password: ")

        if not valid_password(password):
            print("[X] Password tidak memenuhi aturan")
            continue

        break

    # ===== NAMA =====
    while True:
        nama = input("Nama lengkap: ").strip()

        if not valid_nama(nama):
            print("[X] Nama tidak valid")
            continue

        break

    # ADMIN / NAKES TIDAK PUNYA KATEGORI, TB, BB
    simpan_user(username, password, nama, role, "-", "-", "-")

    print(f"\n[✓] Akun {role.upper()} berhasil dibuat!")
