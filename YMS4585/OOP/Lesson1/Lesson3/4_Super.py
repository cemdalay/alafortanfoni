class Personel:
    _baslangic_maas = 4.000

    def __init__(self, ad, soyad, telefon):
        self.Ad = ad
        self.Soyad = soyad
        self.Telefon = telefon

    def FullName(self):
        return f"{self.Ad} {self.Soyad}"

    def Phone(self):
        return f"+90 {self.Telefon}"

    def __str__(self):
        return f"{self.Ad} {self.Soyad} {self.Telefon} {self._baslangic_maas}"


per = Personel("Cem", "Dalay", "5312837775")
print(per)
print(per.Phone())


class Developer(Personel):
    _baslangic_maas = 7.000

    def __init__(self, ad, soyad, telefon, yazilimdili):
        super().__init__(ad, soyad, telefon)
        self.YazilimDili = yazilimdili

    def __str__(self):
        return f"{super().__str__()}{self.YazilimDili}"


dev = Developer("Cem", "Dalay", "5312837775", "Python")

print(dev)
print(issubclass(Personel, Developer))  # False
# True => Personel developer sınıfının alt sınıfı mıdır ?
print(issubclass(Developer, Personel))
