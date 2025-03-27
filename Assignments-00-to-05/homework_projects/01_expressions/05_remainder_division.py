#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division

def divide_numbers():
    """Ask the user for two numbers and perform division with remainder."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        quotient = num1 // num2  
        remainder = num1 % num2  

        print(f"Quotient: {quotient}")
        print(f"Remainder: {remainder}")

divide_numbers()

