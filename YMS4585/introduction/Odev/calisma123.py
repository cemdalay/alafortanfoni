def donustrucu(dizi):

    sayisal_dizi = []
    liste = dizi.split()
    for sayi in liste[0:]:
        if sayi in liste[0:] and (type(sayi) == float or type(sayi) == int):
            sayisal_dizi.append(sayi)
            print(sayisal_dizi)
            print(type(sayi))
        elif sayi in dizi[0:] and (type(sayi) != float or type(sayi) != int):
            print("Listenizde bulunan sayı olmayan değerler : ", sayi)
            print(type(sayi))
        else:
            print("Tekrar deneyiniz.")
        return liste


result = donustrucu(input("Lütfen sayı giriniz :"))
print(result)
