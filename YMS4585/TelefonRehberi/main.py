from Person import Person
from PersonService import *
import os


def Create():

    per = Person()
    per.Firstname = input("Lütfen Kişinin Adını Giriniz : ")
    per.Lastname = input("Lütfen Kişinin Soyadını Giriniz : ")
    per.Phone = input("Lütfen Kişinin Telefon Numarasını Giriniz : ")
    per.Mail = input("Lütfen Kişinin Mail Adresini Giriniz : ")
    return per


def Start():
    key = "y"
    while key != "e":
        print("Lütfen işlem seçiniz!\nKayıt Ekleme : a\nKayıt Silme : d\nKayıt Listesi : l\nKayıt Güncelle")
        key = input("İşlem : ").lower()

        if key == "a":
            person = Create()
            Add(person)
            os.system("Clear")
            print("Kayıt başarıyla eklendi!")
        elif key == "d":
            print("Lütfen _id değerini giriniz : ")
            id = input("_id : ")
            Delete(id)
            print("Kayıt başarıyla silindi!")
        elif key == "l":
            List()
        elif key == "u":
            id = input("_id : ")
            Update("")
            print("Kayıt başarıyla güncellendi")


Start()


# _id           Firstname       LastName        Phone       Mail
#-------------------------------------------------------------------

#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
#45454545       cem             dalay           645454      cemdlsls
