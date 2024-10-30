class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        """Add a new contact with name, phone, email, and address."""
        if phone in self.contacts:
            print("A contact with this phone number already exists.")
        else:
            self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """Display all contacts with name and phone number."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for phone, details in self.contacts.items():
                print(f"Name: {details['Name']}, Phone: {phone}")

    def search_contact(self, query):
        """Search for a contact by name or phone number."""
        found = False
        for phone, details in self.contacts.items():
            if query.lower() in details["Name"].lower() or query == phone:
                print(f"Found: {details['Name']}, Phone: {phone}, Email: {details['Email']}, Address: {details['Address']}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, phone):
        """Update contact details by phone number."""
        if phone in self.contacts:
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
            print(f"Contact with phone {phone} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, phone):
        """Delete a contact by phone number."""
        if phone in self.contacts:
            del self.contacts[phone]
            print(f"Contact with phone {phone} deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)

        elif choice == '4':
            phone = input("Enter phone number of the contact to update: ")
            contact_manager.update_contact(phone)

        elif choice == '5':
            phone = input("Enter phone number of the contact to delete: ")
            contact_manager.delete_contact(phone)

        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
