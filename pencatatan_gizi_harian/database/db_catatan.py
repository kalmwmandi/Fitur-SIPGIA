import os

def baca_catatan_gizi(filename="pencatatan_gizi_harian/database/database_catatan_gizi.txt"):
    catatan = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("|")
                if len(data) >= 7:
                    catatan.append({
                        "id": data[0],
                        "username": data[1],
                        "tanggal": data[2],
                        "makanan": data[3],
                        "kalori": data[4],
                        "protein": data[5],
                        "karbohidrat": data[6]
                    })
    return catatan


def simpan_catatan_gizi(username, tanggal, makanan, kalori, protein, karbohidrat,
                        filename="pencatatan_gizi_harian/database/database_catatan_gizi.txt"):

    catatan = baca_catatan_gizi(filename)
    new_id = len(catatan) + 1

    with open(filename, "a") as file:
        file.write(f"{new_id}|{username}|{tanggal}|{makanan}|{kalori}|{protein}|{karbohidrat}\n")

    return True


def get_catatan_by_user(username, filename="pencatatan_gizi_harian/database/database_catatan_gizi.txt"):
    semua = baca_catatan_gizi(filename)
    return [c for c in semua if c["username"] == username]
