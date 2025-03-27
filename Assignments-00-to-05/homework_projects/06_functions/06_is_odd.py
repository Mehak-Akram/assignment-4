import random

def even_odd_sequence(count, start=10, end=19):
    numbers = random.sample(range(start, end + 1), count)
    for num in sorted(numbers):  
        label = "even" if num % 2 == 0 else "odd"
        print(f"{num} {label}")

even_odd_sequence(10)
