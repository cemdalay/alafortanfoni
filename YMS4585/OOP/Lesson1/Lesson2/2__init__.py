# __init__ constructor (yapıcı metot) sınıftan bir örnek aldığınızda yapılması gereken konfigürasyon var ise,__init__ içerisinde tanımlayabilirsiniz.

from datetime import datetime


class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    CreatedDate = ""
    IkincilAd = ""

    def __str__(self):
        return f"İsim-Soyisim:{self.Adi} {self.Soyadi}\nTelefon:{self.Telefon}\nMail:{self.Adi}{self.Soyadi}@outlook.com\nKayıt eklenme tarihi:{self.CreatedDate}"

    def __init__(self, isim, soyisim, telefon, mail, ikincilAd):
        self.CreatedDate = datetime.now()
        self.Adi = isim
        self.Soyadi = soyisim
        self.Telefon = telefon
        self.Mail = mail
        self.IkincilAd = ikincilAd
        print("__init__ metodu çalıştı")

    def GetInfo(self):
        return f"Adı : {self.Adi}\nSoyadı : {self.Soyadi}"


# __init__ metodunu parametre verdiğinizden dolayı,artık burdaki gibi atama işlemi yapamazsınız.
# personel.Adi = "cem"
# personel.Soyadi = "dalay"
# personel.Telefon = "+905312837775"
# personel.Mail = "cemdalay@outlook.com"
# print(personel)


personel = Personel("cem", "dalay", "+905312837775", "cem dalay", "jam")


print(personel)
print(personel.GetInfo())
