ingredients =["water", "milk", "ginger"]
ingredients.append("sugar")
print(f" Ingredients of tea: {ingredients}")

## Used remove function
ingredients.remove("water")
print(f" Ingredients after remove: {ingredients}")

spice_options = ["ginger",  "sugar"]
chai_ingredients= ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f" chai ingredients will be: {chai_ingredients}")
chai_ingredients.insert(2, "blacktea")
print(f"chai ingredients: {chai_ingredients}")

##used pop function
last_added = chai_ingredients.pop()
print(f" Last added: {last_added}")

## used reverse function
chai_ingredients.reverse()
print(f" chai ingredients after reverse: {chai_ingredients}")

## using sort function
chai_ingredients.sort()
print(f" chai ingredients after sort: {chai_ingredients}")

##using max function
sugar_levels = [1,2,3,4,5]
print(f" Max sugar level: {max(sugar_levels)}")

##Output
# Ingredients of tea: ['water', 'milk', 'ginger', 'sugar']
#  Ingredients after remove: ['milk', 'ginger', 'sugar']
#  chai ingredients will be: ['water', 'milk', 'ginger', 'sugar']
# chai ingredients: ['water', 'milk', 'blacktea', 'ginger', 'sugar']
#  Last added: sugar
#  chai ingredients after reverse: ['ginger', 'blacktea', 'milk', 'water']
#  chai ingredients after sort: ['blacktea', 'ginger', 'milk', 'water']
#  Max sugar level: 5