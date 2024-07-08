class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()
    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, phone, email = line.strip().split(",")
                    self.contacts.append(Contact(name, phone, email))
        except FileNotFoundError:
            pass
    def save_contacts(self):
        with open(self.filename, "w") as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone},{contact.email}\n")
    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email address: ")
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
    def view_contacts(self):
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name} - {contact.phone} - {contact.email}")
    def edit_contact(self):
        self.view_contacts()
        contact_index = int(input("Enter the contact number to edit: ")) - 1
        contact = self.contacts[contact_index]
        print("Editing contact:", contact.name)
        contact.name = input("Enter new name (or press enter to keep current): ") or contact.name
        contact.phone = input("Enter new phone number (or press enter to keep current): ") or contact.phone
        contact.email = input("Enter new email address (or press enter to keep current): ") or contact.email
        self.save_contacts()
    def delete_contact(self):
        self.view_contacts()
        contact_index = int(input("Enter the contact number to delete: ")) - 1
        del self.contacts[contact_index]
        self.save_contacts()
def main():
    manager = ContactManager()
    while True:
        print("Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.edit_contact()
        elif choice == "4":
            manager.delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
