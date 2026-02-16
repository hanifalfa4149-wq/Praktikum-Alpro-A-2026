n = input("masukkan jumlah angka: ")

angka = []
for i in range(int(n)):
    angka.append(int(input("masukkan angka: ")))

for x in angka:
    if x % 2 == 0:
        rata_rata = sum(int(x)) / len(int(x))
        print(rata_rata)
    else:
        print("Tidak ada angka genap dalam daftar")
