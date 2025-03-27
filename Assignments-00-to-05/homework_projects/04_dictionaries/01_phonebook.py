# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def display_phonebook(phonebook):
    """Displays all contacts in the phonebook."""
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def add_contact(phonebook, name, number):
    """Adds a contact to the phonebook."""
    phonebook[name] = number
    print(f"Contact {name} added successfully.")

def remove_contact(phonebook, name):
    """Removes a contact from the phonebook."""
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} removed successfully.")
    else:
        print("Contact not found.")

def main():
    phonebook = {}
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Phonebook")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(phonebook, name, number)
        elif choice == '2':
            name = input("Enter name to remove: ")
            remove_contact(phonebook, name)
        elif choice == '3':
            display_phonebook(phonebook)
        elif choice == '4':
            print("Exiting phonebook application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
