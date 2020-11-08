import pymongo
from bson import ObjectId
__DATABASE_NAME = "PhoneBookDB"
__COLLECTION_NAME = "People"


def ConnectAtlas():
    return pymongo.MongoClient("mongodb+srv://root:Zaqxswcde23@cluster0.stjuz.mongodb.net/PhoneBookDB?retryWrites=true&w=majority", ssl_cert_reqs='CERT_NONE')


def Add(person):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    myCollection.insert_one(person.__dict__)


def Delete(param):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    query = {"_id": ObjectId(param)}
    myCollection.delete_one(query)


def List():
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    print(f"{'_id':30}{'FirstName':30}{'LastName':30}{'Phone':30}{'Mail':30}")
    print("_"*150, "\n")

    for x in myCollection.find():
        body = ""
        for key, value in x.items():
            body += f"{str(value):30}"
        print(body)
    print("\n\n")


def Update(person):
    pass
