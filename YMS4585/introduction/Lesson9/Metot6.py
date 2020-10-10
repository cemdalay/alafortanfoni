import os
#os.system("Clear")


def decorator_metot(func):
    def sarmal_metot():
        os.system("Clear")
        #print("sarmal metodu : {}'tan önce tetiklendi".format(metot.__name__))
        return func()
    return sarmal_metot


print("dasdadsasd")


@decorator_metot
def print_metot():
    print("print_metot tetiklendi")


print_metot()
