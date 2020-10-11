# .splitlines() => her bir alt satırdaki elemanların aralarına [,] karakteri ekler
# NOT : METİN ALTTA YER ALAN ÖRNEK GİBİ YAZILDIYSA GEÇERLİDİR.

import os
os.system("Clear")


metin = """bilge
adam
beşiktaş
şubesi
python
dersleri
"""
# NOT => Parametre olarak True eklerseniz, her bir elemanın sonuna \n ekler.
print(metin.splitlines())
#['bilge', 'adam', 'beşiktaş', 'şubesi', 'python', 'dersleri']
print(metin.splitlines(True))
#['bilge\n', 'adam\n', 'beşiktaş\n', 'şubesi\n', 'python\n', 'dersleri\n']
print("".join(metin.splitlines(True)))
