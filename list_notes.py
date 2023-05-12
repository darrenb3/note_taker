# Contains all fucntions for listing notes
import sqlite3
from rich.console import Console
from rich.table import Table


def list_all_notes():
    table = Table(title="Current Notes")
    table.add_column("Name")  # style="pink"
    table.add_column("Last Edited")
    table.add_column("Contents")
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    for row in cur.execute("SELECT name, date, string FROM notes"):
        table.add_row(f"{row[0]}", f"{row[1]}", f"{row[2]}")
    console = Console(highlight=False)
    console.print(table)
    con.close()


def list_note():
    console = Console(highlight=False)
    user_input = input(
        "\nPlease enter the name of the note you want to read:\n")
    print("")
    con = sqlite3.connect("note_taker.db")
    cur = con.cursor()
    row = cur.execute(
        "SELECT name, date,string from notes WHERE name LIKE ?", [user_input])
    result = row.fetchone()
    console.print(
        f"\n[bold underline #ffa6c9]{result[0]}[/bold underline #ffa6c9]\nLast updated at {result[1]}:\n")
    console.print(f"{result[2]}\n")
