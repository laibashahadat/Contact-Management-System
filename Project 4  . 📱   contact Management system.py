contacts = []


#----------------------------
# Add contacts
#----------------------------

def add_contact():
    contact_name = input("Enter the contact name: ")
    contact_number = input("Enter the contact number: ")

    contacts.append({"name": contact_name, "number": contact_number})

    print("Contact added successfully")

#-----------------------------------
# Remove Contact Function
#-----------------------------------

def remove_contact():
    contact_name = input("Enter the name of the contact to remove: ")
    for contact in contacts:
        if contact["name"] == contact_name:
            contacts.remove(contact)
            print("Contact removed successfully")
            return
    print("Contact not found")

#-----------------------------------
#Show Contacts Function
#-----------------------------------
def show_contacts():
    if not contacts:
        print("No contacts found")
        return

    print("Contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Number: {contact['number']}")
#-----------------------------------
#Search Contact Function
#-----------------------------------
def search_contact():
    contact_name = input("Enter the name of the contact to search: ")
    for contact in contacts:
        if contact["name"] == contact_name:
            print(f"Contact found: Name: {contact['name']}, Number: {contact['number']}")
            return
    print("Contact not found")
#-----------------------------------
#Total Contacts Function
#-----------------------------------
def total_contacts():
    print(f"Total contacts: {len(contacts)}")
#===================================
#Main Program
#===================================
while True:

        
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Show Contacts")
        print("4. Search Contact")
        print("5. Total Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            remove_contact()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            total_contacts()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
