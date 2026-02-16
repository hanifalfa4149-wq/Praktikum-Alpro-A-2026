n = input("masukkan jumlah angka: ")

angka = []
for i in range(int(n)):
    angka.append(int(input("masukkan angka: ")))

angka.sort()
print(angka[-1] - angka[0])
