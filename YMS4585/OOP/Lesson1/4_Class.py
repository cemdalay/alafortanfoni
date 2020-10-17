class Ogrenci:
    """
    Bu alan zorunlu alan değilir, sadece __doc__ metodunu print ettiğinizde size bu sınıf hakkında bu alana ne yazdıysanız onu teslim eder.
    """
    Adi = ""

    def NotVer(self, arg):
        print(self.Adi, f"Adlı öğrenciye {arg} notu verildi")

    def CezaVer(self, arg):
        print(self.Adi, f"Adlı öğrenciye {arg} cezası verildi")

    def YoklamaGirisi(self, arg):
        print(self.Adi, f"Adlı öğrenci derse {arg}")


print(Ogrenci.__doc__)

ogr = Ogrenci()
ogr.Adi = "Cem Dalay"
ogr.CezaVer("Disiplin")
ogr.NotVer(100)
ogr.YoklamaGirisi("Girdi")
