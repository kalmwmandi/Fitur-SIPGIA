from Gizi.PencatatanGizi import input_gizi, simpan_catatan, lihat_catatan_user
from Gizi.PemantauanGizi import lihat_total
from Gizi.LaporanGizi import laporan
from Gizi.RekomendasiNutrisi import rekomendasi


def dashboard(user):
    while True:
        print(f"\n===== DASHBOARD USER: {user['nama']} =====")
        print("1. Pencatatan Gizi Harian")
        print("2. Pemantauan Data Gizi")
        print("3. Laporan Gizi")
        print("4. Rekomendasi Nutrisi")
        print("5. Logout")

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
            print("\n[!] Logout berhasil.")
            break

        else:
            print("[X] Pilihan tidak valid.")
