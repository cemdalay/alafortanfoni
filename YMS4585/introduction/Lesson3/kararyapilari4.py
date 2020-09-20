# Örnek : Dışarıdan girilen kelimenin uzunluğu, 8 karaktere eşit veya uzunsa,parola onaylandı,kısa ise,daha uzun bir şifre seçiniz uyarısı verdiriniz

sifre = len(input("Lütfen şifrenizi giriniz : "))

if sifre >= 8:
    print("Şifre onaylandı")
else:
    print("Daha uzun bir şifre giriniz")
           