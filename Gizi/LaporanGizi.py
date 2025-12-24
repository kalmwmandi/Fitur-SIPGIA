# laporangizi.py
from .PencatatanGizi import lihat_catatan_user

def laporan(username):
    data = lihat_catatan_user(username)
    print("\n--- LAPORAN GIZI ---")
    for d in data:
        print(f"{d['tanggal']} - {d['makanan']} | Kalori: {d['kalori']}")
