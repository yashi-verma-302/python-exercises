class Employee:
    pass

class Manager:
    pass

# Print the type of the class itself
print(type(Employee))  # <class 'type'>

# Create an instance of Employee
employee_instance = Employee()

# Print the type of the instance
print(type(employee_instance))  # <class '__main__.Employee'>

# Check if the type of the instance is exactly the Employee class
print(type(employee_instance) is Employee)  # True

# Check if the type of the instance is exactly the Manager class
print(type(employee_instance) is Manager)  # False


##Output
# <class 'type'>
# <class '__main__.Employee'>
# True
# False