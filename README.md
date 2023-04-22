# Contacts-Database-App
This is a simple command line interface for a contact list program using Python and SQLite3. 

The program allows a user to add, update, delete, and view contacts. 

The program first checks if a database file 'contacts.db' exists. 
If it doesn't, then it creates the database file with a table named 'contacts' that stores a contact's first name, last name, phone number, and email address. 
If the database file already exists, then the program connects to it. 

The program offers four options: 
1. Add a contact: Prompts the user for a new contact's first name, last name, phone number, and email address. 
2. Update a contact: Prompts the user to enter a contact's name and presents the user with a menu of options to update that contact's information (first name, last name, phone number, or email address). 
3. Delete a contact: Prompts the user to enter a contact's name and then deletes that contact from the database. 
4. View all contacts: Displays all the contacts in the database. 

When the user exits the program, any changes made to the database are committed and the database connection is closed.
