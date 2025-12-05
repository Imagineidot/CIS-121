# Written by Justice V.

class Product:
    def _init__(self):
        self.name = "Unknowkn"
        self.price = 0
        self.quantity = 0

    # Get and Set
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price
    def set_price(self, price):
        if 0 <= price < 10000:
            self.price = price
    
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        if 0 <= quantity < 1000:
            self.quantity = quantity

    # To String
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"
    
BagOfProducts = []

product1 = Product()
product1.set_name("Pokemon Elite Trainer Box")
product1.set_price(49.99)
product1.set_quantity(20)

BagOfProducts.append(product1)

product2 = Product()
product2.set_name("Magic The Gathering Booster Box")
product2.set_price(89.99)  
product2.set_quantity(15)

BagOfProducts.append(product2)

print(product1)
print(product2)
print(BagOfProducts)