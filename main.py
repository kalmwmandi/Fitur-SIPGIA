from login.loginModule import loginAuth, registerTenagaKesehatan
from pencatatan_gizi_harian.PencatatanGiziHarian import menu_pencatatan
from pemantauan_gizi.PemantauanGizi import menu_pemantauan


def main():

    while True:
        print("\n=== SISTEM INFORMASI PEMANTAUAN GIZI (SIPGIA) ===")
        print("1. Login")
        print("2. Registrasi Tenaga Kesehatan")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            # --- LOGIN ---
            print("\n--- LOGIN ---")
            username = input("Username: ")
            password = input("Password: ")

            user = loginAuth(username, password)
            if not user:
                print("\nLogin gagal! Periksa username/password.")
                continue

            print(f"\nLogin berhasil! Selamat datang, {user['nama']} ({user['role']})")
            break  # lanjut ke menu setelah login

        elif pilih == "2":
            registerTenagaKesehatan()

        elif pilih == "3":
            print("\nTerima kasih telah menggunakan SIPGIA!")
            return

        else:
            print("Pilihan tidak valid.")


    # --------------------------
    # MENU UTAMA SETELAH LOGIN
    # --------------------------
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Pencatatan Gizi Harian (Pasien)")
        print("2. Pemantauan Gizi oleh Tenaga Kesehatan")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if user["role"] == "user":
                menu_pencatatan(user)
            else:
                print("\n[!] Hanya pasien yang dapat mengakses menu ini.")

        elif pilihan == "2":
            if user["role"] == "tenaga_kesehatan":
                menu_pemantauan(user)
            else:
                print("\n[!] Hanya tenaga kesehatan yang dapat mengakses menu ini.")

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan SIPGIA!")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
