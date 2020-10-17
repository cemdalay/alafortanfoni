# Kullanıcı dışarıdan sayısal olarak bir dizi gönderecek, siz bunu sayısal bir diziye çeviren bir metot yazınız.

# "3 4 5 6 7 8 9 10 34 55.6 a b c d e "=> [3,4,5,6,7,8,9,10.9,11,34,55.6]

import os
os.system('cls')


def SayisalDizi(*param):
    dizi = []
    for i in param:

        if i in param[0:] and (type(i) == float or type(i) == int or type(i) != str):
            dizi.append(i)
            dizi.sort()
            print(f"Girdiğiniz dizide sayı olan değerler :{dizi} ")

        elif i in param[0:] and (type(i) != float or type(i) != int):
            print("Listenizde bulunan sayı olmayan değerler : ", i)

        else:
            print("Tekrar deneyiniz.")


SayisalDizi(1, 2, 3, 45, 5.6, "a", "b")
