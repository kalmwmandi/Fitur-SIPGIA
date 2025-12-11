def validasi_data_gizi(tanggal, makanan, kalori, protein, karbohidrat):
    if tanggal == "" or makanan == "" or kalori == "" or protein == "" or karbohidrat == "":
        return False

    try:
        float(kalori)
        float(protein)
        float(karbohidrat)
    except:
        return False

    return True
