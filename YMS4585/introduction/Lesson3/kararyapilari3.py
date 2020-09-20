# kullanıcının dışarıdan girdiği sayının tek veya çift olma durumunu kontrol etme,sayı tek ise, sayı tektir uyarısı,çift ise sayı çifttir uyarısı veriniz
try:

    sayi = int(input("Lütfen bir sayı giriniz : "))
    if (sayi / 2 == 0): 
        print("Girdiğiniz sayı çifttir.")   
    else:
        sayi / 2 != 0
        print("Girdiğiniz sayı tektir.")

except Exception as mahmud:
    print(mahmud)