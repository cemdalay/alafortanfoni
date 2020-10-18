class Calisan:
    def __init__(self, firstname, lastname, salary, department, age=18):
        self.Firstname = firstname
        self.Lastname = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age

    def __str__(self):
        return f"{self.Firstname} {self.Lastname} "

    def BilgiGoster(self):
        print("Çalışana ait bilgiler ekrana yazdırılıyor")
        print("-"*50, "\n")

        return f"Personelin Adı : {self.Firstname}\nPersonelin Soyadı : {self.Lastname}\nPersonelin Maaşı : {self.Salary}\nPersonelin Departmanı : {self.Department}\nPersonelin Yaşı : {self.Age}"
        # print("-"*50)

    def ZamYap(self, yapilanZam):
        print("Çalışanın maaşına zam yapıldı")
        maas = self.Salary
        self.Salary += yapilanZam
        print(
            f"{self}adlı personelin {maas} usd olan maaşı {self.Salary} usd olarak düzenlendi")

    def DegistirDep(self, yeni_dep):
        print("-"*50, "\n")
        print("Departman güncellenmesi...")
        departman = self.Department
        self.Department = yeni_dep
        #yeni_dep = "sales"
        print(f"{self}adlı personelin {departman} departmanından {yeni_dep} departmanına geçişi yapılmıştır.")
        print("-"*50)


# personel = Calisan("Cem", "Dalay", 1500, "eee", "90")
# print(personel)
# personel.BilgiGoster()
# personel.ZamYap(10000)
# print(personel.BilgiGoster())
# personel.DegistirDep("sales")
# print(personel.BilgiGoster())
