#latihan 2.1
print("masitha")
print("python's is easy, bro!")
print('"guk guk guk,"aku mendengar suara anjing hitam itu.')

#latihan 2.2
#nomor 1
print("masitha")
nilai1 = int(99)
nilai2= float(45.9)
nilai3=float(7.0)
nilai4=int(7)
nilai5= "'abc'"

print("nilai_1 :" , nilai1) #nilai int
print("nilai_2 :" , nilai2) #nilai float
print("nilai_3 :" , nilai3) #nilai float
print("nilai_4 :" , nilai4) #nilai int
print("nilai_5 :" , nilai5) #nilai str

#nomor 2
nilai_saya = 99
nilai_saya = 0
print (nilai_saya)

#latihan 2.3
nama = input ('siapakah nama anda?')
usia = int(input('berapa usia anda'))
income = float (input('berapakah enghasian anda?'))
print (" ")
print ('berikut adalah data yang telah anda masukan :')
print ('nama :' , nama)
print ('usia' , usia)
print ('penghasilan :' , income)

#nmor 1
# Dapatkan harga asli barang tersebut.
harga_asli = float(input("Masukkan harga asli barang: "))
# Hitung besarnya diskon
diskon = harga_asli * 0.2
# Hitung harga jualnya
harga_jual = harga_asli - diskon
# Menampilkan harga jual
print('Harga jual adalah', harga_jual)


#LATIHAN 2.4
#NOMOR1
bil1 = float(input("Masukkan bil 1: "))  
bil2= float(input("Masukkan bil 2: "))  
bil3 = float(input("Masukkan bil 3: "))  
bil4 = float(input("Masukkan bil 4: ")) 

print (" ")
result1 = float (bil1 + bil2 * bil3)
print("result1 =", result1)

result2 = float (bil1 / bil2 - bil3)
print("result2 =", result2)

result3 = float (bil1 + bil2 * bil3 - bil4)
print("result3 =", result3)

result4 = float ((bil1 + bil2) * bil3)
print("result4 =", result4)

result5 = float (bil1 / (bil2 - bil3))
print("result5 =", result5)

result6 = float (bil1 + bil2 * (bil3 - bil4))
print("result6 =", result6)

result7 = float (bil1 // bil2)
print("result7 =", result7)

result8 = float (bil1 % bil2)
print("result8 =", result8)

print (" ")

#NOMOR 2
F = float(input("masukan nilai uang yang anda inginkan = $ "))
r = float(input("masukan nilai bunga per tahun (%) = "))
r = r/100
n = float (input("masukan jangka waktu (tahun) = "))
p = float (F*(1+r)**n)

print(" ")
print("menghitung...")
print(" ")

print("maka uang yang harus anda tabung hari ini adalah $" , p )
