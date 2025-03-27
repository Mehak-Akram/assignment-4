def count_even():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

count_even()


