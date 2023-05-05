# This is the driver code for the cli note recording app 2chi notes
from os.path import exists
import sqlite3
import create_note
import list_notes


if __name__ == "__main__":
    print("Running the preflight check...")
    print("Checking for database...")
    db_present = exists("note_taker.db")
    if db_present == True:  # Checking if 2chi_notes.db exits. If not creates db file and table
        pass
    else:
        con = sqlite3.connect("note_taker.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE notes(name, date, string)")
        con.close()
        print("Database created...")
    print("Preflight complete\n")
    print("Welcome to Note Taker!\n")
    while True:
        help_options = """To enter a new note please type new
To list all notes please type list all
To list a single note please type list
To exit the app please type exit
"""
        print("Please enter a command:")
        user_input = input()
        if user_input == "exit":
            break
        elif user_input == "new":
            if create_note.new_note():
                print("Note created successfully\n")
        elif user_input == "list all":
            list_notes.list_all_notes()
        elif user_input == "list":
            list_notes.list_note()
        else:
            print(help_options)
