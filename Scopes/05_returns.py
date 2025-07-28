def make_chai():
    return "Here is your masala chai"

return_value = make_chai()

print(return_value)

def sold_cups():
    return 120

total = sold_cups()
print(total)

def tea_status(cup_left):
    if cup_left == 0:
        return "Sorry, tea is over"
    return "Tea is ready"

print (tea_status(0))
print (tea_status(5))
