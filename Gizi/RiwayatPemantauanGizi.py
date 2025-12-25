# laporangizi.py
from .PencatatanGizi import lihat_catatan_user
import os

DB_CATATAN_NAKES = "database_catatan_nakes.txt"

def ambil_catatan_nakes(username, tanggal):
    """Mengambil catatan nakes untuk username dan tanggal tertentu"""
    if not os.path.exists(DB_CATATAN_NAKES):
        return None
    
    with open(DB_CATATAN_NAKES, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 4:
                u, tgl, nakes, catatan = data
                if u == username and tgl == tanggal:
                    return {"nakes": nakes, "catatan": catatan}
    return None

def riwayat_hasil_pemantauan(username):
    data = lihat_catatan_user(username)

    if not data:
        print("\n[!] Belum ada catatan gizi.")
        return

    print("\n========== Riwayat dan Hasil Pemantauan Gizi ==========")
    
    data_per_tanggal = {}
    for d in data:
        tgl = d['tanggal']
        if tgl not in data_per_tanggal:
            data_per_tanggal[tgl] = []
        data_per_tanggal[tgl].append(d)
    
    for tanggal in sorted(data_per_tanggal.keys()):
        print(f"\nRiwayat Pencatatan Gizi Tanggal {tanggal}:")
        
        for d in data_per_tanggal[tanggal]:
            print(
                f" • {d['makanan']} | "
                f"Kalori: {d['kalori']} kkal | "
                f"Protein: {d['protein']} g | "
                f"Karbohidrat: {d['karbohidrat']} g"
            )

        catatan_nakes = ambil_catatan_nakes(username, tanggal)
        if catatan_nakes:
            print(f"Rekomendasi atau Catatan dari {catatan_nakes['nakes']}:")
            print(f"     {catatan_nakes['catatan']}")