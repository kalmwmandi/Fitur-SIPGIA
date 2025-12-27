# Profil/ManajemenProfil.py
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
        print("\n=== MANAJEMEN PROFIL ===")
        print("1. Lihat Profil")
        print("2. Ubah Nama Lengkap")
        print("3. Ubah Password")
        print("4. Kembali")

        pilih = input("Pilih menu: ")
        users = baca_database_user()

        # ===== LIHAT PROFIL =====
        if pilih == "1":
            print("\n--- PROFIL ANDA ---")
            print(f"Username : {user['username']}")
            print(f"Nama     : {user['nama']}")

            if user["role"] == "user":
                if user["kategori"] == "ibu_hamil":
                    kategori_tampil = "Ibu hamil"
                else:
                    kategori_tampil = "Anak"
                print(f"Kategori : {kategori_tampil}")

            else:
                print(f"Role     : {user['role']}")

        # ===== UBAH NAMA =====
        elif pilih == "2":
            while True:
                nama_baru = input("Nama baru: ").strip()

                if nama_baru == "":
                    print("[X] Nama lengkap baru tidak boleh kosong.\n")
                    continue

                if not valid_nama(nama_baru):
                    print("[X] Nama tidak boleh mengandung angka atau simbol, harus terdiri dari 3-50 karakter.\n")
                    continue

                break

            for u in users:
                if u["username"] == user["username"]:
                    u["nama"] = nama_baru
                    user["nama"] = nama_baru

            simpan_semua_user(users)
            print("[✓] Nama berhasil diperbarui")


        # ===== UBAH PASSWORD =====
        elif pilih == "3":
            while True:
                password_baru = getpass("Password baru: ")

                if password_baru == "":
                    print("[X] Password baru tidak boleh kosong.\n")
                    continue

                if not valid_password(password_baru):
                    print("[X] Password minimal 8 karakter, ada huruf besar, kecil, angka, dan simbol\n")
                    continue

                break

            for u in users:
                if u["username"] == user["username"]:
                    u["password"] = password_baru
                    user["password"] = password_baru

            simpan_semua_user(users)
            print("[✓] Password berhasil diperbarui")

        # ===== KEMBALI =====
        elif pilih == "4":
            break

        else:
            print("[X] Pilihan tidak valid")