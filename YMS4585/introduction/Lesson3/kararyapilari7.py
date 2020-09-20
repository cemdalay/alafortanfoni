# Örnek:
# Kullanıcı dışarıdan sipariş alınacak kitap adedi girilecek,
# birim fiyat 5 tl
# sipariş sayısı : 0 veya altı ise uyarı verdiriniz
# sipariş sayısı : 1 ile 20(dahil) ise %5 indirim uygulayınız
# sipariş sayısı : 21 ile 50(dahil) ise %10 indirim uygulayınız
# sipariş sayısı : 51 ile 80(dahil) ise %15 indirim uygulayınız
# sipariş sayısı : 81 ile 100(dahil) ise %20 indirim uygulayınız 
# sipariş sayısı : 100'den büyük ise %25 indirim uygulayınız 

# kitap_fiyat = 5

# siparis_sayisi = int(input("Lütfen kitap adedini giriniz : "))

# if siparis_sayisi <= 0:
#     print("Lütfen 0'dan büyük bir değer giriniz.")
# elif siparis_sayisi > 0 and siparis_sayisi <= 20:
#     print("Toplam İndirim Tutarı : ",siparis_sayisi * kitap_fiyat * 0.05)
#     print("Toplam İndirimli Tutar : ",siparis_sayisi * kitap_fiyat - siparis_sayisi * kitap_fiyat * 0.05)
# elif siparis_sayisi > 21 and siparis_sayisi <= 50:
#     print("Toplam İndirim Tutarı : ",siparis_sayisi * kitap_fiyat * 0.10)
#     print("Toplam İndirimli Tutar : ",siparis_sayisi * kitap_fiyat - siparis_sayisi * kitap_fiyat * 0.01)
# elif siparis_sayisi > 51 and siparis_sayisi <= 80:
#     print("Toplam İndirim Tutarı : ",siparis_sayisi * kitap_fiyat * 0.15)
#     print("Toplam İndirimli Tutar : ",siparis_sayisi * kitap_fiyat - siparis_sayisi * kitap_fiyat * 0.15)  
# elif siparis_sayisi > 81 and siparis_sayisi <= 100:
#     print("Toplam İndirim Tutarı : ",siparis_sayisi * kitap_fiyat * 0.20)
#     print("Toplam İndirimli Tutar : ",siparis_sayisi * kitap_fiyat - siparis_sayisi * kitap_fiyat * 0.20)    
# elif siparis_sayisi > 100 :
#     print("Toplam İndirim Tutarı : ",siparis_sayisi * kitap_fiyat * 0.25)
#     print("Toplam İndirimli Tutar : ",siparis_sayisi * kitap_fiyat - siparis_sayisi * kitap_fiyat * 0.25)          
# else:
#     print("Yanlış bir işlem yaptınız.")    

print("""
******** Kitap otomasyonuna hoşgeldiniz *********
*                                               *
*                                               *
*  Bige Adam Kitap Satış Otomasyonu             *
*                                               *
*                                               *
*************************************************
""")

try: 
    
    adet = int(input("Lütfen sipariş aded giriniz : "))
    if adet > 0:
        
        birim_fiyat = 5
        total = 0
        discount = ""
        dolar = 7.44
        result = """
        Verilen Sipariş Adedi                : {}
        Adet Birim Fiyat                     : {}$
        Toplam Tutar                         : {}$
        Yapılan indirim oranı                : {}
        Toplam Ödemeniz Gereken Tutar        : {}
        Türk Lirası Olarak Ödemek İsterseniz : {}TL
        """
    
    
        if adet <= 20:
            discount = "%5"
            total = (birim_fiyat * adet) * 0.95
        elif adet <= 50:
            discount = "%10"
            total = (birim_fiyat * adet) * 0.90
        elif adet <= 80:
            discount = "%15"
            total = (birim_fiyat * adet) * 0.85
        elif adet <= 100:
            discount = "%20"
            total = (birim_fiyat * adet) * 0.80
        else:
            discount = "%25"
            total = (birim_fiyat * adet) * 0.75
        print(result.format(adet,birim_fiyat,(adet * birim_fiyat),discount,total,(total * dolar)))
    else:
        print("Minumum sipariş adedi 1'dir")
except Exception as mahmud:
    print(mahmud)