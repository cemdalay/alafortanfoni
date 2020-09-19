try:
    sayi = int(input("Lütfen sadece sayısal değer giriniz : "))
    print("gelen sayı :",sayi)
    sayi = sayi / 0
    print("İşlem Sonucu :",sayi)
except ValueError as ex:
    print("Lütfen Tekrar Deneyiniz")
    print("Sistem mesajı", ex)    
except Exception as ex:
    print("İşlem Hatası")
    print("Sistem Mesajı :", ex)