# mantıksal operatörler

# and sorguya katılan her bir koşulun sağlanması durumu
# or sorguya katılan herhangi bir koşulun sağlanması durumu
# not sorguya olumsuzluk katar, değil ise

# username = input("Lütfen kullanıcı adınızı giriniz : ")
# if(username == "admin"):
#     password = input("Lütfen şifrenizi giriniz : ")
#     if password == "123456":
#         print("Giriş yaptınız")
#     else:
#         print("Kullanıcı bilgilerinizi kontrol ediniz.")    
# else:
#     print("Kullanıcı bilgilerinizi kontrol ediniz.")
    


username = input("Lütfen kullanıcı adınızı giriniz : ")
password = input("Lütfen kullanıcı şifrenizi giriniz : ")

if username == "admin" and password == "123" :
    print("Tebrikler giriş yaptınız")
else:
    print("Kullanıcı bilgilerinizi kontrol ediniz.")

# örnek : Fışarıdan kullanıcı not girişi sağlayacak
# 0 - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 - 100 => AA harf notunu aldığınız uyarısını veriniz.


not_girisi = int(input("Lütfen not girişini yapınız : "))

if not_girisi >= 0 and not_girisi <=30 :
    print("Notunuz : FF ")
elif not_girisi >= 31 and not_girisi <= 50:
    print("Notunuz : DD ")
elif not_girisi >= 51 and not_girisi <= 70:
    print("Notunuz : CC ")
elif not_girisi >= 71 and not_girisi <= 84:
    print("Notunuz : BB ")
elif not_girisi >= 85 and not_girisi <= 100:
    print("Notunuz : AA ")
else:
    print("Lütfen 0 ile 100 arasında bir not giriniz.")    

    

       
