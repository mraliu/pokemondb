import sqlite3

conn = sqlite3.connect("pokemon.db")

cur = conn.cursor()

sql = "SELECT * FROM pokemon"

res = cur.execute(sql)

# print(res.fetchall())

for record in res.fetchall():
    print(record)