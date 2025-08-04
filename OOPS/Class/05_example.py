# Create a Circle Class
# Define a class Circle with attribute radius.
# Add methods:
# area() (use 3.14 * radius * radius)
# circumference()

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

# Create an object of a class
cir_object = Circle(5)

calculate_area = cir_object.area()
print(f"Area: {calculate_area}")

calculate_circumference = cir_object.circumference()
print(f"Circumference: {calculate_circumference}")