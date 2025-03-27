def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]  

def fruit_game():
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]  
    print("Current fruit list:", fruits)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(fruits, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new fruit name: ").strip()
        print(modify_element(fruits, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(fruits, start, end))
    else:
        print("Invalid operation.")

fruit_game()
