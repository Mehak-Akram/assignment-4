# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit.
# The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit of {num} is {ones_digit}")

def main():
    num = int(input("Enter an integer: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
