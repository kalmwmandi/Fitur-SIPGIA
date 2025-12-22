# Profil/ManajemenProfil.py
from Register import valid_password, baca_database_user

DB_USER = "database_user.txt"


def simpan_semua_user(users):
    with open(DB_USER, "w") as f:
        for u in users:
            f.write(
                f"{u['username']}|{u['password']}|{u['nama']}|{u['role']}|{u.get('kategori','-')}\n"
            )


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
            nama_baru = input("Nama baru: ").strip()

            for u in users:
                if u["username"] == user["username"]:
                    u["nama"] = nama_baru
                    user["nama"] = nama_baru

            simpan_semua_user(users)
            print("[✓] Nama berhasil diperbarui")

        # ===== UBAH PASSWORD =====
        elif pilih == "3":
            password_baru = input("Password baru: ")

            if not valid_password(password_baru):
                print("[X] Password tidak memenuhi aturan")
                continue

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
