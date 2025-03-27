# Print 10 random numbers in the range 1 to 100.


import random

def print_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(" ".join(map(str, numbers)))

print_random_numbers()


