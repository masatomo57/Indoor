import csv
import sqlite3



conn = sqlite3.connect('kakeibo.db')
db = conn.cursor()

# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
users = db.execute("SELECT username FROM users").fetchall()

for username in users:
    # print(username[0])
    last_week_transact = db.execute("SELECT sum(price*shares) AS sum FROM transact WHERE user_id=? transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", 'signup').fetchall()

print(lastweek_transact)




db.close()