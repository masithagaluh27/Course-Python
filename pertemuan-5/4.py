class BangunDatar:
    def __init__(self, parameter):
        self.parameter = parameter

    def luas(self):
        return "cara hitung luas"

    def keliling(self):
        return "cara hitung keliling"


class PersegiPanjang(BangunDatar):
    def luas(self):
        return self.parameter["panjang"] * self.parameter["lebar"]

    def keliling(self):
        return 2 * (self.parameter["panjang"] + self.parameter["lebar"])


class Persegi(BangunDatar):
    def luas(self):
        return self.parameter["sisi"] ** 2

    def keliling(self):
        return 4 * self.parameter["sisi"]


class Trapesium(BangunDatar):
    def luas(self):
        return 0.5 * (self.parameter["alas_a"] + self.parameter["alas_b"]) * self.parameter["tinggi"]

    def keliling(self):
        return self.parameter["alas_a"] + self.parameter["alas_b"] + self.parameter["sisi_miring_1"] + self.parameter["sisi_miring_2"]


class Lingkaran(BangunDatar):
    def luas(self):
        return 3.14 * self.parameter["jari_jari"] ** 2

    def keliling(self):
        return 2 * 3.14 * self.parameter["jari_jari"]


# Pemanggilan
persegi_panjang_1 = PersegiPanjang({"panjang": 10, "lebar": 20})
print(persegi_panjang_1.luas())       # Output: 200
print(persegi_panjang_1.keliling())   # Output: 60

persegi_1 = Persegi({"sisi": 10})
print(persegi_1.luas())               # Output: 100
print(persegi_1.keliling())           # Output: 40

trapesium_1 = Trapesium({
    "alas_a": 5,
    "alas_b": 6,
    "tinggi": 4,
    "sisi_miring_1": 3,
    "sisi_miring_2": 4
})
print(trapesium_1.luas())             # Output: 22.0
print(trapesium_1.keliling())        # Output: 18

lingkaran_1 = Lingkaran({"jari_jari": 10})
print(lingkaran_1.luas())             # Output: 314.0
print(lingkaran_1.keliling())         # Output: 62.8


