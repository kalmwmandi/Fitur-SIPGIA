from Register import valid_password, baca_database_user, valid_nama
from getpass import getpass

DB_USER = "database_user.txt"


def simpan_semua_user(users):
    with open(DB_USER, "w") as f:
        for u in users:
            if u["tb"] == None:
                tb = "-"
            else:
                tb = str(u["tb"])
            
            if u["bb"] == None:
                bb = "-"
            else:
                bb = str(u["bb"])
            
            baris = u["username"] + "|" + u["password"] + "|" + u["nama"] + "|" + u["role"] + "|" + u["kategori"] + "|" + tb + "|" + bb + "\n"
            f.write(baris)


def manajemen_profil(user):
    while True:
        print("\n--- MANAJEMEN PROFIL ---")
        print("1. Lihat Profil")
        print("2. Ubah Nama Lengkap")
        print("3. Ubah Password")
        print("4. Kembali")

        pilih = input("Pilih menu: ")
        users = baca_database_user()

        if pilih == "1":
            print("\n--- PROFIL ANDA ---")
            print(f"Username : {user['username']}")
            print(f"Nama     : {user['nama']}")

            if user["role"] == "user":
                if user["kategori"] == "ibu_hamil":
                    kategoriTampil = "Ibu hamil"
                else:
                    kategoriTampil = "Anak"
                print(f"Kategori : {kategoriTampil}")

            else:
                print(f"Role     : {user['role']}")

        elif pilih == "2":
            while True:
                namaBaru = input("Nama baru: ").strip()

                if namaBaru == "":
                    print(">> Nama lengkap baru tidak boleh kosong.\n")
                    continue

                if valid_nama(namaBaru) == False:
                    print(">> Nama tidak boleh mengandung angka atau simbol, harus terdiri dari 3-50 karakter.\n")
                    continue

                break

            for u in users:
                if u["username"] == user["username"]:
                    u["nama"] = namaBaru
                    user["nama"] = namaBaru
            simpan_semua_user(users)
            print("\n>> Nama berhasil diperbarui.")

        elif pilih == "3":
            while True:
                passwordBaru = getpass("Password baru: ")

                if passwordBaru == "":
                    print(">> Password baru tidak boleh kosong.\n")
                    continue

                if valid_password(passwordBaru) == False:
                    print(">> Password minimal 8 karakter, ada huruf besar, kecil, angka, dan simbol.\n")
                    continue

                break

            for u in users:
                if u["username"] == user["username"]:
                    u["password"] = passwordBaru
                    user["password"] = passwordBaru

            simpan_semua_user(users)
            print("\n>> Password berhasil diperbarui.")

        elif pilih == "4":
            break

        else:
            print(">> Pilihan tidak valid.")