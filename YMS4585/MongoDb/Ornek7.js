db.Categories.aggregate({ // ana tabloyu çağırmak

    $lookup: {
        from: "Products", // join yapılacak tablo
        localField: "_id", // ana tablo içerisinde yer alan pk(primary key)birincil anahtar.
        foreignField: "CategoryID", // foreignKey ikincil alan,ürünler tablosunda kategoriyi temsil eden alan
        as: "Products" // sorgu sonucu kategoriye bağlı ürünlerin listelenirken,verilecek olan isim,(opsiyonel dilediğiniz ismi verin elma,armut,vs)
    }


}).pretty()

db.Categories.aggregate({
    $lookup: {
        from: "Products",
        localField: "CategoryID",
        foreignField: "CategoryID",
        as: "Products"
    }
}).pretty()