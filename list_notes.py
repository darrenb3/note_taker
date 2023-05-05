# Contains all fucntions for listing notes
import sqlite3

def list_all_notes():
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    for row in cur.execute("SELECT name, date, string FROM notes"):
        print(row)
    con.close()

def list_note():
    user_input = input("Please enter the name of the note you want to read:\n")
    print("")
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    row = cur.execute("SELECT name, date,string from notes WHERE name = ?", [user_input])
    result = row.fetchone()
    print(result[2])
    print("")