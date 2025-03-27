# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. 
# Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy,
#  and then prints out the total combined cost of all of the fruits.
# Dictionary of fruit prices

fruit_prices = {
    "apple": 5.0,
    "durian": 20.0,
    "jackfruit": 15.0,
    "kiwi": 7.5,
    "rambutan": 10.0,
    "mango": 12.5
}

total_cost = 0

for fruit, price in fruit_prices.items():
    while True:
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
            if quantity < 0:
                print("Please enter a non-negative number.")
                continue
            total_cost += quantity * price
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Print total cost
print(f"\nYour total is ${total_cost:.2f}")
