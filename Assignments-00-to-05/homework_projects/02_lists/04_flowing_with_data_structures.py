def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

data = input("Enter a message to copy: ")

my_list = []
print("List before:", my_list)

add_three_copies(my_list, data)

print("List after:", my_list)
