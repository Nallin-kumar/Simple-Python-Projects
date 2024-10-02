# Initialize an empty contact book
contact_book = {}

def add_contact(name, phone):
    """Add a new contact to the contact book."""
    contact_book[name] = phone
    print(f"Contact {name} added successfully.")

def view_contacts():
    """Display all contacts in the contact book."""
    if not contact_book:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")

def search_contact(name):
    """Search for a contact by name."""
    if name in contact_book:
        print(f"{name}: {contact_book[name]}")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book application
main()

