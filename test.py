import sqlite3 as sq


base = sq.connect('svyatoshapomichnyk.db')
cur = base.cursor()

a = cur.execute('SELECT * FROM skarga').fetchall()
if a:
    for ret in a:
        print(ret)
else:
    print("БД пуста")