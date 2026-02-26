A = [[5, 3, 1], [2, 8, 4], [6, 0, 7]]

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def tambah(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            hasil[i][j] = A[i][j] + B[i][j]
    return hasil


def kurang(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            hasil[i][j] = A[i][j] - B[i][j]
    return hasil


def skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil


C_tambah = tambah(A, B)
print()
print(f"penambahan matriks: {C_tambah}")
print()
C_kurang = kurang(A, B)
print(f"pengurangan matriks: {C_kurang}")
print()
C_skalar = skalar(A, 4)
for baris in C_skalar:
    print(f"perkalian skalar: {baris}")
print()
