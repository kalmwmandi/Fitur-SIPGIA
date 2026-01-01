from .PencatatanGizi import ambil_user_unik, baca_catatan
from Register import baca_database_user

DB_CATATAN_NAKES = "database_catatan_nakes.txt"


def total_gizi(catatan):
    totalKalori = 0
    totalProtein = 0
    totalKarbo = 0
    
    for c in catatan:
        totalKalori = totalKalori + c["kalori"]
        totalProtein = totalProtein + c["protein"]
        totalKarbo = totalKarbo + c["karbohidrat"]
    
    hasil = {}
    hasil["kalori"] = totalKalori
    hasil["protein"] = totalProtein
    hasil["karbo"] = totalKarbo
    return hasil


def pilih_user_gizi():
    users = ambil_user_unik()

    if len(users) == 0:
        print(">> Belum ada user yang mengisi gizi.")
        return None

    print("\n--- DAFTAR USER ---")
    nomor = 1
    for u in users:
        print(f"{nomor}. {u}")
        nomor += 1

    while True:
        pilih = input("Pilih user: ")

        if len(pilih) == 0:
            print(">> Pilihan tidak valid.")
            continue
        
        pilihValid = True
        for i in pilih:
            if i < '0' or i > '9':
                pilihValid = False
                break
        
        if pilihValid == True:
            nomor = int(pilih) - 1
            if nomor >= 0 and nomor < len(users):
                return users[nomor]
        
        print(">> Pilihan tidak valid.")


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
            
            sudahAda = False
            for tanggal in rekap:
                if tanggal == tgl:
                    sudahAda = True
                    break
            
            if sudahAda == False:
                rekap[tgl] = {}
                rekap[tgl]["kalori"] = 0
                rekap[tgl]["protein"] = 0
                rekap[tgl]["karbo"] = 0

            rekap[tanggal]["kalori"] = rekap[tanggal]["kalori"] + c["kalori"]
            rekap[tanggal]["protein"] = rekap[tanggal]["protein"] + c["protein"]
            rekap[tanggal]["karbo"] = rekap[tanggal]["karbo"] + c["karbohidrat"]

    return rekap


def simpan_catatan_nakes(username, tanggal, namaNakes, catatan):
    with open(DB_CATATAN_NAKES, "a") as f:
        f.write(f"{username}|{tanggal}|{namaNakes}|{catatan}\n")


def pemantauan_gizi_nakes(userNakes):
    username = pilih_user_gizi()
    if username == None:
        return

    tb, bb = ambil_tb_bb(username)
    rekap = rekap_gizi_harian(username)

    if len(rekap) == 0:
        print(">> Tidak ada data gizi.")
        return

    print(f"\n--- PEMANTAUAN GIZI : {username} ---")
    print(f"Tinggi Badan : {tb} cm")
    print(f"Berat Badan  : {bb} kg")

    print("\nTanggal       | Kalori | Protein | Karbo\n")

    tanggalList = []
    for tgl in rekap:
        tanggalList.append(tgl)
        g = rekap[tgl]
        print(f"{tgl:<13} | {g['kalori']:.0f}   | {g['protein']:.1f}    | {g['karbo']:.1f}")

    while True:
        print("\n1. Tambahkan Catatan")
        print("2. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            print("\nPilih tanggal:")
            nomor = 1
            for tgl in tanggalList:
                print(f"{nomor}. {tgl}")
                nomor += 1

            pilihTgl = input("Pilih tanggal: ")

            if len(pilihTgl) == 0:
                print(">> Pilihan tidak valid.")
                continue
            
            pilihValid = True
            for i in pilihTgl:
                if i < '0' or i > '9':
                    pilihValid = False
                    break
            
            if pilihValid == False:
                print(">> Pilihan tidak valid.")
                continue

            nomor = int(pilihTgl) - 1
            if nomor < 0 or nomor >= len(tanggalList):
                print(">> Pilihan tidak valid.")
                continue

            tanggalTerpilih = tanggalList[nomor]

            catatan = input("Masukkan catatan nakes: ").strip()
            if catatan == "":
                print(">> Catatan tidak boleh kosong.")
                continue

            simpan_catatan_nakes(
                username,
                tanggalTerpilih,
                userNakes["nama"],
                catatan
            )

            print("\n>> Catatan berhasil disimpan.")
            break

        elif pilih == "2":
            break

        else:
            print(">> Pilihan tidak valid.")
