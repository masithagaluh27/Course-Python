#latihan 2.5

#latihan 2.6
buah = ("apel","pisang","mangga","jeruk","anggur")
buah_lain = buah[1::2]
print(" ")
print ("buah_lain :", buah_lain)

#latihan 2.7
nilai_mahasiswa ={budi : 85 , siti : 90 , andi : 75}
def rata_rata_nilai(data_mahasiswa):
    if len(data_mahasiswa) == 0:
        return 0
    total_nilai = sum(data_mahasiswa.values())
    rata_rata = total_nilai / len(data_mahasiswa)
    return rata_rata

# 3. Menguji fungsi dengan dictionary mahasiswa
hasil = rata_rata_nilai(mahasiswa)
print(f"Rata-rata nilai mahasiswa adalah: {hasil}")

#LATIHAN 2.8