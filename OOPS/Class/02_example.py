# Create a Rectangle Class
# Define a class Rectangle with:
# attributes: length, width
# methods: area() and perimeter()
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width  = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
rect = Rectangle(5, 3)
print("Area:", rect.area())         # Output: 15
print("Perimeter:", rect.perimeter())  