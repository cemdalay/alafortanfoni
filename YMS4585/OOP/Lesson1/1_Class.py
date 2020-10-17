import os
os.system("Clear")

# Class tanımlaması :


class Employee:
    """
    FirstName : Kişinin Adı
    LastName  : Kişinin Soyadı
    Phone     : Kişinin Telefonu
    Mail      : Kişinin Mail Adresi
    """

# tanımlanan class'ın instance(yeni bir örnek) alma işlemi


employee = Employee()

# __doc__ => class içerisinde eğer açıklama yazdıysanız size outputta o açıklamayı teslim eder
print(employee.__doc__)
