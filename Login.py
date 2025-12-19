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

    while True:
        username = input("Username: ").strip()
        password = getpass("Password: ")

        if not username or not password:
            print("[!] Username dan password tidak boleh kosong\n")
            continue

        user = loginAuth(username, password)
        if user:
            print(f"\n[✓] Login berhasil! Selamat datang, {user['nama']}")
            return user
        else:
            print("[X] Username atau password salah\n")
