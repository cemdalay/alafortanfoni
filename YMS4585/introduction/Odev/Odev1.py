# Telefon Rehberi

# Kullanıcı uygulamayı çalıştırdığında , seçenekler sunulacak

############### Telefon Rehberi ###############
# Kayıt Eklemek için 1
# Kayıt Düzenlemek İçin 2
# Kayıt Silmek İçin 3
# Kayıt Listesi İçin 4
# Arama İçin 5
# Lütfen bir değer giriniz :

# Adı               : murat
# Soyadı            : vuranok
# Mail Adresi       : murat.vuranok@bilgeadam.com
# Telefon Numarası  : 354446465 

# Yeni bir işlem yapmak istiyor musunuz (Y/N) :
###############################################
print("""
###############################################
#                                             # 
#                                             # 
#             Telefon Rehberi                 #
#                                             #
#                                             #
#                                             #
###############################################
""")

try:
    
    telefon_rehberi = ["kayıt ekleme","kayıt düzenleme","kayıt silme","kayıt listesi","arama"]
    
    
    kayit_ekleme = int(input("Kayıt eklemek için 1'e basınız : "))
    
    if kayit_ekleme == 1 :
        isim = input("Lütfen kaydetmek istediğiniz ismi giriniz :")
        soyadı = input("Lütfen kaydetmek istediğiniz soyadını giriniz : ")
        tel_no = input("Lütfen kaydetmek istediğiniz telefon numaranısını giriniz : ")

        print(f"""
        Adı                 : {isim}
        Soyadı              : {soyadı}
        Mail Adresi         : {isim}{soyadı}@cdcable.com
        Telefon Numarası    : {tel_no}

        """)
       
    else:
        print("Yapmak istediğiniz işlem bulunmamaktadır.")    
    
    
    
    # kayit_düzenleme = "Kayıt Düzenlemek için 2"
    # kayit_silmek = "Kayıt Silmek için 3"
    # kayit_listesi = "Kayıt Listesi için 4"
    # arama = "Aramayapmak için 5"

    # numaralar = ["1","2","3","4","5"]























except Exception as mahmud:
    print(mahmud)
