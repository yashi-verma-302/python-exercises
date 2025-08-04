#  Create a Book Class
# Create a class Book with attributes: title, author, and price.
# Add a method display_info() that prints all the attributes.

class Book:
    
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        
book1 = Book("Atomic Habits", "James Clear", 399)
book1.display_info()