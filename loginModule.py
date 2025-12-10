import PencatatanGiziHarian as pgh

def loginAuth(username, password):
    """Fungsi login user"""
    users = pgh.baca_database_user()
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