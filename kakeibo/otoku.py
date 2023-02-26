# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
import csv
import sqlite3



conn = sqlite3.connect('kakeibo.db')
db = conn.cursor()


users = db.execute("SELECT username FROM users").fetchall()

for username in users:
    last_week_consumption = db.execute("SELECT sum(price*shares) AS sum FROM transact WHERE user_id=? AND transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", (username[0],)).fetchall()[0][0]
    if last_week_consumption == None:
        last_week_consumptionn = 0

    



db.close()