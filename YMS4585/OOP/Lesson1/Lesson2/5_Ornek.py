import os
import socket
from datetime import datetime
# print(socket.gethostname())
os.system("Clear")
# print(socket.gethostbyname(socket.gethostname()))
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)


class CoreEntity():
    Id = 0

    def __init__(self):
        self.CreatedDate = datetime.now()
        self.CreatedComputerName = socket.gethostname()
        self.CreatedIP = socket.gethostbyname("")


class Category(CoreEntity):

    CategoryName = ""
    Description = ""


class Product(CoreEntity):
    ProductName = ""
    UnitPrice = 0
    UnitsInStock = 0


product = Product()
product.Id = 1
product.ProductName = "Beverages"
product.UnitPrice = 12
product.UnitsInStock = 100

category = Category()
category.Id = 1

print(product.ProductName)
print(category.CreatedDate)
