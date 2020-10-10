# .sorted() => dizi içerisinde yer alan elemanları A'dan Z'ye 0'dan 9'a sıralama yapar

import locale
dizi = ['a', 's', 'd', 'f', 'g', 'h', 'l', 'ş', 'ç', 'ğ', 'i']
print(sorted(dizi))  # ['a', 'd', 'f', 'g', 'h', 'i', 'l', 's', 'ç', 'ğ', 'ş']

print(sorted("bilgeadambeşiktaşşubesipythondersleri"))
#['a', 'a', 'a', 'b', 'b', 'b', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'g', 'h', 'i', 'i', 'i', 'i', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'r', 'r', 's', 's', 't', 't', 'u', 'y', 'ş', 'ş', 'ş']


# alfabetik sıraya göre değil ascii kod değerine göre sıralama yaptığından,türkçe karakterleri dizinin sonuna ekleyecektir.
#locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")  # windows için
locale.setlocale(locale.LC_ALL, "tr_TR")  # GNU\Linux için

sonuc = sorted("bilgeadambeşiktaşşubesipythondersleri", key=locale.strxfrm)
print(sonuc)
