import os
os.system('clear')

word = "bilge adam"

for item in word:
    print(item)

print("-"*30)

for item in enumerate(word):
    print(item)
# (0, 'b')
# (1, 'i')
# (2, 'l')
# (3, 'g')
# (4, 'e')
# (5, ' ')
# (6, 'a')
# (7, 'd')
# (8, 'a')
# (9, 'm')

for (key,value) in enumerate(word):
    print("Sayı :",key)
    print("Karşı gelen değer :",value)
    print("\n")