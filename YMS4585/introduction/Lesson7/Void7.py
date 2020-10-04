# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harflerin toplamını kullanıcıya bildiriniz.

def SesliKontrol(param):
    sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
    liste = list(param.lower())
    sesli = 0
    sessiz = 0
    for i in liste:
        if i in sesli_harfler:
            sesli += 1
        else:
            sessiz += 1

    print(f"Metin içerisinde yer alan, sesli harflerin toplam sayısı : {sesli}")
    
    print(f"Metin içerisinde yer alan,sessiz harflerin toplam sayısı : {sessiz}")
    


SesliKontrol("cemdalay")
        
