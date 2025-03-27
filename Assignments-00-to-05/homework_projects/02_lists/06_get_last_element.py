#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.
# The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    """Prints the last element of the list."""
    print(f"The last element is: {lst[-1]}")

num_elements = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

get_last_element(user_list)
