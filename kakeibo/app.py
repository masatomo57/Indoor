from flask import Flask, render_template, g

# アプリケーション定義
app = Flask(__name__)

# データベースを呼び出す関数の定義、データベースができたらコメントアウト外してください。
'''
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('データベースの名前.db')
    return g.db
'''

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

# CS50モジュールのSQLを使いたくないため上のコメントアウトを書いています。以下はCS50のbirthdayにおけるCS50のSQLを使わなかった場合の例です。
'''
import os

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, g

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('birthdays.db')
    return g.db

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
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
'''