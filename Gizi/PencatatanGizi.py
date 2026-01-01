from datetime import datetime
import os

DB_CATATAN = "database_catatan_gizi.txt"
DB_MAKANAN = "database_makanan.txt"

def valid_tanggal(tanggal):
    if len(tanggal) != 10 or tanggal[2] != '-' or tanggal[5] != '-':
        return None

    for i in [0, 1, 3, 4, 6, 7, 8, 9]:
        if tanggal[i] < '0' or tanggal[i] > '9':
            return None

    hari = int(tanggal[0:2])
    bulan = int(tanggal[3:5])
    tahun = int(tanggal[6:10])

    if bulan < 1 or bulan > 12:
        return None
    
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        maxHari = 31

    elif bulan in [4, 6, 9, 11]:
        maxHari = 30

    else:  
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            maxHari = 29
        else:
            maxHari = 28

    if hari < 1 or hari > maxHari:
        return None

    if datetime(tahun, bulan, hari).strftime("%d-%m-%Y") != tanggal:
        return None

    return tanggal

def baca_makanan():
    if os.path.exists(DB_MAKANAN) == False:
        print(">> Database makanan tidak ditemukan!.")
        return []

    makanan = []

    with open(DB_MAKANAN, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
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

def baca_catatan():
    if os.path.exists(DB_CATATAN) == False:
        return []

    hasil = []

    with open(DB_CATATAN, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) == 7:
                kaloriValid = True
                for kal in data[4]:
                    if kal < '0' or kal > '9':
                        if kal != '.':
                            kaloriValid = False
                            break
                
                proteinValid = True
                for pro in data[5]:
                    if pro < '0' or pro > '9':
                        if pro != '.':
                            proteinValid = False
                            break
                
                karboValid = True
                for kar in data[6]:
                    if kar < '0' or kar > '9':
                        if kar != '.':
                            karboValid = False
                            break
                
                if kaloriValid == True and proteinValid == True and karboValid == True:
                    hasil.append({
                        "id": data[0],
                        "username": data[1],
                        "tanggal": data[2],
                        "makanan": data[3],
                        "kalori": float(data[4]),
                        "protein": float(data[5]),
                        "karbohidrat": float(data[6])
                    })
    return hasil

def simpan_catatan(username, tanggal, makanan):
    semua = baca_catatan()
    idBaru = len(semua) + 1

    with open(DB_CATATAN, "a") as f:
        f.write(
            f"{idBaru}|{username}|{tanggal}|{makanan['nama']}|"
            f"{makanan['kalori']}|{makanan['protein']}|{makanan['karbo']}\n"
        )

def input_gizi(username):
    print("\n--- INPUT GIZI HARIAN ---")

    while True:
        inputanTanggal = input("Tanggal (DD-MM-YYYY): ").strip()
        tanggal = valid_tanggal(inputanTanggal)

        if tanggal == None:
            print(">> Format tanggal salah! Contoh: 1-1-2025 / 01-01-2025.")
            continue

        break

    daftarMakanan = baca_makanan()
    if len(daftarMakanan) == 0:
        print(">> Data makanan kosong.")
        return

    print("\n--- DAFTAR MAKANAN ---")
    nomor = 1
    for m in daftarMakanan:
        print(f"{nomor}. {m['nama']}")
        nomor += 1

    while True:
        pilih = input("Pilih nomor makanan: ")

        if len(pilih) == 0:
            print(">> Masukkan angka!.")
            continue

        pilihValid = True
        for i in pilih:
            if i < '0' or i > '9':
                pilihValid = False
                break

        if pilihValid == False:
            print(">> Pilihan tidak valid!.")
            continue

        nomor = int(pilih) - 1
        if nomor < 0 or nomor >= len(daftarMakanan):
            print(">> Pilihan tidak valid.")
            continue

        makanan = daftarMakanan[nomor]
        break

    simpan_catatan(username, tanggal, makanan)
    print("\n>> Data gizi berhasil disimpan.")

def lihat_catatan_user(username):
    semua = baca_catatan()
    hasil = []
    
    for i in semua:
        if i["username"] == username:
            hasil.append(i)
    
    return hasil

def ambil_user_unik():
    semua = baca_catatan()
    users = []

    for i in semua:
        sudahAda = False
        for u in users:
            if u == i["username"]:
                sudahAda = True
                break
        
        if sudahAda == False:
            users.append(i["username"])

    return users