# Fills the database with random info for testing purposes
import sqlite3

con = sqlite3.connect("note_taker.db")
cur = con.cursor()
i = 0
while i < 100:
    data = [f"Note {i}", f"Time {i}", f"Content {i}"]
    cur.execute("INSERT INTO notes VALUES(?,?,?)", data)
    i += 1
    con.commit()
con.close()
