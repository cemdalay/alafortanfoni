# .maketrans,.translate

# mail adresi düzenleyen metot yazdık

def ClearString(param):
    return param.lower().replace("ç", "c").replace("ş", "s")


print(ClearString("ahmetşahinç"))
