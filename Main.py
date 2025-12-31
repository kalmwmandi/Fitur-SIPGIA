from Login import login
from Register import register
from Dashboard import dashboard

def main():
    while True:
        print("\n--- MENU UTAMA SIPGIA ---")
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
            print("\n>> Terima kasih telah menggunakan SIPGIA.")
            break

        else:
            print("\n>> Pilihan tidak valid.")

main()
