import sqlite3
from datetime import datetime
from rich.console import Console

console = Console(highlight=False)


def update_note():
    note_name = console.input(
        "\nPlease enter the name of the note you want to update:\n")
    # Need to put error checking here that the record actually exists
    note_content = console.input(
        "\nPlease enter the new content of the note:\n")
    now = datetime.now().strftime('%H:%M:%S %m/%d/%Y')
#    console.print(now)
    data = [now, note_content, note_name]
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    cur.execute("UPDATE notes SET date = ?, string = ? WHERE name LIKE ?", data)
    con.commit()
    con.close()
    return True
