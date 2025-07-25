staff = [("Amit", 16), ("Zara", 29), ("Yashi", 22)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")