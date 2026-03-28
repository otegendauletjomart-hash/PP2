create_phonebook_table = """
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    user_name TEXT NOT NULL,
    phone_number VARCHAR(20)
);
"""

insert_contact = """
INSERT INTO phonebook (user_name, phone_number)
VALUES (%s, %s)
RETURNING id;
"""

contacts_list = [
    ("S1mple", "+7 701 234 56 78"),
    ("Donk", "+7 705 987 65 43"),
    ("Deko", "+7 777 111 22 33"),
    ("Chopper", "+7 747 456 78 90")
]

get_all_contacts = "SELECT * FROM phonebook ORDER BY id ASC;"
get_contacts_by_name = "SELECT * FROM phonebook ORDER BY user_name ASC;"
get_contacts_by_number = "SELECT * FROM phonebook ORDER BY phone_number ASC;"

updating_contacts_name = """
UPDATE phonebook
SET user_name = %s
WHERE phone_number = %s;
"""

updating_contacts_number = """
UPDATE phonebook
SET phone_number = %s
WHERE user_name = %s;
"""

deleting_contacts = "DELETE FROM phonebook"

deleting_contacts_by_name = "DELETE FROM phonebook WHERE user_name = %s"
deleting_contacts_by_number = "DELETE FROM phonebook WHERE phone_number = %s"
deleting_contacts_by_id = "DELETE FROM phonebook WHERE id = %s"

delete_all = "DROP TABLE phonebook"