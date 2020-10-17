
# 1 ile 10 arasındaki sayıları çarpım tablosu olarak ekrana yazdıran metot yazınız.


# format => 1x1 = 1
#--------------------
# 2x2 = 4
#---------------------
print("""
***********************************
*                                 *
*         ÇARPIM TABLOSU          *
*                                 *
***********************************
""")


def CarpimTablosu():

    for i in range(1, 10):
       print("*************************")
       for j in range(1, 10):
           print("{} x {} = {}".format(i, j, i*j))


CarpimTablosu()
