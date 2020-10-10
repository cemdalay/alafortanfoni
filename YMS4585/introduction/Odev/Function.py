# Kullanıcı dışarıdan sayısal olarak bir dizi gönderecek, siz bunu sayısal bir diziye çeviren bir metot yazınız.

# "3 4 5 6 7 8 9 10 34 55.6 a b c d e "=> [3,4,5,6,7,8,9,10.9,11,34,55.6]

import os
os.system('cls')


def SayisalDizi():
    sayisal_dizi = []
    dizi = []
    dizi = input("Lütfen bir dizi giriniz : ")
    dizi = list(dizi)
    print(dizi)
    print(dizi[3:5])

    print(type(dizi[0]))
    for sayi in dizi:

        if sayi in dizi[0:] and (type(sayi) == float or type(sayi) == int):
            sayisal_dizi.append(sayi)
            print(sayisal_dizi)
            print(type(sayi))
        elif sayi in dizi[0:] and (type(sayi) != float or type(sayi) != int):
            print("Listenizde bulunan sayı olmayan değerler : ", sayi)
            print(type(sayi))
        else:
            print("Tekrar deneyiniz.")


SayisalDizi()
#3, 4, 5, 6, 7, 8, 10.8, "a", "b", "z", "t"
