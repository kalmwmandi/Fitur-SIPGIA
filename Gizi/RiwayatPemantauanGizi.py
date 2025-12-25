# riwayatpemantauangizi.py
from Gizi.PencatatanGizi import lihat_catatan_user
import os

DB_CATATAN_NAKES = "database_catatan_nakes.txt"


def ambil_catatan_nakes(username, tanggal):
    if not os.path.exists(DB_CATATAN_NAKES):
        return None

    with open(DB_CATATAN_NAKES, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if len(data) == 4:
                u = data[0]
                tgl = data[1]
                nakes = data[2]
                catatan = data[3]

                if u == username and tgl == tanggal:
                    return {
                        "nakes": nakes,
                        "catatan": catatan
                    }

    return None


def riwayat_hasil_pemantauan(username):
    data = lihat_catatan_user(username)

    if len(data) == 0:
        print("\n[!] Belum ada catatan gizi.")
        return

    print("\n========== Riwayat dan Hasil Pemantauan Gizi ==========")

    # ================= KELOMPOKKAN DATA PER TANGGAL =================
    data_per_tanggal = {}

    for d in data:
        tanggal = d["tanggal"]

        if tanggal not in data_per_tanggal:
            data_per_tanggal[tanggal] = []

        data_per_tanggal[tanggal].append(d)

    # ================= URUTKAN TANGGAL =================
    daftar_tanggal = []
    for tgl in data_per_tanggal:
        daftar_tanggal.append(tgl)

    daftar_tanggal.sort()

    # ================= TAMPILKAN DATA =================
    for tanggal in daftar_tanggal:
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
