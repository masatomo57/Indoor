# 毎週水曜日0時に実行する。先週月曜日から日曜日までの購入履歴を取得する。
import csv
import sqlite3
from pandas import read_csv


file='yasai.csv'
yasai_data=read_csv(file, header=0)
items=yasai_data.columns[2:]



conn = sqlite3.connect('kakeibo.db')
db = conn.cursor()




users = db.execute("SELECT username FROM users").fetchall()

for username in users:
    for item in items:
        last_week_consumptions = db.execute("SELECT item, price, shares FROM buying WHERE user_id=? AND item=? AND transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", (username[0],item)).fetchall()
        yasai_data[item][]

db.close()