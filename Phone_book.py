#Phone book
phone_book = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phone_book[name] = number
    print(f"Contact {name} added successfully.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in phone_book:
        print(f"Name: {name}, Number: {phone_book[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if not phone_book:
        print("Phone book is empty.")
    else:
        print("Contacts in the phone book:")
        for name, number in phone_book.items():
            print(f"Name: {name}, Number: {number}")


while True:
    print("Simple Phone Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")