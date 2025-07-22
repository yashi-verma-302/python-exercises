black_tea_grams=14
ginger_grams=3

total_grams = black_tea_grams + ginger_grams
print(f" Total grams: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f" Reamining tea: {remaining_tea}")

milk_litres=7
servings=4
milk_per_serving= milk_litres / servings
print(f" milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots =4
bags_per_pot = total_tea_bags // pots
print(f" Total tea bags: {bags_per_pot}")

total_cardomom_pods =10
pods_per_cup = 7
left_over_pods = total_cardomom_pods % pods_per_cup
print(f" total leftover pods: {left_over_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f" powerful flavour: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f" total tea harvested: {total_tea_leaves_harvested}")

# OUTPUT 
# Total grams: 17
#  Reamining tea: 11
#  milk per serving: 1.75
#  Total tea bags: 1
#  total leftover pods: 3
#  powerful flavour: 8
#  total tea harvested: 1000000000