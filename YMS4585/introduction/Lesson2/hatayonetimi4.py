try:
    sayi1 = int(input("Lütfen sayı giriniz : "))
    sayi2 = int(input("Lütfen sayı giriniz : "))
    sonuc = sayi1 / sayi2

except ValueError as mahmud:
    print("İşlem Hatası")

else:
    try:
        print(sayi1 / sayi2)
        print("İşlem Sonucu")
    except ZeroDivisionError as mahmud:
        print(mahmud)
    