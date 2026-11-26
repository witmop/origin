import sqlite3 as sq
import pandas as pd

# Создание баз данных

# con = sq.connect("marvel-wikia-data.csv")
# cur = con.cursor()
# cur.execute(""" """)        #запрос к базе данных

# con.close()

# лучше так
# with sq.connect("saper.db") as con:
#     cur =con.cursor()
#     cur.execute("DROP TABLE IF EXISTS users")
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, sex INTEGER DEFAULT 1, old INTEGER, score INTEGER) """)        #primary_key значит что начение не должны повторяться
#     # cur.execute("""DROP TABLE users""")   удаляет таблицу
    

# Заропсы SELECT INSERT

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     # cur.execute("INSERT INTO users (name,old,score) VALUES('Фёдор',32,200)")
#     # cur.execute("INSERT INTO users (name,old,score) VALUES('Николай',22,500)")
#     cur.execute("SELECT name,old,score FROM users")
#     cur.execute("SELECT * FROM users WHERE score<1000   ")
#     print(pd.DataFrame(cur.execute("SELECT * FROM users WHERE score BETWEEN 500 AND 1000")))
#     cur.execute("SELECT * FROM users WHERE old<20 AND SCORE<900")   #в конце можно записать ORDER BY (название колонки) - включает сортирвоку если добавить DESC - обратная сортировка
#     #если добавить LIMIT (число) - кол-во записей или 

#     cur.execute("SELECT * FROM users WHERE sex==1 and old<=25 ORDER BY old DESC LIMIT 1")
#     # result = cur.fetchall()     #для получение упорядоч. списка
#     # cur.fetchone() - выбирает первую запись
#     # cur.fetchmany(число) - выбирает опр число записей
#     # #Альтернатива fetchall (экономит память)
#     for result in cur:
#         print(result)


# Запросы DELETE/UPDATE

# with  sq.connect("saper.db") as con:
#     cur = con.cursor()
    # cur.execute("UPDATE users SET score = 200 WHERE user_id == 1")
    # cur.execute("UPDATE users SET score = score+50 WHERE sex == 2")
    # cur.execute("UPDATE users set old = old + 1 WHERE name LIKE 'Фёдор'")     #LIKE возвращает True пример LIKE 'М%' - все имена, начинающиеся с М (_) - одна любая буква (%) - любое кол-во букв

    #   Лучше задавать фильтры по числам, а не по буквам (так быстрее)
    
    # cur.execute("DELETE FROM users WHERE row_id IN (2,5)") -    #удалиться row_id, где 2 и 5
    

#Агрегирование и группировка GROUP BY

with sq.connect("saper.db") as con:
    cur = con.cursor()
    # cur.execute("INSERT INTO users (name,old,score) VALUES('Пётр', 22,350)")
    cur.execute("SELECT count(old) as count FROM users WHERE old == 22")     #возвращает кол-во  (as count) просто меняет название поля
    cur.execute("SELECT count(DISTINCT old) as old FROM users")     #DISTINCT смотри кол-во уникальных значений
    cur.execute("SELECT old,sum(score) as result_score FROM users GROUP BY old ORDER BY result_score")
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)