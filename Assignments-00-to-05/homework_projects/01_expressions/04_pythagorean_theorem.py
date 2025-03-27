#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math

def calculate_hypotenuse(a, b):

    return math.sqrt(a**2 + b**2)

side_a = float(input("Enter the length of the first perpendicular side: "))
side_b = float(input("Enter the length of the second perpendicular side: "))

hypotenuse = calculate_hypotenuse(side_a, side_b)

print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
