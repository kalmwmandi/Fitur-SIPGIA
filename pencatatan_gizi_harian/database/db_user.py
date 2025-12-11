import os

def baca_database_user(filename="pencatatan_gizi_harian/database/database_user.txt"):
    users = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("|")
                if len(data) >= 4:
                    users.append({
                        "username": data[0],
                        "password": data[1],
                        "nama": data[2],
                        "role": data[3]
                    })
    return users


def simpan_user(username, password, nama, role, filename="pencatatan_gizi_harian/database/database_user.txt"):
    with open(filename, "a") as file:
        file.write(f"{username}|{password}|{nama}|{role}\n")
