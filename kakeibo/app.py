import os

from flask import Flask, render_template, flash, redirect, request, url_for, session, g
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import login_required, tax
import csv

import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["tax"] = tax

app.config.from_object('config')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# ブラウザがレスポンスをキャッシュしないようにしている
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# データベースを呼び出す関数の定義
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('kakeibo.db')
    return g.db



# yasai.csvを読み込む関数の定義
def read_csv(csv_file, item):
    price = []
    date = []
    data = {}
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date.append(row["DATE"])
            if row[item] == '':
                price.append(None)
            else:
                price.append(row[item])
    data["price"] = price
    data["date"] = date
    data["lastprice"] = price[len(price)-1]
    return data


@app.route("/")
@login_required
def index():
    name = "おトク"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]

    return render_template("index.html", label_list=label_list, price_list=price_list, name=name)

@app.route("/charts")
@login_required
def charts():
    return redirect("/charts/cabbage")

@app.route("/charts/cabbage")
@login_required
def cabbage():
    name = "キャベツ"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/greenonion")
@login_required
def greenonion():
    name = "ねぎ"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/lettuce")
@login_required
def lettuce():
    name = "レタス"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/potato")
@login_required
def potato():
    name = "ばれいしょ"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/onion")
@login_required
def onion():
    name = "たまねぎ"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/cucumber")
@login_required
def cucumber():
    name = "きゅうり"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/tomato")
@login_required
def tomato():
    name = "トマト"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/spinach")
@login_required
def spinach():
    name = "ほうれんそう"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/carrot")
@login_required
def carrot():
    name = "にんじん"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/chinesecabbage")
@login_required
def chinesecabbage():
    name = "はくさい"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/raddish")
@login_required
def raddish():
    name = "だいこん"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/eggplant")
@login_required
def eggplant():
    name = "なす"
    data = read_csv(yasai.csv, name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)




@app.route("/kakeibo")
@login_required
def kakeibo():
    return render_template("kakeibo/index.html")


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    if request.method == "POST":
        if request.form.get("submit") == "test1":
            return redirect("/test1")
        elif request.form.get("submit") == "test2":
            return redirect("/test2")
        elif request.form.get("submit") == "test3":
            return redirect("/test3")
        elif request.form.get("submit") == "test4":
            return redirect("/test4")
    else:
        # 日付と税込み金額を渡してほしい(カレンダー表示のため)
        return render_template("register.html")

@app.route("/test1", methods=["POST"])
@login_required
def test1():
    if request.method == "POST":
        regist_name = request.form.get("name")
        regist_price = request.form.get("price")
        regist_quantity = request.form.get("quantity")
        regist_date = request.form.get("date")
        print(regist_name)
        print(regist_price)
        print(regist_quantity)
        print(regist_date)
        # Redirect user to home page
        if not (regist_name or regist_price or regist_quantity or regist_date):
            return redirect("/register")
        # 出来れば税込金額のカラム(sum)も欲しいかも!
        db = get_db()
        db.execute("INSERT INTO buying (user_id,item,price,shares,transacted) VALUES (?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_date))
        db.commit()
        db.close()
        return redirect("/register")

@app.route("/test2", methods=["POST"])
@login_required
def test2():
    # 表示期間ボタンを押すので、対象期間の日付と品目と税込金額が必要
    # (例)2023-02-26
    tax = 1.1
    start_date = request.form.get("start_date")
    last_date = request.form.get("last_date")
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute('SELECT transacted,item,price FROM buying WHERE user_id = ? AND transacted BETWEEN ? AND ?', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    return render_template('register.html', database=database, tax=tax)

@app.route("/test3", methods=["POST"])
@login_required
def test3():
    # test3の処理を実装
    # 削除ボタン(テーブルの削除)
    data = request.json
    date = data['date']
    item = data['name']
    price = data['sum']
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM buying WHERE user_id = ? AND transacted=? AND item=? AND price=?", (session["user_id"], date, item, price))
    conn.commit()
    cur.execute("SELECT * FROM buying WHERE user_id = ?", (session["user_id"],))
    database = cur.fetchall()
    conn.close()
    return render_template('register.html',database=database)

@app.route("/test4", methods=["POST"])
@login_required
def test4():
    # test4の処理を実装
    # 編集ボタン(テーブルの編集)(ここは最悪なくて良い)
    return redirect("/reister")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        db = get_db()

        # Ensure username was submitted
        if not request.form.get("username"):
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return redirect("/login")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),)).fetchall()
        rows_count = db.execute("SELECT count(*) FROM users WHERE username = ?", (request.form.get("username"),)).fetchall()

        # Ensure username exists and password is correct
        if rows_count[0][0] != 1 or not check_password_hash(rows[0][2], request.form.get("password")):
            return redirect("/login")
        # Remember which user has logged in
        session["user_id"] = rows[0][1]

        db.close()

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        db = get_db()

        duplication=db.execute("SELECT id FROM users WHERE username=?", (request.form.get("username"),)).fetchall()
        if request.form.get("username")=="" or request.form.get("password")=="":
            return redirect("/signup")
        elif request.form.get("password")=="" or not request.form.get("password")==request.form.get("confirmation"):
            return redirect("/signup")
        elif duplication:
            return redirect("/signup")
        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (request.form.get("username"), generate_password_hash(request.form.get("password"))))
            db.commit()
            db.close()

            return redirect("/login")
    else:
        return render_template("signup.html")

# CS50モジュールのSQLを使いたくないため上のget_dbを定義しています。以下はCS50のbirthdayにおけるCS50のSQLを使わなかった場合の例です。これを参考にfinanceの移植、書き換えをお願いします。
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
