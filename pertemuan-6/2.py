file = open("saudara.txt", "w")
total_orang_tua = int(input("Masukkan jumlah orang tua = "))
orang_tuas = []

file.write("---------------------\n")
file.write("Nama Orang Tua :\n")
total_ortu = 0
for x in range(total_orang_tua):
    orang_tua = input("Masukkan nama orang tua = ")
    orang_tuas.append(orang_tua)
    file.write("Nama Orang Tua = "+orang_tua+"\n")
    total_ortu += 1

total_ortu_str = 'total orang tua = '+str(total_ortu)+'\n'
file.write(total_ortu_str)
file.write("---------------------\n")
file.write("Nama Saudara :\n")
total_saudara = int(input("Masukkan jumlah saudara = "))
saudaras = []
total_sdr = 0

for x in range(total_saudara):
    saudara = input("Masukkan nama saudara = ")
    saudaras.append(saudara)
    file.write("Nama Saudara =  "+saudara+"\n")
    total_sdr += 1

total_saudara_str = 'total saudara = '+str(total_sdr)+'\n'
file.write(total_saudara_str)
file.write("---------------------\n")
file.close()
