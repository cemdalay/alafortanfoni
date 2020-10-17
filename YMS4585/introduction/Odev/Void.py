
# 1 ile 10 arasındaki sayıları çarpım tablosu olarak ekrana yazdıran metot yazınız.


# format => 1x1 = 1
#--------------------
# 2x2 = 4
#---------------------

for i in range(1, 10):
    print("*************************")
    for k in range(1, 10):
        print("{} x {} = {}".format(k, i, i*k))
