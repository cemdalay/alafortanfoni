import os
os.system("Clear")


file1 = "ba.png"
file2 = "ba.jpg"
file3 = "ba.gif"
file4 = "ba.png"
file5 = "ba.tff"
file6 = "ba.mp3"
file7 = "ba.mp4"
file8 = "ba.jpg"
file9 = "ba.gif"
file10 = "ba.png"
file11 = "ba.gif"

# yukarıda yer alan dosyalar içerisinde .png olanların sayısını ekrana yazdırınız


toplam = list(filter(lambda x: "png" in x, (

    file1,
    file2,
    file3,
    file4,
    file5,
    file6,
    file7,
    file8,
    file9,
    file10,
    file11,
)))

print(len(toplam))


def Kontrol(*param):
    count = 0
    for i in param:
        retVal = i.endswith(".png")
        if retVal:
            count += 1
        return count


result = Kontrol(
    file1,
    file2,
    file3,
    file4,
    file5,
    file6,
    file7,
    file8,
    file9,
    file10,
    file11)
print(result)


# def Kontrols(**param):
#     count = 0
#     for key, value in param.items()
#     retVal = value.endswith("png")
#     if retVal:
#         count += 1
#     return count


# results = Kontrols(
#     file1="ba.png",
#     file2="ba.jpg",
#     file3="ba.gif",
#     file4="ba.png",
#     file5="ba.tff",
#     file6="ba.mp3",
#     file7="ba.mp4",
#     file8="ba.jpg",
#     file9="ba.gif",
#     file10="ba.png",
#     file11="ba.gif"

# )
# print(len(results))
