def form_input_gizi():
    print("\n--- FORM PENCATATAN GIZI HARIAN ---")
    tanggal = input("Tanggal (DD-MM-YYYY): ")
    makanan = input("Makanan: ")
    kalori = input("Kalori (kkal): ")
    protein = input("Protein (g): ")
    karbohidrat = input("Karbohidrat (g): ")
    return tanggal, makanan, kalori, protein, karbohidrat


def tampilkan_catatan(catatan):
    if len(catatan) == 0:
        print("\n[!] Belum ada catatan.")
        return

    print("\n--- RIWAYAT CATATAN GIZI ---")
    print("-"*70)
    print(f"{'ID':<5}{'Tanggal':<15}{'Makanan':<20}{'Kalori':<10}{'Protein':<10}{'Karbo':<10}")
    print("-"*70)
    
    for c in catatan:
        print(f"{c['id']:<5}{c['tanggal']:<15}{c['makanan']:<20}{c['kalori']:<10}{c['protein']:<10}{c['karbohidrat']:<10}")

    print("-"*70)
