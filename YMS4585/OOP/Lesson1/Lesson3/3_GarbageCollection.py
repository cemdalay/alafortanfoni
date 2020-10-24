a = 40  # değeri 40 olan sayısal bir değişken tanımladık
print(type(a))  # <class 'int'>

b = a  # b adında bir değişken tanımladık refeansını a değişkeninden almasını sağladık

c = [b]  # c değişkenini tanımlayıp b değerini eleman olarak atadık

print(type(c))  # <class 'list'>

del a  # a değişkenini ram üzerinden sildik
# print(a) #NameError: name 'a' is not defined
print(b)  # 40 => a içerisinde yer alan veriyi b adındaki değişkene kopyaladığımızdan , ram üzerindeki b değişkeni için yeni bir alan oluşmuş olur o yüzden a değerini silsenizde,b üzerindeki veriyi tutmaya devam eder.
b = 100  # b değişkenin değerini 100 olarak değiştirdik
print(b)


class Point:
    # eğer sınıf tanımlaması yapılırken değer verilmezse constructor'a default değeri 0'dır.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "heap alan üzerinden silindi")


point1 = Point()
point2 = point1
point3 = point1

# nesnelerin ram üzerindeki adresini ekrana yazdırma
print(id(point1), id(point2), id(point3))
# 4400254928
# 4400254928
# 4400254928

c = 10  # c değişkeninin ram üzerindeki adresi => 4502838240
# c değişkenini y değişkenine referans olarak verdiğimizden üzerindeki sayısal tutuğu değer ve referans adresini teslim eder.
y = c
# c=> 4502838240
# y => 4502838240
print(id(c), id(y))

# y değişkenine yeni bir değer atandığından dolayı ram üzerinde yeni bir referans adresi oluşur.
y = 100

print(id(y))
# y => 4323084064

del point1
del point2
del point3
