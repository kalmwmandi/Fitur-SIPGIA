from Gizi.PencatatanGizi import lihat_catatan_user

def hitung_selisih_hari(tanggal1, tanggal2):
    data1 = tanggal1.split("-")
    data2 = tanggal2.split("-")
    
    hari1 = int(data1[0])
    hari2 = int(data2[0])
    
    selisih = hari2 - hari1 + 1
    return selisih

def rekomendasi(username):
    print("\n--- REKOMENDASI NUTRISI MINGGUAN ---")
    
    catatan_user = lihat_catatan_user(username)
    
    if len(catatan_user) == 0:
        print("\n[!] Belum ada catatan gizi.")
        print("Silakan catat makanan Anda terlebih dahulu!")
        return
    
    print("\nMasukkan periode yang ingin dicek (maksimal 7 hari):")
    tanggal_awal = input("Tanggal awal (DD-MM-YYYY): ")
    tanggal_akhir = input("Tanggal akhir (DD-MM-YYYY): ")
    
    selisih = hitung_selisih_hari(tanggal_awal, tanggal_akhir)
    
    if selisih > 7:
        print("\n[X] Periode terlalu panjang! Maksimal 7 hari (seminggu).")
        return
    
    if selisih < 1:
        print("\n[X] Tanggal akhir harus lebih besar atau sama dengan tanggal awal!")
        return
    
    tanggal_dalam_periode = []
    for catatan in catatan_user:
        tgl = catatan["tanggal"]
        
        if tgl >= tanggal_awal and tgl <= tanggal_akhir:
            if tgl not in tanggal_dalam_periode:
                tanggal_dalam_periode.append(tgl)
    
    catatan_periode = []
    for catatan in catatan_user:
        if catatan["tanggal"] in tanggal_dalam_periode:
            catatan_periode.append(catatan)
    
    if len(catatan_periode) == 0:
        print(f"\n[!] Tidak ada catatan gizi dalam periode {tanggal_awal} sampai {tanggal_akhir}")
        return
    
    total_kalori = 0
    total_protein = 0
    total_karbohidrat = 0
    
    for catatan in catatan_periode:
        total_kalori = total_kalori + float(catatan["kalori"])
        total_protein = total_protein + float(catatan["protein"])
        total_karbohidrat = total_karbohidrat + float(catatan["karbohidrat"])
    
    jumlah_hari = len(tanggal_dalam_periode)
    print(f"\n=== AKUMULASI NUTRISI ({tanggal_awal} s/d {tanggal_akhir}) ===")
    print(f"Jumlah hari tercatat: {jumlah_hari} hari")
    print(f"\nTotal akumulasi:")
    print(f"Kalori       : {total_kalori:.0f} kkal")
    print(f"Protein      : {total_protein:.1f} gram")
    print(f"Karbohidrat  : {total_karbohidrat:.1f} gram")
    
    standar_kalori_mingguan = 2000 * jumlah_hari
    standar_protein_mingguan = 50 * jumlah_hari
    standar_karbohidrat_mingguan = 300 * jumlah_hari
    
    print(f"\nTarget standar nutrisi {jumlah_hari} hari:")
    print(f"Kalori       : {standar_kalori_mingguan:.0f} kkal")
    print(f"Protein      : {standar_protein_mingguan:.0f} gram")
    print(f"Karbohidrat  : {standar_karbohidrat_mingguan:.0f} gram")
    
    print("\n--- REKOMENDASI UNTUK ANDA ---")
    
    if total_kalori < standar_kalori_mingguan:
        kurang = standar_kalori_mingguan - total_kalori
        print(f"[!] Kalori masih kurang {kurang:.0f} kkal!")
        print("    Saran: Tambah porsi makan atau makan camilan sehat.")
    else:
        print("[OK] Kalori sudah mencukupi kebutuhan mingguan!")
    
    if total_protein < standar_protein_mingguan:
        kurang = standar_protein_mingguan - total_protein
        print(f"[!] Protein masih kurang {kurang:.1f} gram!")
        print("    Saran: Makan telur, ayam, ikan, tempe, atau tahu.")
    else:
        print("[OK] Protein sudah mencukupi kebutuhan mingguan!")
    
    if total_karbohidrat < standar_karbohidrat_mingguan:
        kurang = standar_karbohidrat_mingguan - total_karbohidrat
        print(f"[!] Karbohidrat masih kurang {kurang:.1f} gram!")
        print("    Saran: Tambah nasi, roti, atau kentang.")
    else:
        print("[OK] Karbohidrat sudah mencukupi kebutuhan mingguan!")
    
    print("\nTips Umum:")
    print("• Minum air putih minimal 8 gelas sehari")
    print("• Makan sayur dan buah setiap hari")
    print("• Olahraga teratur 30 menit per hari")
