class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number

    def display(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.roll_number}")

s1 = Student("Yashi", 22, "1101")
s1.display()