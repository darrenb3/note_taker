import sqlite3
from datetime import datetime


def update_note():
    note_name = input(
        "\nPlease enter the name of the note you want to update:\n")
    # Need to put error checking here that the record actually exists
    note_content = input("\nPlease enter the new content of the note:\n")
    now = now = datetime.now()
    data = [now, note_content, note_name]
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    cur.execute("UPDATE notes SET date = ?, string = ? WHERE name = ?", data)
    con.commit()
    con.close()
    return True
