# Contains all fucntions for listing notes
import sqlite3


def list_all_notes():
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    for row in cur.execute("SELECT name, date, string FROM notes"):
        print(f"{row[0]} | {row[1]} | {row[2]}")
    con.close()


def list_note():
    user_input = input(
        "\nPlease enter the name of the note you want to read:\n")
    print("")
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    row = cur.execute(
        "SELECT name, date,string from notes WHERE name LIKE ?", [user_input])
    result = row.fetchone()
    print(f"\n{result[0]}\nLast updated at {result[1]}:\n")
    print(result[2])
    print("")
