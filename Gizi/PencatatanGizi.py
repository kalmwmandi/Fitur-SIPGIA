# pencatatangizi.py
from datetime import datetime
import os

DB_CATATAN = "database_catatan_gizi.txt"
DB_MAKANAN = "database_makanan.txt"


# ================= VALIDASI =================
def valid_tanggal(tanggal):
    try:
        dt = datetime.strptime(tanggal, "%d-%m-%Y")
        return dt.strftime("%d-%m-%Y")
    except ValueError:
        return None


# ================= DATABASE MAKANAN =================
def baca_makanan():
    if not os.path.exists(DB_MAKANAN):
        print("[X] Database makanan tidak ditemukan!")
        return []

    makanan = []

    with open(DB_MAKANAN, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if len(data) == 5:
                id_makanan = data[0]
                nama = data[1]
                kalori = float(data[2])
                protein = float(data[3])
                karbo = float(data[4])

                makanan.append({
                    "id": id_makanan,
                    "nama": nama,
                    "kalori": kalori,
                    "protein": protein,
                    "karbo": karbo
                })

    return makanan


# ================= DATABASE CATATAN =================
def baca_catatan():
    if not os.path.exists(DB_CATATAN):
        return []

    hasil = []

    with open(DB_CATATAN, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if len(data) == 7:
                id_catatan = data[0]
                username = data[1]
                tanggal = data[2]
                makanan = data[3]

                try:
                    kalori = float(data[4])
                    protein = float(data[5])
                    karbo = float(data[6])
                except ValueError:
                    continue

                hasil.append({
                    "id": id_catatan,
                    "username": username,
                    "tanggal": tanggal,
                    "makanan": makanan,
                    "kalori": kalori,
                    "protein": protein,
                    "karbohidrat": karbo
                })

    return hasil


def simpan_catatan(username, tanggal, makanan):
    semua = baca_catatan()
    new_id = len(semua) + 1

    with open(DB_CATATAN, "a") as f:
        f.write(
            str(new_id) + "|" +
            username + "|" +
            tanggal + "|" +
            makanan["nama"] + "|" +
            str(makanan["kalori"]) + "|" +
            str(makanan["protein"]) + "|" +
            str(makanan["karbo"]) + "\n"
        )


# ================= INPUT GIZI =================
def input_gizi(username):
    print("\n--- INPUT GIZI HARIAN ---")

    # INPUT TANGGAL
    while True:
        input_tanggal = input("Tanggal (DD-MM-YYYY): ").strip()
        tanggal = valid_tanggal(input_tanggal)

        if tanggal is None:
            print("[X] Format tanggal salah! Contoh: 1-1-2025 / 01-01-2025")
            continue

        break

    # PILIH MAKANAN
    daftar_makanan = baca_makanan()
    if len(daftar_makanan) == 0:
        print("[X] Data makanan kosong.")
        return

    print("\n--- DAFTAR MAKANAN ---")
    i = 1
    for m in daftar_makanan:
        print(f"{i}. {m['nama']}")
        i = i + 1

    while True:
        pilih = input("Pilih nomor makanan: ")

        if not pilih.isdigit():
            print("[X] Masukkan angka!")
            continue

        idx = int(pilih) - 1
        if idx < 0 or idx >= len(daftar_makanan):
            print("[X] Pilihan tidak valid!")
            continue

        makanan = daftar_makanan[idx]
        break

    simpan_catatan(username, tanggal, makanan)
    print("\n[✓] Data gizi berhasil disimpan.")


# ================= LAPORAN =================
def lihat_catatan_user(username):
    semua = baca_catatan()
    hasil = []

    for c in semua:
        if c["username"] == username:
            hasil.append(c)

    return hasil


def ambil_user_unik():
    semua = baca_catatan()
    users = []

    for c in semua:
        if c["username"] not in users:
            users.append(c["username"])

    return users
