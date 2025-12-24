# login.py
from Register import baca_database_user
from getpass import getpass

def loginAuth(username, password):
    users = baca_database_user()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None


def login():
    print("\n--- LOGIN ---")
    MAX_ATTEMPT = 3
    attempt = 0

    while attempt < MAX_ATTEMPT:
        username = input("Username: ").strip()
        password = getpass("Password: ")

        if not username or not password:
            print("[!] Username dan password tidak boleh kosong\n")
            attempt += 1
            continue

        user = loginAuth(username, password)
        if user:
            print(f"\n[✓] Login berhasil! Selamat datang, {user['nama']}")
            return user
        else:
            attempt += 1
            sisa = MAX_ATTEMPT - attempt
            print(f"[X] Username atau password salah ({sisa} percobaan tersisa)\n")

    # kalau sudah 3x salah
    print("[!] Gagal memproses login.")
    print("[!] Kembali ke Menu Utama SIPGIA.")
    return None
