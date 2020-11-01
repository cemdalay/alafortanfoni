// var olan bir database'i silme
// use <database ismi>
// db.dropDatabase()

// db içerisinde yer alan kayıtları listelemek için, öncelikle database'in seçilmiş olması gerekir.

// 1) Kayıtların listelenmesi
// 1.1) use Theaters

// 2) Koleksiyon içerisinde yer alan tüm kayıtların listelenmesi
// 2.1) db.Games.find() => tüm kayıtları listeler
// 2.1) db.Games.find().pretty() => düzgün formatta listeleme yapar

// 3) Koleksiyon içerisinde yer alan tüm kayıtların filtrelenerek listelenmesi
// 3.1) db.Games.find({"key":"value"})
// Ornek : db.Games.find({"Name":"AMANVERMEZ AVNİ"}).pretty()

// 4) Update işlemi,bir kaydın belirli bir alanı veya tüm kayıtların belirli alanların değiştirilmesi işlemi
//  4.1) db.Games.update({"key":"value"},{$set:{"key":"value"}})
//  1.süslü parantez içeriği
//      {key => filtreleme yaparken,neye göre yapacaksanız property adı : value => filtreleme yaparken verdiğiniz değer}
//  2.süslü parantez içeriği
//       {$set : => eşitle anlamına gelir {key => hangi alan değişecek : value => o alanın değeri nedir? }} 
// Ornek : db.Games.update({"Name" :"AMANVERMEZ AVNİ"})
db.Games.update(

    {
        "Name": "AMANVERMEZ AVNİ"
    },
    {
        $set: {
            "ImageUrl": "bilgeadam"
        }

    })
db.Games.find(
    {
        "Name": "AMANVERMEZ AVNİ"
    }
).pretty()

db.Games.update({ "Id": 1 }, { $set: { "ImageUrl": "bilgeadam" } })
db.Games.update({ "Id": 4 }, { $set: { "ImageUrl": "bilgeadam" } })
db.Games.update({ "Id": 180 }, { $set: { "ImageUrl": "bilgeadam" } })
db.Games.update({ "Id": 183 }, { $set: { "ImageUrl": "bilgeadam" } })

//db.Games.find({"Url":"www.bilgeadam.com"})

// db.Games.update("Id": "4")
// db.Games.update("Id": "1")
// db.Games.update("Id": "180")
// db.Games.update("Id": "183")

// Games içerisinde ImageUrl'i bilge adam olan tüö kayıtların Url kısmına www.bilgeadam.com

//db.Games.updateMany({ "ImageUrl": "bilgeadam" }, { $set: { "Url": "www.bilgeadam.com" } })

db.Games.update(
    {
        "ImageUrl": "bilgeadam"

    },
    {
        $set: {
            "Url": "www.bilgeadam.com"
        }
    },
    {
        multi: true
    }

)
//Veya

db.Games.updateMany(
    {
        "Url": "www.bilgeadam.com"

    },
    {
        $set: {
            "ImageUrl": "bilgeadam akademi"
        }
    }
)

db.Games.find({ "ImageUrl": "bilgeadam akademi" }).pretty()


// var games = db.Games.find() => oyun listesini değişkene atadık.
// games.hasNext() => true dönüyorsa içeride okunacak kayıt var anlamına gelir.

