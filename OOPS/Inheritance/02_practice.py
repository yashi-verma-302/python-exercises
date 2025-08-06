class Person:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age, roll_number)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")

# Creating student objects
student1 = Student("Yashi", "22", "1101")
student2 = Student("Smit", "23", "1102")

# Displaying student info
student1.display_info()
print()
student2.display_info()