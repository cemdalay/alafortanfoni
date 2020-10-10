# dışarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metot tekniği:
import os
os.system("Clear")


def Hesapla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam


result = Hesapla(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Toplama işlemi sonucu", result)
