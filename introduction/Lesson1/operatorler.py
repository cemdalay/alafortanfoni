# Aritmetik operatorler

# +, -, /, *, %, **

# sayi1 = 120
# sayi2 = 50

# toplam = sayi1 + sayi2
# print("Islem Sonucu" + " "*50 + str(toplam))   # *50 = 50 tane bosluk birak


# disaridan girilen 2 sayinin toplamasi
# disaridan alinan 2 sayinin butun islemlerini

sayi1 = input("Lutfen 1. sayiyi giriniz : ")
sayi2 = input("Lutfen 2. sayiyi giriniz : ")

toplam = int(sayi1) + int(sayi2)
print("Toplama Islemi Sonucu : " + str(toplam))

cikarma_islemi = int(sayi1) - int(sayi2)
print("Cıkarma Islemi Sonucu : " + str(cikarma_islemi))

bolme_islemi = float(sayi1) / float(sayi2)
print("Bolme Islemi Sonucu : " + str(bolme_islemi))

carpma_islemi = int(sayi1) * int(sayi2)
print("Carpma Islemi Sonucu : " + str(carpma_islemi))

mod_islemi = float(sayi1) % float(sayi2)
print("Mod Islemi Sonucu : " + str(mod_islemi))

kuvvet_islemi = int(sayi1) ** int(sayi2)
print("Kuvvet Islemi Sonucu : " + str(kuvvet_islemi))







