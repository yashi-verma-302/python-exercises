class Animal:
    def __init__(self,breed, age):
        self.breed = breed
        self.age = age

    def feature1(self):
        print(f"{self.breed} ")
        print(f"{self.age} ")

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(breed,age)
        self.name = name

    def feature1(self):
        super().feature1()
        print(f"{self.name}")

dog1 = Dog("Preeti", "10", "Lebra")
dog1.feature1()