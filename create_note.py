# contains all functions required to create a new note in the database
import sqlite3
from datetime import datetime


def new_note():
    name = input("\nPlease enter a name for your notel:\n")
    print("")
    content = input("\nPlease enter the content of your note:\n")
    print("")
    now = datetime.now().strftime('%H:%M:%S %m/%d/%Y')
    data = [name, now, content]
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    cur.execute("INSERT INTO notes VALUES(?,?,?)", data)
    con.commit()
    con.close()
    return True
