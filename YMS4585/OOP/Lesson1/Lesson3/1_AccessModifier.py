class Cup1:
    def __init__(self):

        self.color = None  # public variable
        self.content = None  # public variable

    def Fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return self.color + " " + self.content
        #return f"{self.color} {self.content}"


cup1 = Cup1()
cup1.color = "Guatemeala"
cup1.content = "Coffee"
print(cup1)

cup1.empty()
cup1.content = "Tea"
print(cup1)


class Cup2:
    def __init__(self):
        self.color = None  # public variable
        self._content = None  # protected variable

    def __str__(self):
        return f"{self.color} {self._content}"


cup2 = Cup2()
cup2.color = "Yellow"

# yanlış kullanım şeklidir.
cup2._content = "Tea"
# _ ile işaretlenmişse korumalı(protected) olarak işaretlenmiş anlamına gelir. kullanım gereği instance(örnek) aldıktan sonra değer ataması yapmanız gerekmektedir.Eğer dışarıdan değer ataması yapacaksanız constructor içerisinden gönderebilirsiniz
# _ bir alt tire ile işaretli ise protected anlamına gelir,ve bu değer sınıf üzerinden değil miras verilen sınıf üzerinden erişim sağlanır.
print(cup2)


class Cup3:
    def __init__(self):
        self._color = None  # Korumalı(protected) variable
        self.__content = None  # Gizli(private) variable

    def __str__(self):
        return f"{self._color} {self.__content}"


cup3 = Cup3()
cup3._color = "red"

print(cup3.__content)
# AttributeError: 'Cup3' object has no attribute '__content'
