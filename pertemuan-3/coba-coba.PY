#latihan conditional statements

nilai = {"siswa_a" : 100 , "siswa_b" : 85 ,"siswa_c" : 95 , "siswa_d" : 88}
total_nilai = 0
total_siswa = 0
for x in nilai :
    total_nilai += nilai[x]
    total_siswa += 1

rata_rata =total_nilai / total_siswa
print (f"rata - rata nilai adalah" , format(rata_rata, ".2f"))

nilai_cetak = ""
if rata_rata < 50 :
    nilai_cetak = "C"
elif rata_rata >= 50 and rata_rata < 80 :
    nilai_cetak = "B"
else :
    nilai_cetak = "A"

print ("nilai Cetaknya :", nilai_cetak )