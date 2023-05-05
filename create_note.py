# contains all functions required to create a new note in the database
import sqlite3
from datetime import datetime


def new_note():
    name = input("Please enter a name for your name:\n")
    print("")
    content = input("Please enter the content of your note:\n")
    print("")
    now = datetime.now()
    data = [name,now,content]
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    cur.execute("INSERT INTO notes VALUES(?,?,?)", data)
    con.commit()
    con.close()
    return True
