
#-----------------------------
#川島20230305
#お得の計算コードを作ってみる
#-----------------------------

import sqlite3
from pandas import read_csv


def weekly_otoku_calculate(filename, kind, database):
    conn = sqlite3.connect(database)
    db = conn.cursor()

    users = db.execute("SELECT username FROM users").fetchall()
    print(users)

    otoku_price = 0

    data=read_csv(filename, header=0)
    items=data.columns[2:]
    print(items)

    for username in users:
        for item in items:
            last_week_consumptions = db.execute("SELECT sum(price*shares) FROM buying WHERE user_id=? AND item=? AND transacted BETWEEN DATE('now', 'localtime', '-9 day') AND DATE('now', 'localtime', '-3 day')", (username[0],item)).fetchall()[0][0]
            if last_week_consumptions == None:
                continue
            last_week_consumptions = float(last_week_consumptions)
            otoku_price += float(yasai_data[item][len(yasai_data)-1]) - last_week_consumptions

        db.execute("INSERT INTO otoku (user_id, kind, price, calculated) VALUES(?, ?, ?, DATE('now', 'localtime', '-9 day'))", (username[0], kind, otoku_price))
        conn.commit()

    conn.close()

def monthly_otoku_calculate(filename, kind, database):
    conn = sqlite3.connect(database)
    db = conn.cursor()

    users = db.execute("SELECT username FROM users").fetchall()
    print(users)

    otoku_price = 0

    data=read_csv(filename, header=0)
    items=data.columns[2:]
    print(items)#touple
    print(items[0])
    if items[0] == "食パン":
        print("ok")

    for username in users:
        for item in items:
            last_week_consumptions = db.execute("SELECT sum(price*shares) FROM buying WHERE user_id=? AND item=? AND transacted BETWEEN DATE('now', 'localtime', '-1 month') AND DATE('now', 'localtime', '-1 day')", (username[0],item)).fetchall()[0][0]
            if last_week_consumptions == None:
                continue
            last_week_consumptions = float(last_week_consumptions)
            otoku_price += float(yasai_data[item][len(yasai_data)-1]) - last_week_consumptions

        db.execute("INSERT INTO otoku (user_id, kind, price, calculated) VALUES(?, ?, ?, DATE('now', 'localtime', '-1 month'))", (username[0], kind, otoku_price))
        conn.commit()

    conn.close()


def otoku(username,item):
    if item == "yasai":
        # 毎週水曜日0時に実行する。前週月曜日から日曜日までのお得を計算する。
        weekly_otoku_calculate("yasai.csv", "野菜", "kakeibo.db")
    elif item == "kakou":
        # 毎月1日0時に実行する。先月1日から末日までのお得を計算する。
        monthly_otoku_calculate("kakou.csv", "加工食品", "kakeibo.db")
    elif item == "sakana":
        # 毎月1日0時に実行する。先月1日から末日までのお得を計算する。
        monthly_otoku_calculate("sakana.csv", "加工食品", "kakeibo.db")
    elif item == "niku":
        # 毎月1日0時に実行する。先月1日から末日までのお得を計算する。
        monthly_otoku_calculate("niku.csv", "加工食品", "kakeibo.db")
    else:
        print("error")
        exit()

# 毎週水曜日0時に実行する。前週月曜日から日曜日までのお得を計算する。
weekly_otoku_calculate("yasai.csv", "野菜", "kakeibo.db")
# 毎月1日0時に実行する。先月1日から末日までのお得を計算する。
monthly_otoku_calculate("kakou.csv", "加工食品", "kakeibo.db")

