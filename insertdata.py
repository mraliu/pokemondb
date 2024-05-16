import sqlite3

conn = sqlite3.connect("pokemon.db")

sql = "INSERT INTO pokemon ('#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary') VALUES (1, 'Pikachu', 'Electric', 'Poison', 10, 10, 10, 10, 10, 10, 10, 10, 'False')"

conn.execute(sql)
conn.commit()
conn.close()

    