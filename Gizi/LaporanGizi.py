# laporangizi.py
from .PencatatanGizi import lihat_catatan_user

def laporan(username):
    data = lihat_catatan_user(username)

    if not data:
        print("\n[!] Belum ada catatan gizi.")
        return

    print("\n--- LAPORAN GIZI ---")
    for d in data:
        print(
            f"{d['tanggal']} - {d['makanan']} | "
            f"Kalori: {d['kalori']} kkal | "
            f"Protein: {d['protein']} g | "
            f"Karbohidrat: {d['karbohidrat']} g"
        )
