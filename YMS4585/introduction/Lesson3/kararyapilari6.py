# Örnek:
# Kullanıcı dışarıdan ürün adı girecek,
# domates - biber - patlıcan => sebze reyonu 
# şampuan - parfüm - deodorant => kozmetik reyonu
# cep telefonu - televizyon - bilgisayar - kulaklık => teknoloji reyonu

# farklı bir ürün girerse , bu ürün bizde bulunmamaktadır uyarısı veriniz.



# urun_adi = str(input("Lütfen ürün adı giriniz : "))

# if urun_adi == "domates" or urun_adi == "biber" or urun_adi == "patlıcan":
#     print("Sebze Reyonu : ",urun_adi)
# elif urun_adi == "sampuan" or urun_adi == "parfum" or urun_adi == "deodorant":
#     print("Kozmetik Reyonu : ",urun_adi)
# elif urun_adi == "cep telefonu" or urun_adi == "televizyon" or urun_adi == "kulaklık":
#     print("Teknoloji reyonu : ",urun_adi)        
# else:
#     print("Girdiğiniz ürün bulunmamaktadır.")


urun = input("Lutfen ürün adı giriniz : ").lower().replace(" ", "")
if len(urun)> 1 :
    result = "Aradığınız {}, {} reyonundadır!"
    if urun == "domates" or urun == "biber" or urun == "patlıcan":
        result = result.format(urun, "sebze")
    elif urun == "şampuan" or urun == "parfüm" or urun == "deodorant":
        result = result.format(urun, "kozmetik")
    elif urun == "ceptelefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklık":
        result = result.format(urun, "teknoloji")
    print(result)
else:
        print("Lütfen bir ürün adı giriniz.")


    
