# Written by Justice V.

class Candy: 
    def __init__(self):
        self.name = "Unknown"
        self.flavour = "Unknown"
        self.shape = "Unknown"
        self.size = "Unknown"
        self.price = 0

    # Get and Set
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price
    def get_price_cad(self):
        return self.price * 1.4
    def set_price(self, price):
        if 0 <= price < 1000:
            self.price = price

    def get_flavour(self):
        return self.flavour
    def set_flavour(self, flavour):
        self.flavour = flavour

    def get_shape(self):
        return self.shape
    def set_shape(self, shape):
        self.shape = shape
    
    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size = size

    def reaction(self):
        if 0 < self.size < 5:
            return "Try again next time!0"
        elif 5 <= self.size < 10:
            return "Not bad!"
        else:
            return "Wow! That's amazing!"
    

    # To String
    def __str__(self):
        return f"Candy: {self.name}, its flavour is {self.flavour}, its shape is {self.shape}, its size is {self.size}, and it costs ${self.price} USD or ${self.price * 1.4} CAD"
    
BagOfCandies = []

candy1 = Candy()
candy1.set_name("KitKat")
candy1.set_flavour("Chocolate")
candy1.set_shape("Rectangle")
candy1.set_size(10)
candy1.set_price(499.99)

BagOfCandies.append(candy1)

print(candy1)
