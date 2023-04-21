def add_contact():
# Function to add contact to the database
    print('Add a new contact...')

def update_contact():
# Function to update a contact to the database
    print('Update a contact...')

def delete_contact():
# Function to delete a contact to the database
    print('Delete a contact...')

def view_all_contacts():
# Function to view all contacts to the database
    print('View all contacts...')

def main():
    while True:
        print("Welcome to the contacts database!")
        print("1.) Add a new contact")
        print("2.) Update an existing contact")
        print("3.) Delete a contact")
        print("4.) View all contacts")
        print("5.) Exit program")

        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            update_contact()
        elif user_choice == 3:
            delete_contact()
        elif user_choice == 4:
            view_all_contacts()
        elif user_choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice: %d" % user_choice)
            print("Please try again!")


if __name__ == "__main__":
    main()