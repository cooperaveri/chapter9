import pickle
import os

# empty dictionary to store names and email addresses
contacts = {}

# check if the pickle file exists and load the dictionary if it does
if os.path.exists('contacts.pickle'):
    with open('contacts.pickle', 'rb') as file:
        contacts = pickle.load(file)

def display_menu():
    print("\nMenu:")
    print("1. Look up an email address")
    print("2. Add a new contact")
    print("3. Change an email address")
    print("4. Delete a contact")
    print("5. Exit")
    import pickle
import os

# empty dictionary to store names and email addresses
contacts = {}

# check if the pickle file exists and load the dictionary if it does
if os.path.exists('contacts.pickle'):
    with open('contacts.pickle', 'rb') as file:
        contacts = pickle.load(file)

def display_menu():
    print('\nMenu:')
    print('1. look up an email address')
    print('2. add a new contact')
    print('3. change an email address')
    print('4. delete a contact')
    print('5. exit')
    
def lookup_email():
    name = input('enter the name to look up: ')
   
    if name in contacts:
        print(f'Email Address: {contacts[name]}')
    else:
        print('name not found.')

# add contact
def add_contact():
    name = input('enter the name: ')
    email = input('enter the email address: ')
    contacts[name] = email
    print('contact added.[')

# change email
def change_email():
    name = input('enter the name to change email address: ')
    if name in contacts:
        email = input('enter the new email address: ')
        contacts[name] = email
        print('email address updated.')
    else:
        print('name not found.')

# delete contact
def delete_contact():
    name = input('enter the name to delete: ')
    if name in contacts:
        del contacts[name]
        print('contact deleted.')
    else:
        print('name not found.')

# main function to start execution
def main():
    while True:
        display_menu()
        choice = input('enter your choice (1/2/3/4/5): ')

        if choice == '1':
            lookup_email()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            change_email()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
      
       # save dictionary to a file and exit with open ('contacts.pickle', 'wb') as file: pickle.dump(contacts, file)
          print('contacts saved. exiting program.')
        
        break
    else:
         print('invalid choice. please select valid option')
         
if __name__ == '__main__':
    main()