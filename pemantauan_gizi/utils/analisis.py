def analisis_gizi_harian(total_kalori, total_protein, total_karbohidrat):
    diagnosa = []
    rekomendasi = []

    # Kalori
    if total_kalori < 1500:
        diagnosa.append("Asupan kalori sangat kurang")
        rekomendasi.append("Tingkatkan makanan berkalori tinggi")
    elif total_kalori < 2000:
        diagnosa.append("Asupan kalori kurang")
        rekomendasi.append("Tambah porsi makan")
    elif total_kalori > 3000:
        diagnosa.append("Asupan kalori berlebih")
        rekomendasi.append("Kurangi makanan tinggi kalori")
    else:
        diagnosa.append("Asupan kalori cukup")
        rekomendasi.append("Pertahankan pola makan")

    # Protein
    if total_protein < 40:
        diagnosa.append("Asupan protein kurang")
        rekomendasi.append("Perbanyak telur, ikan, tahu, tempe")
    elif total_protein > 80:
        diagnosa.append("Asupan protein berlebih")
        rekomendasi.append("Kurangi makanan tinggi protein")
    else:
        diagnosa.append("Asupan protein cukup")
        rekomendasi.append("Pertahankan konsumsi protein")

    # Karbohidrat
    if total_karbohidrat < 200:
        diagnosa.append("Asupan karbohidrat kurang")
        rekomendasi.append("Tambah nasi, roti, kentang")
    elif total_karbohidrat > 450:
        diagnosa.append("Asupan karbohidrat berlebih")
        rekomendasi.append("Kurangi makanan manis")
    else:
        diagnosa.append("Asupan karbohidrat cukup")
        rekomendasi.append("Pertahankan karbohidrat kompleks")

    return diagnosa, rekomendasi
