import json

def load_data():
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except:
        return []

def simpan_data(todos):
    with open("todos.json", "w") as f:
        json.dump(todos, f)

def tampilkan_tugas(todos):
    if len(todos) == 0:
        print("Belum ada tugas")
    else:
        print("List tugas:")
        for i, t in enumerate(todos):
            status = "done" if t["done"] else "not yet"
            print(i+1, ".", t["task"], status)

def tambah_tugas(todos):
    tugas = input("Masukkan tugas: ")
    todos.append({"task": tugas, "done": False})
    simpan_data(todos)

def hapus_tugas(todos):
    try:
        nomor = int(input("Masukkan nomor tugas: "))
        if 0 < nomor <= len(todos):
            todos.pop(nomor - 1)
            simpan_data(todos)
            print("Tugas dihapus")
        else:
            print("Nomor tidak valid")
    except:
        print("Input harus angka!")

def tandai_selesai(todos):
    try:
        nomor = int(input("Nomor tugas selesai: "))
        if 0 < nomor <= len(todos):
            todos[nomor - 1]["done"] = True
            simpan_data(todos)
            print("Ditandai selesai")
        else:
            print("Nomor tidak valid")
    except:
        print("Input harus angka!")

def edit_tugas(todos):
    try:
        nomor = int(input("Nomor tugas yang diedit: "))
        if 0 < nomor <= len(todos):
            tugas_baru = input("Tugas baru: ")
            todos[nomor - 1]["task"] = tugas_baru
            simpan_data(todos)
            print("Tugas diupdate")
        else:
            print("Nomor tidak valid")
    except:
        print("Input harus angka!")

def main():
    todos = load_data()

    while True:
        print("\n=== TO-DO APP ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Edit tugas")
        print("4. Hapus tugas")
        print("5. Tandai selesai")
        print("6. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tambah_tugas(todos)
        elif pilihan == "2":
            tampilkan_tugas(todos)
        elif pilihan == "3":
            edit_tugas(todos)
        elif pilihan == "4":
            hapus_tugas(todos)
        elif pilihan == "5":
            tandai_selesai(todos)
        elif pilihan == "6":
            break

main()