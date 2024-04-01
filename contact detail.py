class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

def display_menu():
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    address_book = AddressBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            address_book.add_contact(new_contact)

        elif choice == '2':
            address_book.view_contact_list()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = address_book.search_contact(search_term)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact you want to update: ")
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            address_book.update_contact(old_name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact you want to delete: ")
            address_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
