# .index() , .rindex()

metin = "bilge adam beşiktaş şubesi pyton dersleri"


# parametreye verdiğiniz değerin,metin içerisinde yer alan index değerini teslim eder,
# metin içerisinde aynı karakter birden fazla içeriyorsa , ilk bulduğu değerin index numarasını,
# eğer parametrede gönderdiğiniz değer metin içerisinde geçmiyorusa size,(ValueError:substring not found)değer teslim eder.

result = metin.index("a")
print(result)

sonuc = metin.rindex("a")
print(sonuc)

# metin içerisinde parameterede gönderilen değerin,birden fazla olup olmadığını kullanıcıya mesaj olarak dönen bir mesaj yazınız.
# metot içeriye metin ve parametre alacak, geriye str mesaj dönecek.
