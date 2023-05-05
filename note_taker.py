# This is the driver code for the cli note recording app 2chi notes
from os.path import exists
import sqlite3
import create_note
import list_notes
import update_note
import delete_note


if __name__ == "__main__":
    print("Running the preflight check...")
    print("Checking for database...")
    db_present = exists("note_taker.db")
    if db_present == True:  # Checking if note_taker.db exits. If not creates db file and table
        print("Database present...")
        pass
    else:
        con = sqlite3.connect("note_taker.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE notes(name, date, string)")
        con.close()
        print("Database created...")
    print("Preflight complete!\n")
    print("\nWelcome to Note Taker!\n")
    while True:
        help_options = """\nTo enter a new note please type new
To list all notes please type list all
To list a single note please type list
To update a note please type update
To delete a note please type delete
To exit the app please type exit
"""
        user_input = input("\nPlease enter a command:\n")
        if user_input == "exit":
            print("\nThank you for using Note Taker\n\nExiting...\n")
            break
        elif user_input == "new":
            if create_note.new_note():
                print("\nNote created successfully\n")
        elif user_input == "list all":
            list_notes.list_all_notes()
        elif user_input == "list":
            list_notes.list_note()
        elif user_input == "update":
            if update_note.update_note():
                print("\nNote has been updated successfully\n")
        elif user_input == "delete":
            if delete_note.delete_note():
                print("\nThe note was successfully deleted\n")
            else:
                print("\nNo notes were deleted\n")
        else:
            print(help_options)
