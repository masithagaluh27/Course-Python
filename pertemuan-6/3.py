try:
    nama_file = 'text'
    # Mencoba membuka file
    file = open(nama_file, 'r')
    # Membaca isi file
    konten = file.read()
    print(konten)
except FileNotFoundError:
    # Menangani kesalahan jika file tidak ditemukan
    print(f"File '{nama_file}' tidak ditemukan. Silahkan cari file yang lain")
    print("testestes")
    # print("saya akan buat file baru nya")
    # f = open("contoh.txt","w")
except IsADirectoryError:
    print("ini directory bukan file")

except PermissionError:
    # Menangani kesalahan jika izin ditolak
    print(f"Izin untuk membuka file '{nama_file}' ditolak.")
except Exception as f:
    # Menangani kesalahan lain
    print(f"Terjadi kesalahan: {f}")
else:
    # Menutup file jika tidak ada eksepsi yang terjadi
    file.close()
finally:
    print("Blok finally dieksekusi.")
