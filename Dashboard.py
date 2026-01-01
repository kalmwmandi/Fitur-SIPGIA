from Gizi.PencatatanGizi import input_gizi
from Gizi.RiwayatPemantauanGizi import riwayat_hasil_pemantauan
from Profil.ManajemenProfil import manajemen_profil
from Gizi.PemantauanGizi import pemantauan_gizi_nakes
from Profil.BuatAkunAdmin import buat_akun_admin


def dashboard(user):
    role = user["role"]

    while True:
        if role == "user":
            if user["kategori"] == "ibu_hamil":
                judul = "IBU HAMIL"
            else:
                judul = "ANAK"
            print(f"\n--- DASHBOARD {judul} : {user['nama']} ---")
        else:
            print(f"\n--- DASHBOARD {role.upper()} : {user['nama']} ---")

        if role == "user":
            print("1. Pencatatan Gizi Harian")
            print("2. Riwayat dan Hasil Pemantauan Gizi")
            print("3. Manajemen Profil")
            print("4. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                input_gizi(user["username"])

            elif pilih == "2":
                riwayat_hasil_pemantauan(user["username"])

            elif pilih == "3":
                manajemen_profil(user)

            elif pilih == "4":
                break

            else:
                print(">> Pilihan tidak valid.")

        elif role == "admin":
            print("1. Buat Akun")
            print("2. Manajemen Profil")
            print("3. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                buat_akun_admin()

            elif pilih == "2":
                manajemen_profil(user)

            elif pilih == "3":
                break

            else:
                print(">> Pilihan tidak valid.")

        elif role == "tenaga_kesehatan":
            print("1. Pemantauan Gizi")
            print("2. Manajemen Profil")
            print("3. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                pemantauan_gizi_nakes(user)

            elif pilih == "2":
                manajemen_profil(user)

            elif pilih == "3":
                break

            else:
                print(">> Pilihan tidak valid.")

        else:
            print(">> Role tidak dikenali.")
            break
