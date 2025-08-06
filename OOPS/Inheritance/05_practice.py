class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        super().start()
        print("Driving")

my_car = Car()
my_car.drive()
my_car.start()