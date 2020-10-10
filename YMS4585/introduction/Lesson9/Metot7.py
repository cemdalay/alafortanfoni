import os
os.system("Clear")


def Square(number):
    # result = number**2
    # return result

    return number**2


def SquareVol1(num): return num**2


result = SquareVol1(10)
print(result)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map => döngü mantığı ile dizi içerisindeki her bir eleman üzerinde işlem yapar
retVal = list(map(lambda num: num**2, my_numbers))
print(retVal)

# filter => oluşan result içerisinde verilen filtreye göre sonuç kümesinde filtreleme yapar
retBul = list(filter(lambda num: num % 2 == 0, my_numbers))
print(retBul)
