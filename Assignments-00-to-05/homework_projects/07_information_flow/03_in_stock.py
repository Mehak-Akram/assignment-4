

def num_in_stock(fruit):
    inventory = {
        "apple": 10,
        "banana": 5,
        "orange": 0,
        "grape": 7,
        "mango": 3
    }
    return inventory.get(fruit.lower(), 0)  

def main():
    fruit = input("Enter a fruit: ").strip()
    count = num_in_stock(fruit)
    
    if count > 0:
        print(f"There are {count} {fruit}(s) in stock.")
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
