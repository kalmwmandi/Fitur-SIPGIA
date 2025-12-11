def menu_utama():
    print("\n--- MENU UTAMA ---")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    return input("Pilih menu: ")


def menu_user(nama_user):
    print(f"\n--- DASHBOARD USER: {nama_user} ---")
    print("1. Pencatatan Gizi Harian")
    print("2. Lihat Riwayat Catatan Gizi")
    print("3. Lihat Total Gizi Hari Ini")
    print("4. Logout")
    return input("Pilih menu: ")
