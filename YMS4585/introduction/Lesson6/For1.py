sehirler = ["adana","urfa","bursa","antep","hatay"]

# i = 0 # index tanımlama
# while i < len(sehirler):
#     sehir = sehirler[i] #nesne tanıtma
#     print(sehir)

#     i+=1
# print("-"*50)

for sehir in sehirler:
    print(sehir)

print("-"*50)

print("-".join(sehirler)) # adana-urfa-bursa-antep-hatay
