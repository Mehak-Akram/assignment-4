# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def fahrenheit_to_celsius():

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit}F = {celsius}C")

fahrenheit_to_celsius()
