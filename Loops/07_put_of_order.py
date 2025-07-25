flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} Item Found")
    
print(" Outside of loop")

##Output
# Ginger Item Found
# Lemon Item Found
#  Outside of loop