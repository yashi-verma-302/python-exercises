# Laptop Class with Discount
# Create a class Laptop with attributes brand, price, ram.
# Add method apply_discount(percent) that reduces price by given percent.

class Laptop:
    def __init__(self, brand, price, ram):
        self.brand = brand
        self.price = price
        self.ram = ram

    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount

laptop1 = Laptop("HP", 50000, "8GB")
laptop1.apply_discount(10)
print(laptop1.price)

class Mobile:
    def __init__(self, brand, price, ram):
        self.brand = brand
        self.price = price
        self.ram = ram

    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount

mobile1 = Mobile("OnePlus", 50000, "8GB")
mobile1.apply_discount(20)
print(mobile1.price)