# sayısal loto, benzersiz, 6 adet sayı 8 kolon
import os
os.system('clear')

from random import randint

# print(random.randint(1,49))

counter = int(input("Lütfen kolon adedi giriniz : "))
index = 0 

while index < counter :
    sayilar = []
    i = 0
    while i < 6:
        sayi = str(randint(1,49))
        
        if sayi in sayilar :
                #i -= 1
            continue
        else:
            if(len(sayi) == 1):
                sayilar.append("0"+sayi)
            else:    
                sayilar.append(sayi)
        i += 1

    sayilar.sort()
    print(f"{index + 1}.kolon =","-".join(sayilar))
    index += 1
