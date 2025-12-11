# PemantauanGizi.py

from login import loginModule as lgn
from pencatatan_gizi_harian import PencatatanGiziHarian as pgh

from pemantauan_gizi.database.db_pemantauan import (
    baca_pemantauan_gizi,
    simpan_pemantauan,
    update_pemantauan,
    get_pemantauan_by_pasien
)

from pemantauan_gizi.utils.analisis import analisis_gizi_harian
from pemantauan_gizi.ui.menu import menu_tenaga_kesehatan
from pemantauan_gizi.ui.tampil import (
    tampilkan_daftar_pasien,
    tampilkan_catatan_pasien,
    tampilkan_riwayat_pemantauan,
    tampilkan_detail_pemantauan,
)


def menu_pemantauan(user):
    """Dipanggil dari main.py untuk Tenaga Kesehatan."""

    while True:
        pilihan = menu_tenaga_kesehatan(user["nama"])

        # 1. Lihat daftar pasien
        if pilihan == "1":
            data = baca_pemantauan_gizi()
            tampilkan_daftar_pasien(data)

        # 2. Lihat catatan gizi pasien tertentu
        elif pilihan == "2":
            username = input("Masukkan username pasien: ")
            catatan = get_pemantauan_by_pasien(username)
            tampilkan_catatan_pasien(catatan)

        # 3. Analisis gizi pasien
        elif pilihan == "3":
            username = input("Masukkan username pasien: ")
            catatan = get_pemantauan_by_pasien(username)

            if not catatan:
                print("\n[!] Pasien belum memiliki catatan gizi.")
            else:
                hasil = analisis_gizi_harian(catatan)
                tampilkan_detail_pemantauan(hasil)

        # 4. Tambah pemantauan baru
        elif pilihan == "4":
            username = input("Masukkan username pasien: ")
            tanggal = input("Tanggal (DD-MM-YYYY): ")
            status = input("Status pemantauan (normal/kurang/lebih): ")
            catatan = input("Catatan tambahan: ")

            simpan_pemantauan(username, tanggal, status, catatan)
            print("\n[✓] Pemantauan berhasil ditambahkan!")

        # 5. Update pemantauan
        elif pilihan == "5":
            username = input("Masukkan username pasien: ")
            tanggal = input("Tanggal pemantauan: ")

            status = input("Status baru: ")
            catatan = input("Catatan baru: ")

            update_pemantauan(username, tanggal, status, catatan)
            print("\n[✓] Pemantauan berhasil diperbarui!")

        elif pilihan == "6":
            print("\nLogout tenaga kesehatan berhasil.")
            break

        input("\nTekan Enter untuk melanjutkan...")
