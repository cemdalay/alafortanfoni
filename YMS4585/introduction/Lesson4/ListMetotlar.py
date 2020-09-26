# dizi üzerinde işlemler yapmak için, o nesneye ait metotlar kullanılır.

# .append() => dizi içerisine eleman eklemek için kullanılıri (JavaScript içinde geçerlidir.)
# .append() => ekleme işlemini dizinin sonuna ekleyerek gerçekleştirir

sehirler = [] # boş dizi 
sehirler.append("ankara")
sehirler.append("edirne")
sehirler.append("istanbul")

print(sehirler)

#---------------------------------------------------------------

# .insert() => dizi içerisinde belirli bir alana veri eklemek için kullanılır.

sehirler.insert(1,"bursa")
# 1.Parametre dizinin hangi sırasına eleman eklenecek(index numarasını giriniz)
# 2.Parametre dizi içerisine eklenecek olan eleman

print(sehirler)

#---------------------------------------------------------------

# .pop() => dizi içerisinden eleman silme,parametre verilirse,verilen index değerindeki elemanı,parametre verilmezse , dizinin son elemanını siler.

print(sehirler)
sehirler.pop(1)
print(sehirler)
sehirler.pop()
print(sehirler)
print(sehirler.pop())

#---------------------------------------------------------------

arabalar = ["mercedes","bmw","range rover","bugatti","aston martin","tofaş","kartal","serçe"]

# .remove() => dizi içerisinden eleman silmekle mükellef diğer bir metodumuzdur, pop() metodundan farkı birisi index mekanizması üzerinden silme işlemi yaparken remove() object parametre alarak işleme devam eder.

# dizi içerisinde birden fazla aynı değer var ise, soldan sağa ilk bulduğu elemanı siler
# remove metodu, pop metodu gibi silinen elemanı geriye teslim etmez void metottur.

print(arabalar[:])
arabalar.remove("mercedes")
print(arabalar[:])

#---------------------------------------------------------------

# .sort() => dizi içerisinde bulunan elemanları A'dan Z'ye - 0'dan 9'a sıralar

# print(arabalar)
# arabalar.sort()
# print(arabalar[:])

#---------------------------------------------------------------

# .reverse() => dizi içerisindeki elemanları sıralamadan tersine çevirir.

print(arabalar[:])
arabalar.reverse()
print(arabalar)

#---------------------------------------------------------------

# .len() => dizinin uzunluğunu teslim eder.
print(len(arabalar))

del arabalar # sehirler dizisini tamamen silmiş olursunuz, bu satır derlendikten sonra, alt satırlarda arabalar dizisine ulaşamazsınız.

print(arabalar)
print(len(arabalar))
