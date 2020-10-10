def Metot(**param):
    print(param["Ad"])
    print(param)


Metot(
    Ad="cem",
    Soyad="dalay",
    Telefon="+905312837775",
    Mail="cemdalay@outlook.com"

)
ad = input("Lütfen adınızı giriniz : ")
lastname = input("Lütfen soyadınızı giriniz : ")
Metot(Ad=ad, Soyad=lastname)
