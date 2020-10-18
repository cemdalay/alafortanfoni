class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    Yas = 0

# self metodu default olarak sınıfın adını ve ram üzerindeki adresini teslim eder.
# Siz __str__ metodunu override(yeniden yazma) işlemi yaparsanız,sizin geriye döndüğünüz ekranda görünüyor olacak.

    def __str__(self):
        return f"{self.Adi} {self.Soyadi}"


personel = Personel()
personel.Adi = "Cem"
personel.Soyadi = "Dalay"
personel.Telefon = "+905312837775"
personel.Mail = "cemdalay@outlook.com"
personel.Yas = 100

print(personel)
# sınıftan aldığımız örneği direkt olarak print ederseniz size ram üzerinde tuttuğu adresi teslim eder. =>  <__main__.Personel object at 0x107cc4e50>
