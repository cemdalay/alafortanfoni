# örnek 1) dışarıdan alınan 2 sayının toplamıyla farkının bölümünden kalanı kaçtır

# sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
# sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))

# toplam = sayi1 + sayi2
# fark = sayi1 - sayi2
# kalan = toplam % fark

# print(kalan)

# örnek 2) dışarıdan girilen bir sayının 10 eksiğinin 20 fazlasının ikiye bölümünden kalan kaçtır

# sayi = float(input("Lütfen sayıyı giriniz : "))

# sayi = sayi - 10
# sayi = sayi + 20
# sayi = sayi % 2
# print("İşlem sonucu : ",sayi)

# örnek) Vize notu %30, final notu %70'ini alıp not ortalamasını hesaplayıp kullanıcıya aldığı not'u gösteriniz

# vize_notu = float(input("Vize Notu : "))
# final_notu = float(input("Final Notu : "))

# dönem_ort = ((vize_notu * 0.30) + (final_notu * 0.70)) 

# print("Dönem Ortalaması : ",dönem_ort)

# örnek 5) Kullanıcı ilk olarak adını, 2 olarak ise soyismini girsin, işlem sonunda kullanıcıya   isim.soyisim@hotmail.com şeklimnde mail adersini teslim ediniz.

isim = input("Lütfen isminizi giriniz : ")
soyisim = input("Lütfen soyadınızı giriniz : ")

# mail = "{}.{}@hotmail.com".format(isim,soyisim)
# print(mail)

mail = f"{isim}{soyisim}@hotmail.com"
print(mail)




















