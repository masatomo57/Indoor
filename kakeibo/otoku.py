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

otoku_price = 0

for username in users:
    for item in items:
        last_week_consumptions = db.execute("SELECT sum(price*shares) FROM buying WHERE user_id=? AND item=? AND transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", (username[0],item)).fetchall()[0][0]
        if last_week_consumptions == None:
            continue
        last_week_consumptions = float(last_week_consumptions)
        otoku_price += float(yasai_data[item][len(yasai_data)-1]) - last_week_consumptions

    db.execute("INSERT INTO otoku (user_id, price, calculated) VALUES(?, ?, DATE('now', 'localtime', '-9 day'))", (username, otoku_price))
    db.commit()

db.close()

