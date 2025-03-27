#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def feet_to_inches(feet):
    """Convert feet to inches."""
    return feet * 12

feet = float(input("Enter feet: "))
inches = feet_to_inches(feet)

print(f"{feet} feet is equal to {inches} inches.")
