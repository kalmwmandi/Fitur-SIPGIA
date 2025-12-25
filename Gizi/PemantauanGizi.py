from .PencatatanGizi import lihat_catatan_user, ambil_user_unik, baca_catatan
from Register import baca_database_user

DB_CATATAN_NAKES = "database_catatan_nakes.txt"


def total_gizi(catatan):
    return {
        "kalori": sum(c["kalori"] for c in catatan),
        "protein": sum(c["protein"] for c in catatan),
        "karbo": sum(c["karbohidrat"] for c in catatan)
    }


def pilih_user_gizi():
    users = ambil_user_unik()

    if not users:
        print("[!] Belum ada user yang mengisi gizi.")
        return None

    print("\n--- DAFTAR USER ---")
    for i, u in enumerate(users):
        print(f"{i+1}. {u}")

    while True:
        pilih = input("Pilih user: ")
        if pilih.isdigit():
            idx = int(pilih) - 1
            if 0 <= idx < len(users):
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
            tgl = c["tanggal"]
            if tgl not in rekap:
                rekap[tgl] = {"kalori": 0, "protein": 0, "karbo": 0}

            rekap[tgl]["kalori"] += c["kalori"]
            rekap[tgl]["protein"] += c["protein"]
            rekap[tgl]["karbo"] += c["karbohidrat"]

    return rekap


def simpan_catatan_nakes(username, tanggal, nama_nakes, catatan):
    with open(DB_CATATAN_NAKES, "a") as f:
        f.write(f"{username}|{tanggal}|{nama_nakes}|{catatan}\n")


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
    for tgl, g in rekap.items():
        tanggal_list.append(tgl)
        print(f"{tgl:<13} | {g['kalori']:.0f}   | {g['protein']:.1f}    | {g['karbo']:.1f}")

    while True:
        print("\n1. Tambahkan Catatan")
        print("2. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            print("\nPilih tanggal:")
            for i, tgl in enumerate(tanggal_list):
                print(f"{i+1}. {tgl}")

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
