import os

DB_CATATAN_NAKES = "database_catatan_nakes.txt"

def lihat_catatan_nakes(username):
    print("\n=== CATATAN DARI TENAGA KESEHATAN ===")

    if not os.path.exists(DB_CATATAN_NAKES):
        print("[!] Belum ada catatan.")
        return

    ada = False
    with open(DB_CATATAN_NAKES, "r") as f:
        for line in f:
            u, tgl, nakes, catatan = line.strip().split("|")
            if u == username:
                ada = True
                print(f"\nTanggal : {tgl}")
                print(f"Dari    : {nakes}")
                print(f"Catatan : {catatan}")

    if not ada:
        print("[!] Belum ada catatan untuk Anda.")
