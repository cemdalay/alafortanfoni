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
    
    telefon_rehberi =[
                        {

                            "isim" : "Cem",
                            "soyadı" : "Dalay",
                            "tel_no" : "+905312837775"

                        }


    ]
    
    i = 0
    islem_numarası = 0
    
    
    print("""
    Ana Menü için 0'a basınız
    Kayıt Eklemek için 1'e basınız
    Kayıt Düzenlemek için 2'ye basınız
    Kayıt Silmek için 3'e basınız
    Kayıt Listesi için 4'e basınız
    Aramayapmak için 5'e basınız
    """)
    
    islem_numarası = [0,1,2,3,4,5]
    islem_numarası = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz : "))
    isim = []
    soyadı = []
    tel_no = []
    
    while i < islem_numarası :    
            
        if islem_numarası == 0 :
            print("""
            Ana Menü için 0'a basınız
            Kayıt Eklemek için 1'e basınız
            Kayıt Düzenlemek için 2'ye basınız
            Kayıt Silmek için 3'e basınız
            Kayıt Listesi için 4'e basınız
            Arama yapmak için 5'e basınız
            """)
         
        elif islem_numarası == 1 :
                
            isim = input("Lütfen kaydetmek istediğiniz ismi giriniz :")
            soyadı = input("Lütfen kaydetmek istediğiniz soyadını giriniz : ")
            tel_no = input("Lütfen kaydetmek istediğiniz telefon numaranısını giriniz : ")

            print(f"""
            Adı                 : {isim}
            Soyadı              : {soyadı}
            Mail Adresi         : {isim}{soyadı}@cdcable.com
            Telefon Numarası    : {tel_no}
             """)
            islem_sonucu = str(input("Kayıt ekleme işlemine devam etmek ister misiniz ?\nDevam etmek için E'ye,Ana Menüye dönmek için O'a basınız."))
            if islem_sonucu == "0" :
                print("""
            Ana Menü için 0'a basınız
            Kayıt Eklemek için 1'e basınız
            Kayıt Düzenlemek için 2'ye basınız
            Kayıt Silmek için 3'e basınız
            Kayıt Listesi için 4'e basınız
            Arama yapmak için 5'e basınız
            """)
            else:
                islem_numarası = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz : "))
                break
                


                
        elif islem_numarası == 2: 
                
                # isim = input("Lütfen düzenlemek istediğiniz ismi giriniz :")
                # soyadı = input("Lütfen kaydetmek istediğiniz soyadını giriniz : ")
                # tel_no = input("Lütfen kaydetmek istediğiniz telefon numaranısını giriniz : ")
                
            isim.append(isim)
            soyadı.append(soyadı)
            tel_no.append(tel_no)
                
            print(f"""
            Adı                 : {isim}
            Soyadı              : {soyadı}
            Mail Adresi         : {isim}{soyadı}@cdcable.com
            Telefon Numarası    : {tel_no}

            """)
        continue  
            
            
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    i += 1

except Exception as mahmud:
    print(mahmud)