n = input("masukkan jumlah angka: ")

angka = []
for i in range(int(n)):
    angka.append(int(input("masukkan angka: ")))

angka_genap = [x for x in angka if x % 2 == 0]

if angka_genap:
    rata_rata = sum(angka_genap) / len(angka_genap)
    print(rata_rata)
else:
    print("Tidak ada angka genap dalam daftar")
