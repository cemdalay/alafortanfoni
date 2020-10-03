# 1000(dahil) ile 1 arasındaki sayıları ekrana yazdırınız.

def SayilarWhile():
    i = 1000
    while(i>=1):
        print(i)
        i -= 1
SayilarWhile()

def SayilarFor():
    for sayi in range(1000,0,-1):
        print(sayi)

SayilarFor()