# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harfleri ayrıştırınız ve kullanıcıya toplam adetlerini gösteriniz.

import os
os.system('clear')

sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
sesli = []
sessiz = []

metin = input("Lütfen bir metin giriniz : ")

i = 0

while i < len(metin):
    karakter = metin[i]
    
    if sesli_harfler.count(karakter):
        sesli.append(karakter)
    else:
        sessiz.append(karakter)
    i += 1

print(f"Metin içerisinde bulunan toplam sesli harf sayısı : {len(sesli)}\nMetin içerisinde toplam sessiz harf sayısı : {len(sessiz)}")