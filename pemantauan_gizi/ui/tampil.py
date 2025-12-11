def tampilkan_daftar_pasien(users):
    pasien_list = [u for u in users if u["role"] == "user"]

    if not pasien_list:
        print("\n[!] Belum ada pasien terdaftar.")
        return []

    print("\n--- DAFTAR PASIEN ---")
    print("-"*60)
    print(f"{'No':<5}{'Username':<20}{'Nama':<35}")
    print("-"*60)
    for i, p in enumerate(pasien_list, 1):
        print(f"{i:<5}{p['username']:<20}{p['nama']:<35}")
    print("-"*60)

    return pasien_list


def tampilkan_catatan_pasien(catatan):
    print("\n=== CATATAN GIZI PASIEN ===")
    if not catatan:
        print("[!] Pasien belum memiliki catatan gizi.")
        return

    print("-"*60)
    for c in catatan:
        print(f"Tanggal : {c['tanggal']}")
        print(f"Status  : {c.get('status', '-')}")  # jika belum ada status pemantauan
        print(f"Catatan : {c.get('catatan', '-')}")
        print("-"*60)


def tampilkan_riwayat_pemantauan(data):
    print("\n=== RIWAYAT PEMANTAUAN ===")
    if not data:
        print("[!] Belum ada riwayat pemantauan.")
        return

    print("-"*60)
    for c in data:
        print(f"Tanggal : {c['tanggal']}")
        print(f"Status  : {c['status']}")
        print(f"Catatan : {c['catatan']}")
        print("-"*60)


def tampilkan_detail_pemantauan(hasil):
    print("\n=== HASIL ANALISIS GIZI ===")
    if not hasil:
        print("[!] Tidak ada hasil analisis.")
        return

    print(f"Total Kalori     : {hasil['total_kalori']} kkal")
    print(f"Total Protein    : {hasil['total_protein']} g")
    print(f"Total Karbohidrat: {hasil['total_karbohidrat']} g")
    print(f"Status Gizi      : {hasil['status']}")
    print(f"Saran            : {hasil['saran']}")
