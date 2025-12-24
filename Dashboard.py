# dashboard.py
from Gizi.PencatatanGizi import input_gizi, simpan_catatan
from Gizi.PemantauanGizi import lihat_total
from Gizi.LaporanGizi import laporan
from Gizi.RekomendasiNutrisi import rekomendasi
from Profil.ManajemenProfil import manajemen_profil


def dashboard(user):
    role = user["role"]

    while True:
        if role == "user":
            if user["kategori"] == "ibu_hamil":
                judul = "IBU HAMIL"
            else:
                judul = "ANAK"
            print(f"\n===== DASHBOARD {judul} : {user['nama']} =====")
        else:
            print(f"\n===== DASHBOARD {role.upper()} : {user['nama']} =====")

        # ================= USER =================
        if role == "user":
            print("1. Pencatatan Gizi Harian")
            print("2. Laporan Gizi")
            print("3. Manajemen Profil")
            print("4. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                input_gizi(user["username"])
                print("\n[✓] Data berhasil disimpan.")

            elif pilih == "2":
                laporan(user["username"])

            elif pilih == "3":
                manajemen_profil(user)
                
            elif pilih == "4":
                break

            else:
                print("[X] Pilihan tidak valid.")

        # ================= ADMIN =================
        elif role == "admin":
            print("1. Pencatatan Gizi Harian")
            print("2. Pemantauan Data Gizi")
            print("3. Laporan Gizi")
            print("4. Rekomendasi Nutrisi")
            print("5. Manajemen Profil")
            print("6. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                tgl, mkn, kal, pro, kar = input_gizi()
                simpan_catatan(user["username"], tgl, mkn, kal, pro, kar)
                print("\n[✓] Data berhasil disimpan.")

            elif pilih == "2":
                lihat_total(user["username"])

            elif pilih == "3":
                laporan(user["username"])

            elif pilih == "4":
                rekomendasi(user["username"])

            elif pilih == "5":
                manajemen_profil(user)
                
            elif pilih == "6":
                break

            else:
                print("[X] Pilihan tidak valid.")

        # ========== TENAGA KESEHATAN ==========
        elif role == "tenaga_kesehatan":
            print("1. Pemantauan Data Gizi")
            print("2. Laporan Gizi")
            print("3. Rekomendasi Nutrisi")
            print("4. Manajemen Profil")
            print("5. Logout")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                lihat_total(user["username"])

            elif pilih == "2":
                laporan(user["username"])

            elif pilih == "3":
                rekomendasi(user["username"])

            elif pilih == "4":
                manajemen_profil(user)

            elif pilih == "5":
                break

            else:
                print("[X] Pilihan tidak valid.")

        else:
            print("[X] Role tidak dikenali.")
            break
