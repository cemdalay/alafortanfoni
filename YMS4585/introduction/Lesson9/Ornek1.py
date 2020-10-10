# dışarıdan girilen,metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını ekrana yazdırınız.

# ord()   : verdiginiz karakterin, ascii (sayisal) karsiligini teslim eder.
import os
os.system("Clear")


# def Metin(*deger):

#     for i in deger:
#         ascii_kod = ord(i)
#         #print(ascii_kod)

#     return deger


# Metin("a", "b", "c", "d")


def MetinToplamDeger(string):
    string = string.replace(" ", "")
    havuz = 0
    for i in list(string):
        havuz += ord(i)
    return havuz


total = MetinToplamDeger(
    input("Lütfen gereksiz ne kadar karakter varsa giriniz :"))

print(total)
