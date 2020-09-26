# birden fazla elemanla çalışacak ise, tek tek değişken tanımlamak yerine,dizi kullanıyoruz.
# Tanımlama şekli :

sehirler = ["istanbul", "edirne", "konya", "rize", "ankara", "eskişehir", "adana", "kayseri"]

# Not : bir dizinin maksimum index değeri, o dizinin eleman sayısı(uzunluğu) 1- değeridir.

# 1 2 3 4 5 6 7 8 => eleman sayısı 
# 0 1 2 3 4 5 6 7 => o elemanın dizi içerisindeki index değeridir.            
            
            
            #eleman sayısı => dizi içerisindeki toplam adet
            #index değeri => dizi içerisinde yer alan herhangi bir elemana ulaşma şekli

print(sehirler[0]) # dizinin ilk elemanını ekrana yazdırdık.

# dizinin son elemanını ekrana yazdırınız.

print(sehirler[7])

index = len(sehirler) # toplam eleman sayısını teslim eder.
index = len(sehirler) - 1 # o dizinin maximum index değerini verir.
print(index)
print(sehirler[index])

print(sehirler[2:7]) 
# 1.parametrede verilen index değeri(dahil) başlayacağı yeri gösterir
# 2. parametrede verilen index değerinin bir alt değerine kadar olan elemanları listeler.


# dizinin tüm elemanlarını ekrana yazdırmak istersek )

print(sehirler[:])

print("adana" in sehirler) # adana parametresi, dizi içerisinde geçmekte mi geçmemekte mi ?


#kullanıcı dışarıdan şehir adı girecek, var ise bu şehir dizi içerisinde yer almaktadır, yok ise, bu dizi şehir içerisinde yer almamaktadır mesajını veriniz.

sehir_adı = input("Lütfen bir şehir adı giriniz : ")


# if sehir_adı == "adana" or sehir_adı == "istanbul" or  sehir_adı == "edirne" or sehir_adı == "konya" or sehir_adı == "rize" or sehir_adı == "eskişehir" or sehir_adı == "ankara" or sehir_adı == "kayseri":
#     print("Girdiğiniz şehir dizi içerisinde yer almaktadır.")
# else:
#     print("Girdiğiniz şehir dizi içerisinde bulunmamaktadır.")

# result = f"parametrede gönderdiğiniz {sehir_adı} sehri, dizi içerisinde bulunmaktadır" if sehir_adı in sehirler else f"parametrede gönderdiğiniz {sehir_adı} sehri, dizi içerisinde yer almamaktadır"

# # ternary opt.
# # koşul içerisinde true dönerse,soldaki alan ,false dönerse sağdaki alan çalışır.

# print(result)


print(f"parametrede gönderdiğiniz {sehir_adı} sehri, dizi içerisinde yer alma{ '' if sehir_adı in sehirler else 'ma' }ktadır")

print("parametrede gönderdiğiniz {} sehri, dizi içerisinde yer alma{}ktadır".format(sehir_adı,("" if sehir_adı in sehirler else "ma")))


mylist1 = ["sehirler dizisi"]
print(mylist1)

mylist2 = ["arabalar dizisi"]
print(mylist2)

mylist3 = ["renkler dizisi"]
print(mylist3)

result = list(zip(mylist1,mylist2,mylist3))
print(result)