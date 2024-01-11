import sqlite3
import os.path

def display_rows(cur):
    for row in cur:
        print(f'{row[1]:10} {row[-2]:3} {row[-1]}')

db_file = 'students_info_db.sqlite'

if not os.path.exists(db_file):
    raise SystemExit(f'{db_file} not found')

conn = sqlite3.connect(db_file)
cur = conn.cursor()

query = "SELECT * FROM 'Students'"
query += "WHERE exp > ?"
min_exp = 2
query = query + "ORDER BY exp"
cur.execute(query, (min_exp,))

display_rows(cur)

conn.close()