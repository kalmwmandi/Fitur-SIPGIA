from Register import baca_database_user
from getpass import getpass

def login_auth(username, password):
    users = baca_database_user()
    
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    
    return None

def login():
    print("\n--- LOGIN ---")
    maxCoba = 3
    coba = 0

    while coba < maxCoba:
        username = input("Username: ").strip()
        password = getpass("Password: ")

        if not username or not password:
            coba += 1
            sisa = maxCoba - coba
            print(f">> Username dan password tidak boleh kosong ({sisa} percobaan tersisa).\n")
            continue

        user = login_auth(username, password)
        if user:
            print(f"\n>> Login berhasil! Selamat datang, {user['nama']}.")
            return user
        else:
            coba += 1
            sisa = maxCoba - coba
            print(f">> Username atau password salah ({sisa} percobaan tersisa).\n")

    print(">> Gagal memproses login.")
    print(">> Kembali ke Menu Utama SIPGIA.")
    return None