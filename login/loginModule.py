# loginModule.py
from pencatatan_gizi_harian.database.db_user import baca_database_user, simpan_user

def registerTenagaKesehatan():
    print("\n=== REGISTRASI TENAGA KESEHATAN ===")

    username = input("Username baru: ")
    password = input("Password: ")
    nama = input("Nama lengkap: ")
    role = "tenaga_kesehatan"

    # Cek apakah username sudah ada
    users = baca_database_user()
    for u in users:
        if u["username"] == username:
            print("\n[X] Username sudah digunakan!")
            return

    # Simpan ke txt
    simpan_user(username, password, nama, role)
    print("\n[✓] Registrasi tenaga kesehatan berhasil!")


def loginAuth(username, password):
    """Fungsi login user"""
    users = baca_database_user()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def login():
    # Login
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")
    
    user = loginAuth(username, password)
    if user:
        print(f"\n[✓] Login berhasil! Selamat datang, {user['nama']}")
        return user
    else:
        print("\n[X] Login gagal! Username atau password salah.")
        return None