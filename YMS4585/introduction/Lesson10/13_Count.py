# .count() => parametrede verdiğiniz değerin , metin içerisinde kaç adet olduğunu teslim eder.

metin = "bbeşiktaş bilge adam python dersleri"

sonuc = metin.count("b")
print(sonuc)

print(
    f"parametrede gönderdiğiniz değer, metin içerisinde {sonuc} adet bulunmaktadır.")
#parametrede gönderdiğiniz değer, metin içerisinde 3 adet bulunmaktadır.


sehirler = ["ankara", "edirne", "eskişehir",
            "urfa", "adana", "bursa", "eskişehir"]

param = "eskişehir"
result = sehirler.count("eskişehir")

print(f"{param} anahtar kelimesi dizi içerisinde toplam {result} defa geçmektedir")
#eskişehir anahtar kelimesi dizi içerisinde toplam 2 defa geçmektedir

metin = "cem daley"

retVal = metin.count("m", 2)
print(retVal)
retVal = metin.count("a", 6)
print(retVal)
retVal = metin.count("a", 2)
print(retVal)

retVal = metin.count("e", 1, len(metin))
print(retVal)
#help(metin.count)

retVal = metin.count("e", 1, 8)
print(retVal)
