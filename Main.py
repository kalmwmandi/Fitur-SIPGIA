from Login import login
from Register import register
from Dashboard import dashboard

def main():
    user = None

    while True:
        print("\n===== MENU UTAMA SIPGIA =====")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            user = login()
            if user:
                dashboard(user)

        elif pilih == "2":
            register()

        elif pilih == "3":
            print("\nTerima kasih telah menggunakan SIPGIA.")
            break

        else:
            print("[X] Pilihan tidak valid.")


if __name__ == "__main__":
    main()
