masala_spices = ("cardamom", "cloves", "cinnamom")
(spice1, spice2, spice3) = masala_spices
print(f" Main masala spices: {spice1} {spice2} {spice3}")

ginger_ratio, cardamom_ratio = 2,1
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}")

#membership

print(f"Is Ginger is present in masala spices ? {'ginger' in masala_spices}")

##Output
# Main masala spices: cardamom cloves cinnamom
# Ratio is G: 2 and C: 1
# Ratio is G: 1 and C: 2
# Is Ginger is present in masala spices ? False