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


