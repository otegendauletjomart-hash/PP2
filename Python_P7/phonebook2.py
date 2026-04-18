import psycopg2
from psycopg2.extras import RealDictCursor, execute_batch
import csv
import config
import os 

connection = {
    "dbname": "DB1",
    "user": "daulet",
    "password": "12345678",
    "host": "127.0.0.1",
    "port": "5432"
}

def clear_screen():
    os.system('clear')

def csv_converter(file_csv):
    contacts = []
    with open(file_csv) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row:
                contacts.append(tuple(row))
    return contacts

def console_input():
        name = input("Name: ").strip()
        number = input("Number: ").strip()
        return name, number

def console_update_name():
    number = input("Enter the number of the contact to update the name: ").strip()
    new_name = input("New name: ").strip()
    return number, new_name

def console_update_number():
    name = input("Enter the name of the contact to update the number: ").strip()
    new_number = input("New number: ").strip()
    return name, new_number

def print_menu():
    print("\n" + "="*40)
    print("PHONEBOOK")
    print("="*40)
    print("1. Load contacts from CSV")
    print("2. Add contact")
    print("3. Update contact")
    print("4. Show all contacts")
    print("5. Delete contact")
    print("6. Exit")
    print("="*40)

def show_contacts(cur):
    cur.execute(config.get_all_contacts)
    data = cur.fetchall()
    if not data:
        print("No contacts found")
        return
    print("\nCONTACT LIST")
    for row in data:
        print(f"[{row['id']}] {row['user_name']} — {row['phone_number']}")


def main():
    try:
        with psycopg2.connect(**connection) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:

                while True:
                    clear_screen() 
                    print_menu()
                    choice = input("Choose an option: ").strip()

                    if choice == "1":
                        contacts = csv_converter('contacts.csv')
                        execute_batch(cur, config.insert_contact, contacts)
                        print("CSV loaded successfully")
                        input("Press Enter to continue...")

                    elif choice == "2":
                        name, number = console_input()
                        if name and number:
                            cur.execute(config.insert_contact, (name, number))
                            print("Contact added")
                        input("Press Enter to continue...")

                    elif choice == "3":
                        show_contacts(cur)
                        update_type = input("Update name or number? (name/number): ").lower()
                        if update_type == "name":
                            number, new_name = console_update_name()
                            cur.execute(config.updating_contacts_name, (new_name, number))
                            print("Name updated")
                        elif update_type == "number":
                            name, new_number = console_update_number()
                            cur.execute(config.updating_contacts_number, (new_number, name))
                            print("Number updated")
                        input("Press Enter to continue...")

                    elif choice == "4":
                        show_contacts(cur)
                        input("Press Enter to continue...")

                    elif choice == "5":
                        show_contacts(cur)
                        delete_type = input("Delete by name/number/id? ").lower()
                        value = input("Enter value to delete: ").strip()
                        if delete_type == "name":
                            cur.execute(config.deleting_contacts_by_name, (value,))
                        elif delete_type == "number":
                            cur.execute(config.deleting_contacts_by_number, (value,))
                        elif delete_type == "id":
                            cur.execute(config.deleting_contacts_by_id, (value,))
                        print("Contact deleted")
                        input("Press Enter to continue...")

                    elif choice == "6":
                        print("Exiting...")
                        break

                    else:
                        print("What?? Try again")
                        input("Press Enter to continue...")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()