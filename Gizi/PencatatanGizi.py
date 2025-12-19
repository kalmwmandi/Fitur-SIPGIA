# pencatatangizi.py
import os

DB_CATATAN = "database_catatan_gizi.txt"

def baca_catatan():
    if not os.path.exists(DB_CATATAN):
        return []

    hasil = []
    with open(DB_CATATAN, "r") as f:
        for line in f.readlines():
            data = line.strip().split("|")
            if len(data) >= 7:
                hasil.append({
                    "id": data[0],
                    "username": data[1],
                    "tanggal": data[2],
                    "makanan": data[3],
                    "kalori": data[4],
                    "protein": data[5],
                    "karbohidrat": data[6],
                })
    return hasil


def simpan_catatan(username, tanggal, makanan, kalori, protein, karbohidrat):
    semua = baca_catatan()
    new_id = len(semua) + 1

    with open(DB_CATATAN, "a") as f:
        f.write(f"{new_id}|{username}|{tanggal}|{makanan}|{kalori}|{protein}|{karbohidrat}\n")

    return True


def input_gizi():
    print("\n--- INPUT GIZI HARIAN ---")
    tanggal = input("Tanggal (DD-MM-YYYY): ")
    makanan = input("Nama makanan: ")
    kalori = input("Kalori: ")
    protein = input("Protein: ")
    karbo = input("Karbohidrat: ")
    return tanggal, makanan, kalori, protein, karbo


def lihat_catatan_user(username):
    semua = baca_catatan()
    return [c for c in semua if c["username"] == username]
