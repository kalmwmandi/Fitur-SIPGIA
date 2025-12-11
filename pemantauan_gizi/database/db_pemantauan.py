import os

def baca_pemantauan_gizi(filename="database_pemantauan_gizi.txt"):
    pemantauan = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) >= 7:
                    pemantauan.append({
                        "id": data[0],
                        "id_catatan": data[1],
                        "username_pasien": data[2],
                        "tanggal_pemantauan": data[3],
                        "diagnosa": data[4],
                        "rekomendasi": data[5],
                        "tenaga_kesehatan": data[6],
                    })
    return pemantauan


def simpan_pemantauan(id_catatan, username_pasien, tanggal, diagnosa, rekomendasi, tenaga_kesehatan,
                      filename="database_pemantauan_gizi.txt"):
    data = baca_pemantauan_gizi(filename)
    new_id = len(data) + 1
    with open(filename, "a") as file:
        file.write(f"{new_id}|{id_catatan}|{username_pasien}|{tanggal}|{diagnosa}|{rekomendasi}|{tenaga_kesehatan}\n")
    return True


def update_pemantauan(id_pemantauan, diagnosa, rekomendasi, filename="database_pemantauan_gizi.txt"):
    data = baca_pemantauan_gizi(filename)
    with open(filename, "w") as file:
        for p in data:
            if p["id"] == id_pemantauan:
                file.write(f"{p['id']}|{p['id_catatan']}|{p['username_pasien']}|{p['tanggal_pemantauan']}|{diagnosa}|{rekomendasi}|{p['tenaga_kesehatan']}\n")
            else:
                file.write(f"{p['id']}|{p['id_catatan']}|{p['username_pasien']}|{p['tanggal_pemantauan']}|{p['diagnosa']}|{p['rekomendasi']}|{p['tenaga_kesehatan']}\n")
    return True


def get_pemantauan_by_pasien(username, filename="database_pemantauan_gizi.txt"):
    return [p for p in baca_pemantauan_gizi(filename) if p["username_pasien"] == username]
