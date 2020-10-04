# Yaptığımız işlemin sonunda oluşan değeri geriye teslim almak istiyor isek,function kullanmalıyız.

def Hesapla(x,y):
    toplam = x + y

    # not => return anahtar kelimesinden sonra, herhangi bir kod bloğu çalışmaz !
    return(toplam)

sonuc = Hesapla(10,3)
print("Sonuç :",sonuc)

# bu alan içerisinde diğer hesaplamalar yapılacak

