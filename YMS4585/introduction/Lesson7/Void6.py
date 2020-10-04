# dışarıdan kullanıcının adını ve soyadını alan bir metot yazınız. metot aldığı bu değerleri kullanarak bize mail adresi oluştursun

def KullanıcıMail(isim, soyisim):

    mailadresi = f"{isim}.{soyisim}@outlook.com".lower()
    print(mailadresi)

def MailAdres(isim, soyisim=None):
    if soyisim is None:
        mail = f"{isim}@outlook.com"
    else:
        mail = f"{isim}.{soyisim}@outlook.com".lower()
    print(mail)
   

# adi = input("Lütfen adınızı giriniz : ")
# soyadi = input("Lütfen soyadınızı giriniz : ")

KullanıcıMail("cem","dalay")
MailAdres("cem")
