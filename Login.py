# login.py
from Register import baca_database_user

def loginAuth(username, password):
    users = baca_database_user()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None


def login():
    print("\n--- LOGIN ---")

    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # VALIDASI INPUT KOSONG
        if not username or not password:
            print("\n[!] Username dan password tidak boleh kosong.")
            print("[!] Silakan isi ulang.\n")
            continue

        user = loginAuth(username, password)
        if user:
            print(f"\n[✓] Login berhasil! Selamat datang, {user['nama']}")
            return user
        else:
            print("\n[X] Username atau password salah.\n")
