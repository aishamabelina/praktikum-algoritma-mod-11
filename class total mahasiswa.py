class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_biodata(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Angkatan:", self.angkatan)


if __name__ == "__main__":
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    angkatan = input("Masukkan Tahun Angkatan: ")

    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBiodata Mahasiswa:")
    mahasiswa.tampilkan_biodata()

    
    print("\nTotal Mahasiswa:", Mahasiswa.total_mahasiswa)
