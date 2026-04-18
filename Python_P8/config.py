create_phonebook8_table = """
CREATE TABLE IF NOT EXISTS phonebook8 (
    id SERIAL PRIMARY KEY,
    user_name TEXT NOT NULL,
    phone_number VARCHAR(20)
);
"""

insert_contact = """
INSERT INTO phonebook8 (user_name, phone_number)
VALUES (%s, %s)
RETURNING id;
"""

get_all_contacts = "SELECT * FROM phonebook8 ORDER BY id ASC;"
get_contacts_by_name = "SELECT * FROM phonebook8 ORDER BY user_name ASC;"
get_contacts_by_number = "SELECT * FROM phonebook8 ORDER BY phone_number ASC;"

updating_contacts_name = """
UPDATE phonebook8
SET user_name = %s
WHERE phone_number = %s;
"""

updating_contacts_number = """
UPDATE phonebook8
SET phone_number = %s
WHERE user_name = %s;
"""

deleting_contacts = "DELETE FROM phonebook8"

deleting_contacts_by_name = "DELETE FROM phonebook8 WHERE user_name = %s"
deleting_contacts_by_number = "DELETE FROM phonebook8 WHERE phone_number = %s"
deleting_contacts_by_id = "DELETE FROM phonebook8 WHERE id = %s"

delete_all = "DROP TABLE phonebook8"

search_by_name = "SELECT * FROM phonebook WHERE user_name = %s"
search_by_phone = "SELECT * FROM phonebook WHERE phone_number = %s"
search_by_id = "SELECT * FROM phonebook WHERE id = %s"