# .join() => parametrede verdiğiniz seperatör değerine göre, içine aldığı dizi içerisindeki elemanları o seperatör değerini araya ekleyerek,bir metin haline getirir.

# NOT : string bir char dizisidir

metin = input("Lütfen adınızı giriniz : ")
print(("-".join(metin)).replace("- -", " "))  # c-e-m d-a-l-a-y
