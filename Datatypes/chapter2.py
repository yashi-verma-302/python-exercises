spice_mix=set()

print(f" Initial spice mix is: {spice_mix}")
print(f" Secondary spice mix is: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("lemon")
spice_mix.add("clove")
spice_mix.add("cardamom")

print(f" ID of spice mix: {id(spice_mix)}")
print(f" Name of spices added: {spice_mix}")

# OUTPUT
# Initial spice mix is: set()
#  Secondary spice mix is: set()
#  ID of spice mix: 2249456091872
#  Name of spices added: {'lemon', 'clove', 'cardamom', 'Ginger'}