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
