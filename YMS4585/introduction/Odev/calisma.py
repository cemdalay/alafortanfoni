# Kullanıcı dışarıdan sayısal olarak bir dizi gönderecek, siz bunu sayısal bir diziye çeviren bir metot yazınız.

# "3 4 5 6 7 8 9 10 34 55.6 a b c d e "=> [3,4,5,6,7,8,9,10.9,11,34,55.6]

import os
os.system('cls')


def SayisalDizi():
    dizi = []
    dizi_gir = input("Lütfen bir dizi giriniz : ")
    dizi.append(dizi_gir)
    print(",".join(dizi_gir))
    print(dizi_gir[1])
    print(dizi_gir[0:])
    #for sayi in dizi_gir:


SayisalDizi()
#3, 4, 5, 6, 7, 8, 10.8, "a", "b", "z", "t"
