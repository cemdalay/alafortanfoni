# Dışarıdan aldığı değere göre içi dolu kare çiziniz.

# x x x x x x 
# x x x x x x 
# x x x x x x 
# x x x x x x 
# x x x x x x 
# x x x x x x  

def KareCizVol1(armut):
    index = 0
    while index <= armut:
        metin = ""
        for i in range(armut):
            metin += "X "
        print(metin)
        index += 1

KareCizVol1(5)

def KareCizVol2(x):
    index = 0 
    while index < x:
        print("X "*x)
        index += 1

KareCizVol2(7)

def KareCizVol3(x):
    for i in range(x):
        print("-"*x)
KareCizVol3(4)

def BosKareCiz(x):
    index = 0
    while index <= x:
        metin = ""
        for i in range(x):
            metin += "| "
        print(metin)
        index += 1
BosKareCiz(5)
    