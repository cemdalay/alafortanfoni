# .strip() => metnin sağındaki ve solundaki boşlukları siler
import os
os.system("Clear")


metin = " bilge adam "
print(len(metin))  # 12

metin = metin.strip()
print(len(metin))  # 10


metin = "@bilgeadam@"

# metot içerisinde parametre verirseniz, gelen değer içerisindeki metnin başındaki ve sonundaki parametrede gelen değer var ise siler
print(metin.strip("@"))


metin = "@bilgeadam@"
print(metin.rstrip('@'))  # @bilgeadam
print(metin.lstrip('@'))  # bilgeadam@
