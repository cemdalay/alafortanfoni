from Helpers import Clear


class Employee:

    FirstName = ""
    LastName = ""
    Mail = ""

    def CreateMail(self):
        self.Mail = Clear.ClearString(
            f"{self.FirstName}.{self.LastName}@outlook.com")


class EmployeeService:

    def IseAl(self):
        pass
