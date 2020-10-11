# .startswith() => metninizin parametrede gönderdiğiniz değer ile başlayıp başlamadığını kontrol eder, true veya false olarak teslim eder.

metin = "bilge adam beşiktaş"
result = metin.startswith("bil")

print(result)

print(
    f"Parametrede gönderdiğiniz değer \"bil\" anahtar kelimesi ile başlama{'' if result else 'ma'}ktadır")
