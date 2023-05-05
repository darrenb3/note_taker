import sqlite3


def delete_note():
    note_name = input(
        "\nPlease enter the name of the note you want to delete:\n")
    # Need to put error checking here that the record actually exists
    while True:
        confirmation = input(
            f"\nAre you sure that you want to delete {note_name}? This action is irreversible. (y/N):\n")
        if confirmation.lower() == "n":
            break
        elif confirmation.lower() == "y":
            con = sqlite3.connect("note_taker.db")
            cur = con.cursor()
            cur.execute("DELETE FROM notes WHERE name = ?", [note_name])
            con.commit()
            return True
        else:
            print("Please enter a valid confirmation.")
