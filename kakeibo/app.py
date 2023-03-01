import os

from flask import Flask, render_template, flash, redirect, request, url_for, session, g, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, tax
import csv
import datetime
import calendar
import json
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["tax"] = tax
tax = 1.1

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
    data = read_csv("yasai.csv", "キャベツ")
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
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/greenonion")
@login_required
def greenonion():
    name = "ねぎ"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/lettuce")
@login_required
def lettuce():
    name = "レタス"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/potato")
@login_required
def potato():
    name = "ばれいしょ"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/onion")
@login_required
def onion():
    name = "たまねぎ"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/cucumber")
@login_required
def cucumber():
    name = "きゅうり"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/tomato")
@login_required
def tomato():
    name = "トマト"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/spinach")
@login_required
def spinach():
    name = "ほうれんそう"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/carrot")
@login_required
def carrot():
    name = "にんじん"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/chinesecabbage")
@login_required
def chinesecabbage():
    name = "はくさい"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/raddish")
@login_required
def raddish():
    name = "だいこん"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/eggplant")
@login_required
def eggplant():
    name = "なす"
    data = read_csv("yasai.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/bread")
@login_required
def bread():
    name = "食パン"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/instantnoodle")
@login_required
def instantnoodle():
    name = "即席めん"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/udon")
@login_required
def udon():
    name = "ゆでうどん"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/flour")
@login_required
def flour():
    name = "小麦粉"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/milk")
@login_required
def milk():
    name = "牛乳"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/cheese")
@login_required
def cheese():
    name = "チーズ"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/tofu")
@login_required
def tofu():
    name = "豆腐"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/canolaoil")
@login_required
def canolaoil():
    name = "食用油（キャノーラ油）"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/saladoil")
@login_required
def saladoil():
    name = "食用油（サラダ油）"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/margarine")
@login_required
def margarine():
    name = "マーガリン"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/mayonnaise")
@login_required
def mayonnaise():
    name = "マヨネーズ"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/soysauce")
@login_required
def soysauce():
    name = "しょう油"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/miso")
@login_required
def miso():
    name = "みそ"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/fishcake")
@login_required
def fishcake():
    name = "かまぼこ"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/cannedtuna")
@login_required
def cannedtuna():
    name = "まぐろ缶詰"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)

@app.route("/charts/butter")
@login_required
def butter():
    name = "バター"
    data = read_csv("kakou.csv", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)




@app.route("/kakeibo")
@login_required
def kakeibo():
    if request.method == "POST":
        if request.form.get("submit") == "test":
            return redirect("/test")
        return render_template("kakeibo/index.html",database=[])
    else:
        # 今日の1日と今日の日付を取得
        today = datetime.date.today()
        start_date = today.replace(day=1)
        last_date = today
        # 日付と税込金額を渡してほしい(カレンダー表示のため)
        conn = sqlite3.connect('kakeibo.db')
        cur = conn.cursor()
        #cur.execute('SELECT transacted,price FROM buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
        cur.execute('SELECT transacted,price FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
        database = cur.fetchall()
        conn.close()
        print(database)
        return render_template("kakeibo/index.html",database=database)

@app.route("/test", methods=["POST"])
@login_required
def test():
    data = request.json
    year = data['year']
    month = data['month']
    start_date = datetime.date(year,month,1)
    last_date = datetime.date(year,month,calendar.monthrange(year,month)[1])
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute('SELECT transacted,price FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
    #cur.execute('SELECT transacted,price FROM buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    print(database)
    return render_template("kakeibo/index.html", database=database)

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
        regist_gram = request.form.get("gram")
        # Redirect user to home page
        if not regist_name:
            return redirect("/register")
        if not regist_price:
            return redirect("/register")
        if not regist_quantity:
            return redirect("/register")
        if not regist_date:
            return redirect("/register")
        if not regist_gram:
            return redirect("/register")
        # 税込金額のカラムをsum,重さのカラムをgramとする
        db = get_db()
        regist_sum = int(float(regist_price) * tax)
        if not regist_gram:
            db.execute("INSERT INTO test_buying (user_id,item,price,shares,transacted,sum) VALUES (?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_date,regist_sum))
            #db.execute("INSERT INTO buying (user_id,item,price,shares,transacted,sum) VALUES (?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_date,regist_sum))
        else:
           db.execute("INSERT INTO test_buying (user_id,item,price,shares,gram,transacted,sum) VALUES (?,?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_gram,regist_date,regist_sum))
           #db.execute("INSERT INTO bying (user_id,item,price,shares,gram,transacted,sum) VALUES (?,?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_gram,regist_date,regist_sum))
        db.commit()
        db.close()
        return render_template('register.html', database=[])

@app.route("/test2", methods=["POST"])
@login_required
def test2():
    start_date = request.form.get("start_date")
    last_date = request.form.get("last_date")
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    #cur.execute('SELECT transacted,item,price,shares,gram FROM buying WHERE user_id = ? AND transacted BETWEEN ? AND ?', (session["user_id"], start_date, last_date))
    cur.execute('SELECT transacted,item,price,shares,gram FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ?', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    return render_template('register.html', database=database)

@app.route("/test3", methods=["POST"])
@login_required
def test3():
    # test3の処理を実装
    # 削除ボタン(テーブルの削除)
    data = request.json
    date = data['date']
    item = data['name']
    price = data['price']
    quantity = data['quantity']
    gram = data['gram']
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM test_buying WHERE user_id = ? AND transacted = ? AND item = ? AND price = ? AND shares = ? AND gram = ?", (session["user_id"], date, item, price, quantity, gram))
    #cur.execute("DELETE FROM buying WHERE user_id = ? AND transacted = ? AND item = ? AND price = ? AND shares = ? AND gram = ?", (session["user_id"], date, item, price, quantity, gram))
    conn.commit()
    cur.execute("SELECT * FROM test_buying WHERE user_id = ?", (session["user_id"],))
    #cur.execute("SELECT * FROM buying WHERE user_id = ?", (session["user_id"],))
    database = cur.fetchall()
    conn.close()
    return jsonify(database)

@app.route("/test4", methods=["POST"])
@login_required
def test4():
     # 編集実行ボタンが押されたときの処理
    data = request.json
    date = data['date']
    item = data['name']
    price = data['price']
    quantity = data['quantity']
    gram = data['gram']
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute("UPDATE test_buying SET price=?,shares=?,gram=? WHERE user_id=? AND item=? AND transacted=?", (price, quantity, gram, session["user_id"], item, date))
    #cur.execute("UPDATE buying SET price=?,shares=?,gram=? WHERE user_id=? AND item=? AND transacted=?", (price, quantity, gram, session["user_id"], item, date))
    conn.commit()
    cur.execute("SELECT * FROM test_buying WHERE user_id = ?", (session["user_id"],))
    #cur.execute("SELECT * FROM buying WHERE user_id = ?", (session["user_id"],))
    database = cur.fetchall()
    conn.close()
    return render_template('register.html', database=database)

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
