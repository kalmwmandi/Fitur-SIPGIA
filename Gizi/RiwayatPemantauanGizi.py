from .PencatatanGizi import lihat_catatan_user
import os

DB_CATATAN_NAKES = "database_catatan_nakes.txt"

def ambil_catatan_nakes(username, tanggal):
    if os.path.exists(DB_CATATAN_NAKES) == False:
        return None
    
    with open(DB_CATATAN_NAKES, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) == 4:
                if data[0] == username and data[1] == tanggal:
                    return {"nakes": data[2], "catatan": data[3]}
    return None

def bubbleSorting(l, k):
    n = len(l)
    hasil = []
    for item in l:
        hasil.append(item)
    
    for i in range(n):
        for j in range(n - i - 1):
            if hasil[j][k] < hasil[j + 1][k]:
                sementara = hasil[j]
                hasil[j] = hasil[j + 1]
                hasil[j + 1] = sementara
    return hasil

def riwayat_hasil_pemantauan(username):
    data = lihat_catatan_user(username)

    if len(data) == 0:
        print(">> Belum ada catatan gizi.")
        return

    print("\n--- RIWAYAT DAN HASIL PEMANTAUAN GIZI ---")
    
    print("\nNo  | Tanggal       | Makanan                 | Kalori | Protein | Karbo\n")
    no = 1
    for i in range(len(data)):
        makanan = data[i]['makanan']
        if len(makanan) > 23:
            makanan = makanan[:20] + "..."
        print(str(no) + "   | " + data[i]['tanggal'] + "   | " + makanan + "   | " + str(data[i]['kalori']) + "   | " + str(data[i]['protein']) + "   | " + str(data[i]['karbohidrat']))
        tglNext = ""
        if i + 1 < len(data):
            tglNext = data[i + 1]['tanggal']
        if data[i]['tanggal'] != tglNext:
            catatan = ambil_catatan_nakes(username, data[i]['tanggal'])
            if catatan:
                print(f"    Catatan dari {catatan['nakes']}: {catatan['catatan']}")
        no = no + 1

    while True:
        print("\n1. Cari Berdasarkan Tanggal")
        print("2. Urutkan Berdasarkan Nilai Gizi")
        print("0. Kembali")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tglCari = input("Masukkan tanggal (DD-MM-YYYY): ")
            hasil = []
            for item in data:
                if item['tanggal'] == tglCari:
                    hasil.append(item)
            if len(hasil) == 0:
                print(">> Tidak ditemukan.")
            else:
                print("\nNo  | Tanggal       | Makanan                 | Kalori | Protein | Karbo\n")
                no = 1
                for i in range(len(hasil)):
                    makanan = hasil[i]['makanan']
                    if len(makanan) > 23:
                        makanan = makanan[:20] + "..."
                    print(str(no) + "   | " + hasil[i]['tanggal'] + "   | " + makanan + "   | " + str(hasil[i]['kalori']) + "   | " + str(hasil[i]['protein']) + "   | " + str(hasil[i]['karbohidrat']))
                    tglNext = ""
                    if i + 1 < len(hasil):
                        tglNext = hasil[i + 1]['tanggal']
                    if hasil[i]['tanggal'] != tglNext:
                        catatan = ambil_catatan_nakes(username, hasil[i]['tanggal'])
                        if catatan:
                            print(f"    Catatan dari {catatan['nakes']}: {catatan['catatan']}")
                    no = no + 1
        
        elif pilihan == "2":
            print("\n1. Kalori")
            print("2. Protein")
            print("3. Karbohidrat")
            pil = input("Pilihan: ")
            
            if pil == "1":
                sorted_data = bubbleSorting(data, 'kalori')
            elif pil == "2":
                sorted_data = bubbleSorting(data, 'protein')
            elif pil == "3":
                sorted_data = bubbleSorting(data, 'karbohidrat')
            else:
                continue
            
            print("\nNo  | Tanggal       | Makanan                 | Kalori | Protein | Karbo\n")
            no = 1
            for i in range(len(sorted_data)):
                makanan = sorted_data[i]['makanan']
                if len(makanan) > 23:
                    makanan = makanan[:20] + "..."
                print(str(no) + "   | " + sorted_data[i]['tanggal'] + "   | " + makanan + "   | " + str(sorted_data[i]['kalori']) + "   | " + str(sorted_data[i]['protein']) + "   | " + str(sorted_data[i]['karbohidrat']))
                tglNext = ""
                if i + 1 < len(sorted_data):
                    tglNext = sorted_data[i + 1]['tanggal']
                if sorted_data[i]['tanggal'] != tglNext:
                    catatan = ambil_catatan_nakes(username, sorted_data[i]['tanggal'])
                    if catatan:
                        print(f"    Catatan dari {catatan['nakes']}: {catatan['catatan']}")
                no = no + 1
        
        elif pilihan == "0":
            break