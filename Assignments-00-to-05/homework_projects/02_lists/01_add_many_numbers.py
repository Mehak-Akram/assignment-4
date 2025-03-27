# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_numbers(numbers):

    total = sum(numbers)
    return total


def main():
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        sum_of_numbers = add_numbers(numbers)
        print(f"The sum of the entered numbers is: {sum_of_numbers}")
    except ValueError:
        print("Invalid input! Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()