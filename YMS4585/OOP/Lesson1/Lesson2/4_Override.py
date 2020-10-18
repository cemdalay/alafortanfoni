class ParentClass():
    def send_message(self, message):
        print("ParentClass Mesaj Servisine Hoşgeldiniz :", message)


class BaseClass(ParentClass):
    def send_message(self, message):
        # override var olan bir nesneyi yeniden düzenlemek,aynı isimde, bu sınıf içerisinde tanımlamanız yeterlidir. eğer miras aldığınız sınıf içerisinden gelen değere de ihtiyacınız varsa,super()metodunu kullanarak o değeri elde edebilirsiniz.
        super().send_message("bir önceki sınıfın mesaj metodunu tetikledik")
        print(message)


parent = ParentClass()
parent.send_message("Parent sınıfı içerisindeki mesaj yazılmaktadır")


base = BaseClass()
base.send_message("Base sınıfından gönderilen mesaj")
