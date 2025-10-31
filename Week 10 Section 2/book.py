# Written by Justice V.

from candy import Candy

class Book:
    def __init__(self):
        self.title = "Unknown"
        self.author = "Unknown"
        self.page_count = 0

    # Get and Set

    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author

    def get_page_count(self):
        return self.page_count
    def set_page_count(self, page_count):
        if 1 <= page_count < 1000:
            self.page_count = page_count

    

    # To String
    def __str__(self):
        return f"Book: {self.title} by {self.author} has {self.page_count} pages."
    
book1 = Book()
book1.set_title("The Great Gatsby")
book1.set_author("F. Scott Fitzgerald")
book1.set_page_count(180)

print(book1)

candy1 = Candy()
candy1.set_name("KitKat")
candy1.set_flavour("Chocolate")
candy1.set_shape("Rectangle")
candy1.set_size(10)
candy1.set_price(499.99)

print(candy1)