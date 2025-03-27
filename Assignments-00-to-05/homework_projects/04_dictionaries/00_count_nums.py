# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def count_numbers():
    counts = {}  
    
    while True:
        try:
            num = input("Enter a number (or press Enter to stop): ")
            if num == "":
                break  
            num = int(num)
            counts[num] = counts.get(num, 0) + 1  
        except ValueError:
            print("Please enter a valid number.")

    print("\nNumber frequencies:")
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

count_numbers()

