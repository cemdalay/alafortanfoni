class Student:
    """
    self : Sınıf içerisinde yer alan metotların diğerlerinden farkı hangi sınıf içerisinden çalıştığını belirtmesidir.
           Self anahtar kelimesini vererek metodun bu sınıf içerinde çalıştığını belirtmiş oluruz.
           Tanımlama yapılırkn-en ekleniir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    """
    FirstName = ""

    def GiveNot(self, student):
        print(student, "Adlı öğrenciye not girişi yapıldı.")

    def GivePunish(self, student):
        print(student, "Adlı öğrenciye ceza verildi.")

    def Check(self, student):
        print(student, "Adlı öğrencinin yoklaması girildi")


student = Student()
student.FirstName = "Cem"

student.Check(student.FirstName)  # Cem Adlı öğrencinin yoklaması girildi

# cem dalay Adlı öğrencinin yoklaması girildi , not: boşluğu self komutu kullanıldığı için bıraktık.
Student.Check("", "cem dalay")
