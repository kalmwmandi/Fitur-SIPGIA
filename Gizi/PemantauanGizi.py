from .PencatatanGizi import lihat_catatan_user

def total_gizi(catatan):
    totalKal = sum(float(c["kalori"]) for c in catatan)
    totalPro = sum(float(c["protein"]) for c in catatan)
    totalKar = sum(float(c["karbohidrat"]) for c in catatan)

    return {
        "kalori": totalKal,
        "protein": totalPro,
        "karbo": totalKar
    }


def lihat_total(username):
    tanggal = input("Tanggal yang ingin dilihat: ")
    semua = lihat_catatan_user(username)
    catatan_tanggal = [c for c in semua if c["tanggal"] == tanggal]

    if len(catatan_tanggal) == 0:
        print("\n[!] Tidak ada catatan pada tanggal tersebut.")
        return

    total = total_gizi(catatan_tanggal)
    print(f"\n--- TOTAL GIZI {tanggal} ---")
    print(f"Kalori       : {total['kalori']}")
    print(f"Protein      : {total['protein']}")
    print(f"Karbohidrat  : {total['karbo']}")
