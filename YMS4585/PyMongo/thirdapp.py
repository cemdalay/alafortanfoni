import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
myDb = myClient["PhoneBook"]
people = myDb["People"]
phones = myDb["Phones"]


person = {
    "firstname": "murat",
    "lastname": "vuranok",
    "phone": "+9013234548",
    "mail": "murat.vuranok@bilgeadam.com"
}
#myCollection.insert_one(person)

# kaydı ekledikten sonra objectID değerini teslim eder.
kisi_id = people.insert_one(person).inserted_id

phone_numbers = [
    {
        "name": "work",
        "phone": "+9754545454545",
        "personId": kisi_id
    },
    {
        "name": "work",
        "phone": "+9754545454545",
        "personId": kisi_id
    },
    {
        "name": "work",
        "phone": "+9754545454545",
        "personId": kisi_id
    }

]
phones.insert_many(phone_numbers)


for p in people.find():
    print("_"*40)
    print()
    for x, y in p.items():
        print(f"{x}:{y}")
        telefon_numaralari = phones.find({"personId":  p["_id"]})
        for t in telefon_numaralari:
            print()
            for c, d in t.items():
                print(f"{c}:{d}")
    print("_"*40)
