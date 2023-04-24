import os
import sqlite3

DATABASE_NAME = "contacts.db"

# Check if contacts.db exists
if not os.path.exists(DATABASE_NAME):
    # Create database file and table
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE contacts 
                 (id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  phone_number TEXT,
                  email TEXT)''')
    c.close()

# Connect to database
conn = sqlite3.connect(DATABASE_NAME)
c = conn.cursor()

def add_contact():
# Function to add contact to the database
    print("--------------------------------")
    print("Add a new contact...")
    print("--------------------------------")

    first_name = input("Enter contact's first name: ")
    while(not first_name.isalpha()): # Verify first name is alphabetic characters only
        print("Invalid input. First name should be letters only.")
        first_name = input("Enter contact's first name: ")

    last_name = input(f"Enter {first_name}'s last name: ")
    while(not last_name.isalpha()): # Verify last name is alphabetic characters only
        print("Invalid input. Last name should be letters only.")
        last_name = input(f"Enter {first_name}'s last name: ")

    phone_number = input("Enter {}'s phone number: ".format(first_name))
    while(not phone_number.isdigit()): # Verify phone number is digits only
        print("Invalid input. Phone numbers should be digits only.")
        phone_number = input("Enter {}'s phone number: ".format(first_name))

    email = input("Enter %s's email: " % first_name)
    while('@' not in email or '.' not in email): # Verify email address has both @ and . characters
        print("Invalid input. Email should have both an '@' and a '.'")
        email = input("Enter %s's email: " % first_name)

    # Perform SQL query to add the new contact into the database
    c.execute("INSERT INTO contacts (first_name, last_name, phone_number, email) VALUES (?,?,?,?)",
              (first_name, last_name, phone_number, email))
    
    # Print success message
    print("--------------------------------")
    print("Contact added successfully!")
    print("--------------------------------")

    # Commit the changes to connection database
    conn.commit()


def update_contact():
# Function to update a contact in the database
    print("--------------------------------")
    print("Update a contact...")
    print("--------------------------------")

    name = input("Enter contact's name: ")
    while(not name.isalpha()): # Verify name is alphabetic characters only
        print("Invalid input. Name should be letters only.")
        name = input("Enter contact's name: ")

    # SQL query for searching the name in contact database
    c.execute("SELECT * FROM contacts WHERE first_name LIKE ? or last_name LIKE ?", ('%' + name + '%', '%' + name + '%'))
    results = c.fetchall()

    if(len(results) == 0):
        print("No contact results found with that name: %s" % name)
    elif len(results) > 1:
        # If there are multiple results with that name, then prompt user to choose contact_id to update
        print("Multiple contact results found with that name: %s" % name)
        for row in results:
            print(row)
        contact_id = input("Enter contact ID to update(i.e. 1, 2, or 3): ")
    else:
        contact_id = results[0][0]

    # Present menu of options to update contact information
    while True:
        print("Select information to update:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone number")
        print("4. Email")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter new first name: ")
            while not first_name.isalpha():
                print("Invalid input. First name should be letters only.")
                first_name = input("Enter new first name: ")
            c.execute("UPDATE contacts SET first_name = ? WHERE id = ?", (first_name, contact_id))
        elif choice == "2":
            last_name = input("Enter new last name: ")
            while not last_name.isalpha():
                print("Invalid input. Last name should be letters only.")
                last_name = input("Enter new last name: ")
            c.execute("UPDATE contacts SET last_name = ? WHERE id = ?", (last_name, contact_id))
        elif choice == "3":
            phone_number = input("Enter new phone number: ")
            while not phone_number.isdigit():
                print("Invalid input. Phone numbers should be digits only.")
                phone_number = input("Enter new phone number: ")
            c.execute("UPDATE contacts SET phone_number = ? WHERE id = ?", (phone_number, contact_id))
        elif choice == "4":
            email = input("Enter new email: ")
            while not ('@' in email and '.' in email):
                print("Invalid input. Email should have both an '@' and a '.'")
                email = input("Enter new email: ")
            c.execute("UPDATE contacts SET email = ? WHERE id = ?", (email, contact_id))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    # Commit the changes to the database
    conn.commit()
    # Print success message
    print("Contact updated successfully!")


def delete_contact():
# Function to delete a contact from the database
    print("Delete a contact...")


def view_all_contacts():
# Function to view all contacts in the database
    print("View all contacts...")


def main():
    while True:
        print("Welcome to the contacts database app!")
        print("1.) Add a new contact")
        print("2.) Update an existing contact")
        print("3.) Delete a contact")
        print("4.) View all contacts")
        print("5.) Exit program")

        user_choice = input("Enter choice: ")

        if user_choice == "1":
            add_contact()
        elif user_choice == "2":
            update_contact()
        elif user_choice == "3":
            delete_contact()
        elif user_choice == "4":
            view_all_contacts()
        elif user_choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice: %s" % user_choice)
            print("Please try again!")


if __name__ == "__main__":
    main()