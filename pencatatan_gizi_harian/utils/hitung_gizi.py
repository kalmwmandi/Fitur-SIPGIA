def hitung_total_gizi_harian(catatan_list):
    total = {
        "total_kalori": 0,
        "total_protein": 0,
        "total_karbohidrat": 0
    }

    for c in catatan_list:
        total["total_kalori"] += float(c["kalori"])
        total["total_protein"] += float(c["protein"])
        total["total_karbohidrat"] += float(c["karbohidrat"])

    return total
