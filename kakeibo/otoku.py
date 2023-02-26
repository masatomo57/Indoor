# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
import csv
import sqlite3
from pandas import read_csv


file_name='yasai.csv'
df=read_csv(file_name, header=0)
header=df.columns
print(header)





conn = sqlite3.connect('kakeibo.db')
db = conn.cursor()




users = db.execute("SELECT username FROM users").fetchall()

for username in users:
    last_week_consumptions = db.execute("SELECT item, price, shares FROM buying WHERE user_id=? AND transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", (username[0],)).fetchall()
    print(last_week_consumptions)


db.close()