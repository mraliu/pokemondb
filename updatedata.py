import sqlite3

conn = sqlite3.connect("pokemon.db")

sql = "UPDATE pokemon SET Name='Ivy' WHERE Name = 'Ivysaur'"

conn.execute(sql)
conn.commit()
conn.close()



