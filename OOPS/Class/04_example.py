# Student Class with Result Check
# Create a class Student with name, roll_number, and marks.
# Add a method has_passed() that returns True if marks >= 40.

class Student:
    def __init__(self,name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def has_passed(self):
        return self.marks >=40

class_student = Student(name="Yashi", roll_number="01", marks=32)
print(class_student.has_passed())