# içerisinde verilen parametreye göre soldan sağa doğru ayırma işlemi yapar


elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim,web grafik'
elemanlar = elemanlar.split(',')
#['yazılım', 'sistem', 'ofis', 'muhasebe', 'teknik çizim', 'web grafik']
print(elemanlar)

elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim,web grafik'
elemanlar = elemanlar.split()
#['yazılım,sistem,ofis,muhasebe,teknik', 'çizim,web', 'grafik']
# eğer parametre göndermezseniz,default olarak boşluklardan ayırma işlemi yapacaktır.
print(elemanlar)

metin = "cem dalay yazılım beşiktaş istanbul"

# birinci parametrede verdiğiniz seperatör değerine göre,2. parametrede verdiğiniz adet kadar ayırma işlemi yapacaktır.
sonuc = metin.split(" ", 3)
#['cem', 'dalay', 'yazılım', 'beşiktaş istanbul']
print(sonuc)

# text = "bilge,adam;beşiktaş.istanbul"

# a = 'Beautiful, is; better*than\nugly'
# a = re.split('; |, |\*|\n', a)
# print(a)
