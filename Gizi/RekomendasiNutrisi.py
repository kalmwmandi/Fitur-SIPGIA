# rekomendasinutrisi.py
from Gizi.PencatatanGizi import lihat_catatan_user


def hitung_selisih_hari(tanggalAwal, tanggalAkhir):
    tglAwal = tanggalAwal.split("-")
    tglAkhir = tanggalAkhir.split("-")

    hariAwal = int(tglAwal[0])
    hariAkhir = int(tglAkhir[0])

    selisih = hariAkhir - hariAwal + 1
    return selisih


def rekomendasi(username):
    print("\n--- REKOMENDASI NUTRISI MINGGUAN ---")

    catatan_user = lihat_catatan_user(username)

    if len(catatan_user) == 0:
        print("\n[!] Belum ada catatan gizi.")
        print("Silakan masuk ke fitur Pencatatan Gizi terlebih dahulu!")
        return

    print("\nMasukkan periode yang ingin dicek (maksimal 7 hari):")
    tglAwal = input("Tanggal awal (DD-MM-YYYY): ")
    tglAkhir = input("Tanggal akhir (DD-MM-YYYY): ")

    selisih = hitung_selisih_hari(tglAwal, tglAkhir)

    if selisih > 7:
        print("\n[X] Periode terlalu panjang! Maksimal 7 hari.")
        return

    if selisih < 1:
        print("\n[X] Tanggal akhir harus lebih besar atau sama dengan tanggal awal!")
        return

    # ================= AMBIL TANGGAL DALAM PERIODE =================
    tanggal_dalam_periode = []

    for catatan in catatan_user:
        tgl = catatan["tanggal"]

        if tgl >= tglAwal and tgl <= tglAkhir:
            if tgl not in tanggal_dalam_periode:
                tanggal_dalam_periode.append(tgl)

    # ================= AMBIL CATATAN DALAM PERIODE =================
    catatan_periode = []

    for catatan in catatan_user:
        if catatan["tanggal"] in tanggal_dalam_periode:
            catatan_periode.append(catatan)

    if len(catatan_periode) == 0:
        print(f"\n[!] Tidak ada catatan gizi dalam periode {tglAwal} sampai {tglAkhir}")
        return

    # ================= HITUNG TOTAL NUTRISI =================
    totalKkal = 0
    totalProtein = 0
    totalKarbo = 0

    for catatan in catatan_periode:
        totalKkal = totalKkal + float(catatan["kalori"])
        totalProtein = totalProtein + float(catatan["protein"])
        totalKarbo = totalKarbo + float(catatan["karbohidrat"])

    jmlHari = len(tanggal_dalam_periode)

    print(f"\n=== AKUMULASI NUTRISI ({tglAwal} s/d {tglAkhir}) ===")
    print(f"Jumlah hari yang memiliki catatan gizi: {jmlHari} hari")

    print(f"\nTotal akumulasi:")
    print(f"Kalori       : {totalKkal:.0f} kkal")
    print(f"Protein      : {totalProtein:.1f} gram")
    print(f"Karbohidrat  : {totalKarbo:.1f} gram")

    # ================= TARGET STANDAR =================
    standardKal = 200 * jmlHari
    standardProtein = 50 * jmlHari
    standardKarbo = 300 * jmlHari

    print(f"\nTarget standar nutrisi {jmlHari} hari:")
    print(f"Kalori       : {standardKal:.0f} kkal")
    print(f"Protein      : {standardProtein:.0f} gram")
    print(f"Karbohidrat  : {standardKarbo:.0f} gram")

    print("\n--- REKOMENDASI UNTUK ANDA ---")

    if totalKkal < standardKal:
        kurang = standardKal - totalKkal
        print(f"[!] Kalori masih kurang {kurang:.0f} kkal!")
        print("    Saran: Tambah porsi makan atau makan camilan sehat.")
    else:
        print("[OK] Kalori sudah mencukupi kebutuhan mingguan!")

    if totalProtein < standardProtein:
        kurang = standardProtein - totalProtein
        print(f"[!] Protein masih kurang {kurang:.1f} gram!")
        print("    Saran: Makan telur, ayam, ikan, tempe, atau tahu.")
    else:
        print("[OK] Protein sudah mencukupi kebutuhan mingguan!")

    if totalKarbo < standardKarbo:
        kurang = standardKarbo - totalKarbo
        print(f"[!] Karbohidrat masih kurang {kurang:.1f} gram!")
        print("    Saran: Tambah nasi, roti, atau kentang.")
    else:
        print("[OK] Karbohidrat sudah mencukupi kebutuhan mingguan!")

    print("\nTips Umum:")
    print("• Minum air putih minimal 8 gelas sehari")
    print("• Makan sayur dan buah setiap hari")
    print("• Olahraga teratur 30 menit per hari")


def hitung_bmi(tb, bb):
    tb_m = tb / 100
    bmi = bb / (tb_m * tb_m)
    return bmi
