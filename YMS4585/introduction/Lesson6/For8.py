import os
os.system('clear')

myList = ['a', 'b', 'c', 'd', 'e']

print(myList) #['a', 'b', 'c', 'd', 'e']

print(myList[:1]) #['a']
print(myList[1:3]) #['b', 'c']

newList = [x for x in 'word'] # word anahtar kelimesinin içinde dön her döndüğünde x anahtar kelimesine atar,word ü ayırır dizin elemanı olarak ekler.
print(newList) #['w', 'o', 'r', 'd']

liste = []
for x in "word":
    liste.append(x)
print(liste) #['w', 'o', 'r', 'd']