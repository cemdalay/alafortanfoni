# kullanıcı dışarıdan şifre girecek girilen şifre 3 ile 8 karakter aralığında ise şifreniz : şifre olarak onaylandı.

# abc123 => şifreniz :abc123 olarak onaylandı

# kullanıcı 3 kere yanlış girdikten sonra, motive edici bir mesaj veriniz.

print("*Gireceğiniz şifre 3 ile 8 karakter aralığında olmalıdır*")


for i in range(3):
    sifre = input("Lütfen şifrenizi giriniz : ")
    if i == 2:
        print("Şifrenizi 3 kere yanlış girdiniz,bravo")  
    elif len(sifre) >= 3 and len(sifre) <= 8:
        print(f"Şifreniz : {sifre}, onaylanmıştır.")
    elif len(sifre) not in range(3,8):
        print("*Gireceğiniz şifre 3 ile 8 karakter aralığında olmalıdır*")       
    else:
        print("Başarısız")
        break
        
