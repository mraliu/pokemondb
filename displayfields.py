import sqlite3

conn = sqlite3.connect("pokemon.db")

cur = conn.cursor()

sql = "SELECT * FROM pokemon"

res = cur.execute(sql)

for field in res.description: # Description usesd to get field headings
    print(field[0]) # Returns as a tuple using index 0 to get first value of tuple


