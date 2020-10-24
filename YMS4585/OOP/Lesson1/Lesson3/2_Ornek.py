class BasePhone:
    def __init__(self):
        # protected variable
        self._phoneType = "Ahizeli Telefon"
        self.connectionType = None
        self.brand = None

    def __str__(self):
        return f"Telefonun Bağlantı Türü : {self.connectionType}\nTelefonun Markası : {self.brand}\nTelefonun Türü : {self._phoneType}"


basePhone = BasePhone()
basePhone.connectionType = "Kablolu Bağlantı"
basePhone.brand = "Alcatel"

print(basePhone)


class MobilPhone(BasePhone):
    def __init__(self):
        self.hasCamera = None
        self._phoneType = "Mobil Bağlantı"


mobil = MobilPhone()
mobil.hasCamera = True
mobil.brand = "Nokia"
mobil.connectionType = "Mobil Connection Available"


class SmartPhone(MobilPhone):

    def __init__(self):
        self.frontCam = None
        self._phoneType = "Smart Phone"


smartPhone = SmartPhone()
smartPhone.brand = "Apple"
smartPhone.connectionType = "5G"
smartPhone.frontCam = True
smartPhone.hasCamera = True
