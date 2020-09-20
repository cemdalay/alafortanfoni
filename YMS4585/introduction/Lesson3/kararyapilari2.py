 # kullanıcı dışarıdan not değerini girecek ve girilen not o'dan küçükse , 0'dan küçük not giremezsiniz uyarısı , 
 # 100'den büyükse 100'den büyük not girişi yapamazsınız uyarısı , girilen not 0'a veya 100'e eşit veya küçükse , kullanıcaya girdiği notu gösteriniz.

try:

    ders_notu = int(input("Lütfen ders notunu giriniz : "))

    if (ders_notu < 0):
        print("0'dan küçük not giremezsiniz !")
    elif (ders_notu > 100):
        print("100'den büyük not giremezsiniz !")
    else:
        print("Ders notunuz :",ders_notu)
 
except:
     print("Sadece not gireceksin, ne kadar zor olabilir ? ")
