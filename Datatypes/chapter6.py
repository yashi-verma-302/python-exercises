chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : chai type {chai_type}")

chai_description = "Aromatic and Bold"
print(f"Print first word: {chai_description[0:7]}")
print(f"Print word: {chai_description[0:6]}")

label_text="chai special"
encoded_label=label_text.encode("utf-8")
print(f" Non encoded: {label_text}")
print(f" Encoded label: {encoded_label}")

decoded_label=encoded_label.decode("utf-8")
print(f" Decoded label: {decoded_label}")

# OUTPUT
# Order for Priya : chai type Ginger Chai
# Print first word: Aromati
# Print word: Aromat
#  Non encoded: chai special
#  Encoded label: b'chai special'
#  Decoded label: chai special
