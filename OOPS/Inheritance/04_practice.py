class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"{self.name} is the name of Employee")
        print(f"{self.salary} is the salary of Employee")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display_salary(self):
        print(f"{self.name} is the name of the Manager")
        total = self.salary + self.bonus
        print(f"Base Salary is {self.salary}")
        print(f"Bonus is {self.bonus}")
        print(f"Total is {total}")

m1 = Manager("Yashi", 50000000, 1000)
m1.display_salary()