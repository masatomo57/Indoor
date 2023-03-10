import sqlite3
from pandas import read_csv


def weekly_otoku_calculate(filename, kind, database):
    conn = sqlite3.connect(database)
    db = conn.cursor()

    users = db.execute("SELECT username FROM users").fetchall()

    otoku_price = 0

    data=read_csv(filename, header=0)
    items=data.columns[2:]

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

    otoku_price = 0

    data=read_csv(filename, header=0)
    items=data.columns[2:]

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

# ???????????????0????????????????????????????????????????????????????????????????????????????????????
weekly_otoku_calculate("yasai.csv", "??????", "kakeibo.db")
# ??????1???0???????????????????????????1????????????????????????????????????????????????
monthly_otoku_calculate("kakou.csv", "????????????", "kakeibo.db")


