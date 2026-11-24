import sqlite3 as sq
# con = sq.connect("marvel-wikia-data.csv")
# cur = con.cursor()
# cur.execute(""" """)        #запрос к базе данных

# con.close()

# лучше так
with sq.connect("saper.db") as con:
    cur =con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, sex INTEGER DEFAULT 1, old INTEGER, score INTEGER) """)        #primary_key значит что начение не должны повторяться
    # cur.execute("""DROP TABLE users""")   удаляет таблицу
    