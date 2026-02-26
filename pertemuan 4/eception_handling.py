class NamaError(Exception):
    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(self.pesan)


class UmurError(Exception):
    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(self.pesan)


def registrasi_peserta():
    print("=== REGISTRASI PESERTA EVENT ===")

    while True:
        try:
            nama = input("Nama lengkap: ").strip()
            if len(nama) < 3:
                raise NamaError("[ERROR] namanya kependekan, Minimal 3 karakter.")
            break
        except NamaError as e:
            print(e)
            print("isi ulang yaa\n")

    while True:
        try:
            umur_input = input("Umur: ")
            try:
                umur = int(umur_input)
            except ValueError:
                print("[ERROR] umur nya bilangan bulat lah, masak bekoma")
                continue

            if not (17 <= umur <= 60):
                raise UmurError("[ERROR] Umur tidak memenuhi syarat (17-60 tahun).")
            break
        except UmurError as e:
            print(e)
            print("isi ulang yaa\n")

    while True:
        try:
            email = input("Email: ").strip()
            if "@" not in email:
                raise ValueError("[ERROR] Email nya salah, kasih tanda '@'.")
            break
        except ValueError as e:
            print(e)
            print("isi ulang yaa\n")

    while True:
        try:
            no_hp = input("no HP: ").strip()
            if not no_hp.isdigit():
                raise ValueError("[ERROR] no HP nya cuma boleh angka.")
            if not (10 <= len(no_hp) <= 13):
                raise ValueError("[ERROR] no HP nya salah tu! Harus 10-13 digit angka.")
            break
        except ValueError as e:
            print(e)
            print("isi ulang yaa\n")

    print("okee siaapp.")

    print("\n=== DATA PESERTA ===")
    print(f"Nama   : {nama}")
    print(f"Umur   : {umur} tahun")
    print(f"Email  : {email}")
    print(f"No HP  : {no_hp}")
    print("Status : TERDAFTAR")


if __name__ == "__main__":
    registrasi_peserta()
