import sqlite3

conn = sqlite3.connect("pokemon.db")

sql = "DELETE FROM pokemon WHERE Name = 'Pikachu'"

conn.execute(sql)
conn.commit()
conn.close()

    