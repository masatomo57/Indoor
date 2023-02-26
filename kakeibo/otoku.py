import csv
import sqlite3
from app import get_db, read_csv

db = get_db()

last_week_transact = db.execute("SELECT * FROM transact WHERE transacted").fetchall()

db = get_db()
if request.method == "POST":
    name=request.form.get("name")
    month=request.form.get("month")
    day=request.form.get("day")
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", (name, month, day))
    db.commit()
    return redirect("/")
else:
    birthdays = db.execute("SELECT name, month, day FROM birthdays")
    birthdays = birthdays.fetchall()
    birthdays_col = ["name", "month", "day"]
    birthdays_list = []
    for birthday in birthdays:
        item = dict(zip(birthdays_col, birthday))
        birthdays_list.append(item)
    return render_template("index.html", birthdays=birthdays_list)
db.close()