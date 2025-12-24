# pencatatangizi.py
from datetime import datetime
import os

DB_CATATAN = "database_catatan_gizi.txt"
DB_MAKANAN = "database_makanan.txt"


# ================= VALIDASI =================
def valid_tanggal(tanggal):
    try:
        dt = datetime.strptime(tanggal, "%d-%m-%Y")
        return dt.strftime("%d-%m-%Y")  # auto jadi 01-01-2025
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
                makanan.append({
                    "id": data[0],
                    "nama": data[1],
                    "kalori": float(data[2]),
                    "protein": float(data[3]),
                    "karbo": float(data[4])
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
                try:
                    hasil.append({
                        "id": data[0],
                        "username": data[1],
                        "tanggal": data[2],
                        "makanan": data[3],
                        "kalori": float(data[4]),
                        "protein": float(data[5]),
                        "karbohidrat": float(data[6]),
                    })
                except ValueError:
                    # skip data rusak
                    continue
    return hasil


def simpan_catatan(username, tanggal, makanan):
    semua = baca_catatan()
    new_id = len(semua) + 1

    with open(DB_CATATAN, "a") as f:
        f.write(
            f"{new_id}|{username}|{tanggal}|{makanan['nama']}|"
            f"{makanan['kalori']}|{makanan['protein']}|{makanan['karbo']}\n"
        )


# ================= INPUT GIZI =================
def input_gizi(username):
    print("\n--- INPUT GIZI HARIAN ---")

    # INPUT TANGGAL
    while True:
        input_tanggal = input("Tanggal (DD-MM-YYYY): ").strip()
        tanggal = valid_tanggal(input_tanggal)

        if not tanggal:
            print("[X] Format tanggal salah! Contoh: 1-1-2025 / 01-01-2025")
            continue
        break

    # PILIH MAKANAN
    daftar_makanan = baca_makanan()
    if not daftar_makanan:
        print("[X] Data makanan kosong.")
        return

    print("\n--- DAFTAR MAKANAN ---")
    for i, m in enumerate(daftar_makanan, start=1):
        print(f"{i}. {m['nama']}")

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
    return [c for c in semua if c["username"] == username]
