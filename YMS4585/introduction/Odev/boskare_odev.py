import os
os.system('cls')


column = int(input("Enter column size : "))
row = int(input("Enter row size : "))
print('* ' * column)
print(('* ' + "  " * (column-2) + '*'+'\n')*(row - 2) + ('* ' * column))
