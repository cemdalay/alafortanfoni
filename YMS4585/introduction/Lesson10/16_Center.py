# .center() => parametrede verdiğiniz sayısal değeri, metnin sağına ve soluna eşit olarak dağıtır.(küsürat dahil değildir), boşluk ekleme

metin = "bilge adam"
print(len(metin))  # 10

metin = metin.center(20)
print(len(metin))
print("metin başı", metin, "metin sonu")
