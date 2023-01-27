# Categorize Box According to Criteria
# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.
# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.

def categorizeBox (length, width, height, mass) :
    bulky, heavy = False, False
    volume = length * width * height
    if (((length >= 10**4) or (width >= 10**4) or (height >= 10**4)) or (volume >= 10**9)) :
        bulky = True
    else :
        bulky = False
    if mass >= 100 :
        heavy = True
    else :
        heavy = False
    if bulky and heavy :
        return "Both"
    if bulky and not heavy :
        return "Bulky"
    if heavy and not bulky :
        return "Heavy"
    else :
        return "Neither"
print(categorizeBox(length = 2909, width = 3968, height = 3272, mass = 727))