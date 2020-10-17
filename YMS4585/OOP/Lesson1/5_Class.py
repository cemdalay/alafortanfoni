import os
from datetime import datetime
from datetime import timedelta  # timedelta => tarihler arası zamanı hesaplar


class Employee:
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""
    # işe giriş tarihi sistem tarafından otomatik eklenecek.
    HireDate = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().hour}:{datetime.now().minute}"
    FireDays = 0
    Adress = ""

    def IseAl(self):
        fireDate = 0
        if(self.FireDays > 0):
            time = (datetime.now() + timedelta(days=self.FireDays))
            fireDate = f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute}"
        else:
            fireDate = "Gün sayısı belirtilmediğinden , çıkış tarihi hesaplanamadı"

        os.system("Clear")

        print("\n", "-"*50)
        print(
            f"Personelin Adı : {self.FirstName}\nPersonelin Soyadı : {self.LastName}\nPersonel Mail : {self.Mail}\nPersonel Telefon : {self.Phone}\nPersonelin Adresi : {self.Adress}\nPersonel İşe Giriş Tarihi :{self.HireDate}\nPersonelin Sözleşme Bitiş Tarihi : {fireDate}\nPesonelin işe girişi yapıldı")

        print("\n", "-"*50)

    def Update(self):
        # db içerisinden personeli güncelle
        pass

    def Fire(self):
        # personelin db içerisindeki durumunun değiştirilmesi.
        # 1 = Aktif , 2 = Pasif , 3 = Delete , 4 = Kovuldu , 5 = İşten Çıkarıldı
        pass


personel = Employee()
personel.FirstName = "Cem"
personel.LastName = "Dalay"
personel.Mail = "cemdalay@outlook.com"
personel.Phone = "+905312837775"
personel.Adress = "İstanbul / Ataşehir"
personel.FireDays = 120
personel.IseAl()
