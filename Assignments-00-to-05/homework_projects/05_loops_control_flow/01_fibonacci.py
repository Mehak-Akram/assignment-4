#Write a program to print terms in the Fibonacci sequence up to a maximum value.

MAX_VALUE = 10000

def fibonacci_sequence(max_value):
    a, b = 0, 1
    while a < max_value:
        print(a)
        a, b = b, a + b

fibonacci_sequence(MAX_VALUE)
