class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print("-----------")
    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results
    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                print(f"Contact {contact.name} updated successfully.")
                return
        print(f"Contact with name {name} not found.")
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully.")
                return
        print(f"Contact with name {name} not found.")
def get_contact_details():
    name = input("Enter the name: ").strip()
    phone = input("Enter the phone number: ").strip()[:10]  
    return Contact(name, phone)
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            contact = get_contact_details()
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ").strip()
            results = contact_book.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for result in results:
                    print(f"Name: {result.name}")
                    print(f"Phone: {result.phone}")
                    print("-----------")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter the name of the contact to update: ").strip()
            new_phone = input("Enter the new phone number: ").strip()[:10]  
            contact_book.update_contact(name, new_phone)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ").strip()
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
