import csv
import sqlite3
from app import get_db, read_csv

db = get_db()

# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
users = db.execute("SELECT username FROM users").fetchall()

for user in users:
    last_week_transact = db.execute("SELECT sum(price*shares) AS sum FROM transact WHERE user_id=(?,) transacted BETWEEN DATETIME(CURRENT_DATE, 'localtime', '-9 day') AND DATETIME(CURRENT_DATE, 'localtime', '-3 day')").fetchall()



db.close()