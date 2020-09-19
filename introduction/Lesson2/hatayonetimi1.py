# Programci hatalari (Error)
# Program kusurlari
# Istisnai hatalar
# Mantıksal hatalar
# print() --------printin basinda bosluk birakilmaz-----(programci hatasi)


# telefonNumarasi = int(input("Lutfen telefon mumaranizi giriniz :"))
# print("Tebrikler, hayatta bir kez bile olsa basari sagladin!")


try:
    telefonNo = int(input("Lutfen telefon numaranizi giriniz : "))
    print("tebrikler")

except ValueError:
    print("ValueError")

except ZeroDivisionError:
    print("ZeroDivisionError") 

except:
    print("Islem hatasi")


