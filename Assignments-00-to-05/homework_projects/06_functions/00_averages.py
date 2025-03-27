#Write a function that takes two numbers and finds the average between the two.

def find_average(num1, num2):
    return (num1 + num2) / 2

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("The average is:", find_average(a, b))

