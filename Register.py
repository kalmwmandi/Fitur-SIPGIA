import os
import re
import stdiomask
import string

DB_USER = "database_user.txt"

def baca_database_user():
    if not os.path.exists(DB_USER):
        return []

    users = []
    with open(DB_USER, "r") as f:
        for line in f.readlines():
            data = line.strip().split("|")
            if len(data) >= 4:
                users.append({
                    "username": data[0],
                    "password": data[1],
                    "nama": data[2],
                    "role": data[3]
                })
    return users


def simpan_user(username, password, nama, role="user"):
    with open(DB_USER, "a") as f:
        f.write(f"{username}|{password}|{nama}|{role}\n")

def is_only_characters(input_string):
    pattern = r'^[a-zA-Z]+$'
    return bool(re.match(pattern, input_string))

print(f"'hello' only chars? {is_only_characters('hello')}") # True
print(f"'hello123!' only chars? {is_only_characters('hello123!')}") # False


def register():
    print("\n--- REGISTRASI ---")
    username()
    password()
    nama()
            
def username():
    while True:
        username = input("Username: ")
        if all(char.isalpha() or char.isspace() for char in username) and username.strip() != "":
            print("Username")
            users = baca_database_user()
            for u in users:
                if u["username"] == username:
                    print("\n[X] Username sudah digunakan.")
                return False
            break
        else:
            print("Username tidak boleh ada simbol dan tidak boleh kosong!")

def password():
    while True:
        password = stdiomask.getpass(prompt='Password: ', mask='*')
        adaHurufBesar = any(char.isupper() for char in password)
        adaSimbol = any(char in string.punctuation for char in password)
        if len(password) >= 8 and bool(password) != adaHurufBesar and (password) != adaSimbol:
            break
        elif len(password) and password != adaHurufBesar and password != adaSimbol:
            print("[X] Password tidak memenuhi syarat:\n- Minimal harus 8 karakter\n- Harus mengandung minimal 1 huruf besar\n- Harus mengandung minimal 1 simbol (contoh: !, @, #, $)")
        elif password != adaHurufBesar and password != adaSimbol:
            print("[X] Password tidak memenuhi syarat:\n- Harus mengandung minimal 1 huruf besar\n- Harus mengandung minimal 1 simbol (contoh: !, @, #, $)")
        elif password != adaSimbol:
            print("[X] Password tidak memenuhi syarat:\n- Harus mengandung minimal 1 simbol (contoh: !, @, #, $)")
        else:
            print("Password tidak boleh kosong")

def nama():
    while True:
        nama = input("Masukan nama: ")
        if nama == "":
            print("nama tidak boleh kosong!")
        elif len(nama) < 30:
            simpan_user(username, password, nama)
            print("\n[✓] Registrasi berhasil! Silakan login.")
            return True
        break
    
