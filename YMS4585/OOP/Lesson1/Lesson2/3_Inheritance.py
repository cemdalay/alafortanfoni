from Employee import Calisan
import os
os.system("Clear")


class Yonetici(Calisan):  # yönetici sınıfına çalışan sınıfına miras veriyoruz
    def __init__(self, firstname, lastname, salary, department, age=80, employeeCount=10):
        self.Firstname = firstname
        self.Lastname = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age
        self.EmployeeCount = int(employeeCount)

    def BilgiGoster(self):
        # super() miras aldığınız sınıfın değerini teslim eder.
        # Calisan sınıfının içerisindeki metodu çalıştırıp , gelen değeri teslim alıyoruz
        info = super().BilgiGoster()
        return f"{info}\nYöneticinin Toplam Çalışan Sayısı : {self.EmployeeCount}"

    def Print_Base(self):
        for base in self.__class__.__bases__:
            print("Bu sınıfın miras aldığı sınıf :", base.__name__)

    def __str__(self):
        info = super().__str__()
        return f"{info} Yöneticidir"


yonetici = Yonetici("Ahmet", "Şahin", 10000, "Yazılım")

info = yonetici.BilgiGoster()
print(info)
# yonetici.BilgiGoster()

# TypeError: __init__() missing 4 required positional arguments: 'firstname', 'lastname', 'salary', and 'department'

yonetici.Print_Base()
print(yonetici)
