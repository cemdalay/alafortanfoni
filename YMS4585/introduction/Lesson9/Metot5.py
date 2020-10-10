def Metot(**param):
    print("-"*45)
    for key, value in param.items():
        print("{0:8} : {1}".format(key, value))
    print("-"*45)


Metot(
    Ad="cem",
    Soyad="dalay",
    Telefon="+905312837775",
    Mail="cemdalay@outlook.com"
)
