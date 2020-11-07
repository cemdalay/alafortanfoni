// db oluşturma
//use TelefonRehberi

db.Kisiler.insertMany([
    {
        "firstname": "cem",
        "lastname": "dalay"
    },
    {
        "firstname": "mehmet",
        "lastname": "şahin"
    }

])

/*
{
    "acknowledged" : true,
    "insertedIds" : [
        ObjectId("5fa6976ba3ac887722939176"),
        ObjectId("5fa6976ba3ac887722939177")
    ]
}

*/

db.Telefonlar.insertMany([
    {
        "name": "work",
        "number": "+905312837775",
        "personId": ObjectId("5fa6976ba3ac887722939176")
    },
    {
        "name": "home",
        "number": "+905312837795",
        "personId": ObjectId("5fa6976ba3ac887722939176")
    },
    {
        "name": "cell",
        "number": "+905312837785",
        "personId": ObjectId("5fa6976ba3ac887722939176")
    }
])

db.Kisiler.aggregate({

    $lookup: {
        from: "Telefonlar",
        localField: "_id",
        foreignField: "personId",
        as: "TelefonNumaralari"
    }

}).pretty()