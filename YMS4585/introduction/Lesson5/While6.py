# Kullanıcının dışarıdan girdiği sayıların toplamını ekrana yazdıran bir uygulama yazınız

# örnek => 123 => 6

import os
os.system('clear')

sayi = input("Lütfen bir sayi giriniz : ")
index = 0
toplam = 0
while index < len(sayi):
    toplam += int(sayi[index])
    index += 1
print("Girilen sayıların toplamı : {}".format(toplam))
    