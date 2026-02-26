# Nomor 1
angka_list = [10, 20, 30]

try:
    index = int(input("Masukkan index (0-2): "))

    print(f"Nilai: {angka_list[index]}")

except ValueError:
    print("Harus berupa angka bulat!")

except IndexError:
    print("Index di luar jangkauan!")

finally:
    print("Selesai.")

"""
Hasil ketika dijalankan:

Masukkan index (0-2): hh
Harus berupa angka bulat!
Selesai.
"""
print()

# Nomor 2
print("--- Program Pembagian ---")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")

except ZeroDivisionError:
    print("Error: Waduh, nggak bisa bagi pake angka nol (0) ya!")

except ValueError:
    print("Error: Input harus berupa angka, jangan huruf!")

except Exception as e:
    print(f"Ada error tak terduga: {e}")

finally:
    print("Program selesai dijalankan.")

"""
Hasil ketika dijalankan:

--- Program Pembagian ---
Masukkan angka pertama: haha
Error: Input harus berupa angka, jangan huruf!
Program selesai dijalankan.
"""
