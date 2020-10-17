# Kullanıcı input aracılığıyla uygulamaya sayı girecek ,ve kullanıcı dilediği kadar sayı girebilir.
# Her sayı girildiğinde kullanıcıya yeni bir sayı girecek misin diye sorulacak,kullanıcı 'y' tuşuna basarsa lütfen sayı giriniz diyip içeriye sayı alınacak.
# Kullanıcı y harici bir tuşa basarsa, içeride yer alan tek sayıların en küçük ve en büyük sayısının birbirine olan farkını geriye dönsün.

import os
os.system('clear')


def FarkHesapla():
    go_on = "y"
    tek_sayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("Lütfen sadece sayısal değer giriniz :"))
        #os.system('clear')
        if number % 2 != 0:
            tek_sayilar.append(number)
        go_on = input("Yeni bir sayı eklemek istiyor musunuz (Y//N) : ")
        #os.system('clear')
    return max(tek_sayilar) - min(tek_sayilar)


sonuc = FarkHesapla()
print("İşlem sonucu :", sonuc)
