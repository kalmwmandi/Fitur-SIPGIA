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
                user = data[0]
                tgl = data[1]
                nakes = data[2]
                catatan = data[3]
                
                if user == username and tgl == tanggal:
                    hasil = {}
                    hasil["nakes"] = nakes
                    hasil["catatan"] = catatan
                    return hasil
    return None

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                k = array[j]
                array[j] = array[j + 1]
                array[j + 1] = k
    return array

def riwayat_hasil_pemantauan(username):
    data = lihat_catatan_user(username)

    if len(data) == 0:
        print(">> Belum ada catatan gizi.")
        return

    print("\n--- Riwayat dan Hasil Pemantauan Gizi ---")
    
    dataDiTanggal = {}
    for i in data:
        tgl = i['tanggal']

        sudahAda = False
        for tanggal in dataDiTanggal:
            if tanggal == tgl:
                sudahAda = True
                break
        
        if sudahAda == False:
            dataDiTanggal[tgl] = []
        
        dataDiTanggal[tgl].append(i)
    
    listTanggal = []
    for tanggal in dataDiTanggal:
        listTanggal.append(tanggal)

    listTanggal = bubbleSort(listTanggal)

    for tanggal in listTanggal:
        print(f"\nRiwayat Pencatatan Gizi Tanggal {tanggal}:")
        
        for hasil in dataDiTanggal[tanggal]:
            print(
                f" • {hasil['makanan']} | "
                f"Kalori: {hasil['kalori']} kkal | "
                f"Protein: {hasil['protein']} g | "
                f"Karbohidrat: {hasil['karbohidrat']} g"
            )

        catatanNakes = ambil_catatan_nakes(username, tanggal)
        if catatanNakes:
            print(f"Rekomendasi atau Catatan dari {catatanNakes['nakes']}:")
            print(f"    {catatanNakes['catatan']}")