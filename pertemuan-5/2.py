class Produk ():

    def addProduk(self, data_produk):
        self.id = data_produk["id"]
        self.nama = data_produk["nama"]
        self.harga = data_produk["harga"]
        self.deskripsi = data_produk["deskripsi"]
        self.stok_produk = data_produk["stok_produk"]

        self.new__product = {
            "id": self.id,
            "nama": self.nama,
            "harga": self.harga,
            "deskripsi": self.deskripsi,
            "stok": self.stok,

        }

        return "data berhasil diupdate"

    def updateProduk(self, data_produk):
        self. new_produk["id "] = data_produk["id"],
        self. new_produk["nama "] = data_produk["nama"],
        self. new_produk["harga "] = data_produk["harga"],
        self. new_produk["deskripsi "] = data_produk["deskripsi"],
        self. new_produk["stok "] = data_produk["stok"],

        return True

    def getDetailProduk(self):
        return self.new_product


produk = {}

input_id = int(input("masukan id produk ="))
input_nama = input("masukan nama produk = ")
input_harga = int(input("masukan harga produk ="))
input_deskripsi = input("masukan deksripsi produk = ")
input_stok = int(input("masukan stok produk = "))


data_produk = {

    "id": input.id,
    "nama": input.nama,
    "harga": input.harga,
    "deskripsi": input.deskripsi,
    "stok": input.stok,
}

produk1 = Produk()
produk1.addProduk(data_produk)
print(produk1.getDetailProduk())

produk1.updateProduk({
    "id": "P001",
    "nama": "Keripik Pisang Coklat",
    "harga": 17000,
    "deskripsi": "Keripik pisang dengan lapisan coklat",
    "stok_produk": 35
})

print(produk1)
