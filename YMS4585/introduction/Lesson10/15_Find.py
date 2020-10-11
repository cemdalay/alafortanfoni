# .finde(), r.find() => aradığınız eleman index değerini teslim eder, eğer dizi veya metin içerisinde aradığınız değer birden fazla ise, .find() ilk bulduğu elemanı,
# rfind() son bulduğu elemanı teslim eder. dizi içerisinde eğer aradığınız eleman yok ise, size -1 değerini teslim eder

# index metot ile çalışma prensibi aynıdır fark => index ValueError verirken , find metodu -1 değerini teslim eder,parametredeki eleman içermiyorsa

metin = "bilge adam beşiktaş şubesi"

result = metin.find("a")
print(result)

result = metin.rfind("a")
print(result)

result = metin.find("x")
print(result)

result = metin.rfind("x")
print(result)
