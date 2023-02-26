import csv
import sqlite3



conn = sqlite3.connect('kakeibo.db')
db = conn.cursor()

# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
users = db.execute("SELECT username FROM users").fetchall()

for username in users:
    # print(username[0])
    last_week_transact = db.execute("SELECT sum(price*shares) AS sum FROM transact WHERE user_id=(?,) transacted BETWEEN DATETIME(CURRENT_DATE, 'localtime', '-9 day') AND DATETIME(CURRENT_DATE, 'localtime', '-3 day')", (username[0],)).fetchall()

print(lastweek_transact)




db.close()