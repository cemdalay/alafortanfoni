import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')

myDb = myClient["Northwind"]
myCollection = myDb["Products"]

products = myCollection.find({})

for x in products:
    print(x)
