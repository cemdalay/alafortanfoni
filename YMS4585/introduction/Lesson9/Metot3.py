import os
os.system("Clear")


def Metot(ad, soyad, mail, gorev, *telefon):
    print("""
    Personelin Adı                    : {}
    Personelin Soyadı                 : {}
    Personelin Mail Adresi            : {}
    Personelin Görevi                 : {}
    Personelin Telefon Numaraları     : {}
    
    """.format(ad, soyad, mail, gorev, " - ".join(telefon)))


Metot("cem", "dalay", "cemdalay@outlook.com",
      "danısman", "053125", "32323", "053125", "32323")
