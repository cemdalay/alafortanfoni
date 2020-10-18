class Employee:
    """
    Personel sınıfı oluşturuyoruz.
    """
    FirstName = ""
    LastName = ""
    Phone = ""
    Mail = ""


emp = Employee()
emp.FirstName = "Cem"
emp.LastName = "Dalay"
emp.Phone = "+905312837775"
emp.Mail = "cemdalay@outlook.com"

print(emp.__doc__)
print(emp)  # <__main__.Employee object at 0x107a3c0a0>
# personel'i direkt olarak print metodunda yazarsanız size hesap alanındaki tuttuğu yerin adresini teslim eder.

print(emp.FirstName)
