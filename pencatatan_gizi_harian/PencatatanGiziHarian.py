# PencatatanGiziharian.py
# HAPUS baris ini:
# from login.loginModule import login

from pencatatan_gizi_harian.database.db_user import baca_database_user, simpan_user
from pencatatan_gizi_harian.database.db_catatan import (
    simpan_catatan_gizi, get_catatan_by_user
)
from pencatatan_gizi_harian.utils.validasi import validasi_data_gizi
from pencatatan_gizi_harian.utils.hitung_gizi import hitung_total_gizi_harian
from pencatatan_gizi_harian.ui.header import tampilkan_header
from pencatatan_gizi_harian.ui.menu import menu_user
from pencatatan_gizi_harian.ui.form import form_input_gizi, tampilkan_catatan



def registrasi(username, password, nama):
    users = baca_database_user()
    for u in users:
        if u["username"] == username:
            return False
    simpan_user(username, password, nama, "user")
    return True


def menu_pencatatan(user):
    """Dipanggil dari main.py"""
    user_aktif = user

    while True:
        tampilkan_header()
        pilihan = menu_user(user_aktif["nama"])

        if pilihan == "1":
            tanggal, makanan, kalori, protein, karbo = form_input_gizi()

            if validasi_data_gizi(tanggal, makanan, kalori, protein, karbo):
                simpan_catatan_gizi(user_aktif["username"], tanggal, makanan, kalori, protein, karbo)
                print("\n[✓] Catatan berhasil ditambahkan!")
            else:
                print("\n[X] Data tidak valid!")

        elif pilihan == "2":
            data = get_catatan_by_user(user_aktif["username"])
            tampilkan_catatan(data)

        elif pilihan == "3":
            tanggal = input("Masukkan tanggal yang ingin dilihat (DD-MM-YYYY): ")
            data = get_catatan_by_user(user_aktif["username"])
            hari_ini = [c for c in data if c["tanggal"] == tanggal]

            if hari_ini:
                total = hitung_total_gizi_harian(hari_ini)
                print(f"\n--- TOTAL GIZI {tanggal} ---")
                print(f"Kalori     : {total['total_kalori']} kkal")
                print(f"Protein    : {total['total_protein']} g")
                print(f"Karbohidrat: {total['total_karbohidrat']} g")
            else:
                print("\n[!] Tidak ada catatan.")

        elif pilihan == "4":
            print("\nLogout berhasil.")
            break

        input("\nTekan Enter untuk melanjutkan...")
