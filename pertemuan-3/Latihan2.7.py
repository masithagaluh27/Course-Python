nilai_mahasiswa = {'budi' : 85 , 'siti' : 90 , 'andi' : 75}
TotalNilai = 0
TotalMahasiswa = 0
for x in nilai_mahasiswa :
    TotalNilai+= nilai_mahasiswa [x]
    TotalMahasiswa += 1

rata_rata = TotalNilai / TotalMahasiswa
print (f"rata - rata nilai adalah" , format(rata_rata , ".2f"))