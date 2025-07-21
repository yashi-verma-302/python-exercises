## Chai Price Calculator

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 5 rupees")
elif cup == "medium":
    print("Price is 10 rupees")
elif cup == "large":
    print("Price is 20 rupees")

else:
    print("Unknown")
    
##Output
# Choose your cup size (small/medium/large): small
# Price is 5 rupees
# Choose your cup size (small/medium/large): large
# Price is 20 rupees
# Choose your cup size (small/medium/large): extra large
# Unknown