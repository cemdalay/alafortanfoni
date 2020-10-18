# from Helpers import *
# from Helpers import Clear, Mathlibrary
from Employee import EmployeeService
from Employee import Employee


from Helpers import Clear
from Helpers import MathLibrary

# _cls = Clear()
# _cls.ClearScreen()

Clear.ClearScreen("Clear")

result = MathLibrary.Topla("", 1, 2, 3, 4, 5, 6)
result1 = MathLibrary.Fark("", 5, 4, 3)
print(f"Toplam : {result} ")
print(f"Fark   : {result1} ")


mail = "CEM       dalay@outlook.com"

mail = Clear.ClearString(mail)
print(mail)


emp = Employee()
emp.FirstName = "CEM"
emp.LastName = "dalay"
emp.CreateMail()

print(emp.Mail)
