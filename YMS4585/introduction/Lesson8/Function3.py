# Dışarıdan isim ve soyisim alan bir metot yazınız.
# Metot ilk parametredeki kelimenin ilk 2 harfini büyük,kalanını küçük alsın.
# 2. parametrenin ise, hepsini küçük alıp a harflerini e ile değiştirip bize @hotmail.com mail adresi olarak teslim etsin.




# def MailAdresi(isim,soyisim):
    
    
#     isim = isim.upper[0:2]
#     soyisim = soyisim.lower().replace("a","e")
#     mail_adresi = f"{isim}.{soyisim}@hotmail.com"
    
#     print(mail_adresi)

# isim = input("Lütfen bir isminizi giriniz:")
# soyisim = input("Lütfen soyadınızı giriniz : ")
# MailAdresi("cem","dalay")


def Mail(firstname,lastname):
    
    if len(firstname) <= 2: # girilen isim 2 veya daha az karakter ise
        firstname = firstname.upper()
    else:
        firstname = f"{firstname[0:2].upper()}{firstname[2:].lower()}"

    lastname = lastname.lower().replace("a","e")

    return f"{firstname}.{lastname}@hotmail.com"

isim = input("Lütfen bir isminizi giriniz:")
soyisim = input("Lütfen soyadınızı giriniz : ")

mail = Mail(isim,soyisim)
print(mail)