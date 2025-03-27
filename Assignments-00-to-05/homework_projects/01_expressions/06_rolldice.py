#Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_dice():
    """Simulate rolling two dice and print the results."""
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    total = die1 + die2  
    
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

roll_dice()

