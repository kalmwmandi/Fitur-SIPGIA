# pemantauangizi.py
from Gizi.PencatatanGizi import lihat_catatan_user, ambil_user_unik, baca_catatan
from Register import baca_database_user

DB_CATATAN_NAKES = "database_catatan_nakes.txt"


def total_gizi(catatan):
    total_kalori = 0
    total_protein = 0
    total_karbo = 0

    for c in catatan:
        total_kalori = total_kalori + c["kalori"]
        total_protein = total_protein + c["protein"]
        total_karbo = total_karbo + c["karbohidrat"]

    return {
        "kalori": total_kalori,
        "protein": total_protein,
        "karbo": total_karbo
    }


def pilih_user_gizi():
    users = ambil_user_unik()

    if len(users) == 0:
        print("[!] Belum ada user yang mengisi gizi.")
        return None

    print("\n--- DAFTAR USER ---")
    i = 1
    for u in users:
        print(f"{i}. {u}")
        i = i + 1

    while True:
        pilih = input("Pilih user: ")

        if pilih.isdigit():
            idx = int(pilih) - 1
            if idx >= 0 and idx < len(users):
                return users[idx]

        print("[X] Pilihan tidak valid")


def ambil_tb_bb(username):
    users = baca_database_user()

    for u in users:
        if u["username"] == username:
            return u["tb"], u["bb"]

    return "-", "-"


def rekap_gizi_harian(username):
    semua = baca_catatan()
    rekap = {}

    for c in semua:
        if c["username"] == username:
            tanggal = c["tanggal"]

            if tanggal not in rekap:
                rekap[tanggal] = {
                    "kalori": 0,
                    "protein": 0,
                    "karbo": 0
                }

            rekap[tanggal]["kalori"] = rekap[tanggal]["kalori"] + c["kalori"]
            rekap[tanggal]["protein"] = rekap[tanggal]["protein"] + c["protein"]
            rekap[tanggal]["karbo"] = rekap[tanggal]["karbo"] + c["karbohidrat"]

    return rekap


def simpan_catatan_nakes(username, tanggal, nama_nakes, catatan):
    with open(DB_CATATAN_NAKES, "a") as f:
        f.write(username + "|" + tanggal + "|" + nama_nakes + "|" + catatan + "\n")


def pemantauan_gizi_nakes(user_nakes):
    username = pilih_user_gizi()
    if not username:
        return

    tb, bb = ambil_tb_bb(username)
    rekap = rekap_gizi_harian(username)

    if not rekap:
        print("[!] Tidak ada data gizi.")
        return

    print(f"\n=== PEMANTAUAN GIZI : {username} ===")
    print(f"Tinggi Badan : {tb} cm")
    print(f"Berat Badan  : {bb} kg")

    print("\nTanggal       | Kalori | Protein | Karbo")
    print("----------------------------------------")

    tanggal_list = []
    for tgl in rekap:
        g = rekap[tgl]
        tanggal_list.append(tgl)
        print(
            f"{tgl:<13} | "
            f"{g['kalori']:.0f}   | "
            f"{g['protein']:.1f}    | "
            f"{g['karbo']:.1f}"
        )

    while True:
        print("\n1. Tambahkan Catatan")
        print("2. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            print("\nPilih tanggal:")
            i = 1
            for tgl in tanggal_list:
                print(f"{i}. {tgl}")
                i = i + 1

            pilih_tgl = input("Pilih tanggal: ")

            if not pilih_tgl.isdigit():
                print("[X] Pilihan tidak valid")
                continue

            idx = int(pilih_tgl) - 1
            if idx < 0 or idx >= len(tanggal_list):
                print("[X] Pilihan tidak valid")
                continue

            tanggal_terpilih = tanggal_list[idx]

            catatan = input("Masukkan catatan nakes: ").strip()
            if catatan == "":
                print("[X] Catatan tidak boleh kosong")
                continue

            simpan_catatan_nakes(
                username,
                tanggal_terpilih,
                user_nakes["nama"],
                catatan
            )

            print("[✓] Catatan berhasil disimpan")
            break

        elif pilih == "2":
            break

        else:
            print("[X] Pilihan tidak valid")
