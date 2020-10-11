# endswith() => metninizin parametrede gönderdiğiniz değer ile bitip bitmediğini kontrol eder.

metin = " bilge adam beşiktaş python dersleri"

sonuc = metin.endswith("dsad")

if sonuc:
    print("Parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmektedir")
else:
    print("Parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmemektedir")

# ternary if kullanarak tek satırda mesaj veriniz.


print("Parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmektedir" if sonuc else "Parametrede gönderdiğiniz değer 'eri' kelimesi ile bitmemektedir")


print(
    f"Parametrede gönderdiğiniz değer 'eri' kelimesi ile bitme{'' if sonuc else 'me'}ktedir")
