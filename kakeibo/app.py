import os

from flask import Flask, render_template, flash, redirect, request, url_for, session, g, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from forms import SignUpForm, LoginForm
from config import BaseConfig
from flask_wtf.csrf import CSRFProtect
import csv
import datetime
import calendar
import json
import sqlite3
import otoku_test
import otoku_show
import secrets
import logging
logging.basicConfig()

# Configure application
app = Flask(__name__)

app.config.from_object(BaseConfig())

app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY # 秘密鍵を設定する

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["JSON_AS_ASCII"] = False

# 税率宣言
tax = 1.1

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# 秘密鍵を設定する
app.secret_key = app.config['SECRET_KEY']

csrf = CSRFProtect(app)
# ブラウザがレスポンスをキャッシュしないようにしている
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


#if __name__ == "__main__":
#    app.run(debug=True)


# データベースを呼び出す関数の定義
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('kakeibo.db')
    return g.db

"""
@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()
"""

# yasai.csvを読み込む関数の定義
def read_csv(filename, item):
    price = []
    date = []
    data = {}
    csv_file = filename + "_converted.csv"
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[item] == '':
                price.append(None)
            else:
                price.append(row[item])
            date.append(row["DATE"])
    data["price"] = price
    data["date"] = date
    data["lastprice"] = price[len(price)-1]
    return data


@app.route("/")
@login_required
def index():
    otoku = otoku_test.otoku(session["user_id"])
    #野菜のホーム画面データ
    num_list,judge=otoku_show.otoku_show_num(287)
    # num_list,judge=otoku_show.otoku_show_num(otoku[0])
    print(f'num_list:{num_list},judge:{judge}')
    level_hana=otoku_show.show_hana(num_list)

    #加工食品のホーム画面データ
    num_list,judge=otoku_show.otoku_show_num(9872)
    # num_list,judge=otoku_show.otoku_show_num(otoku[1])
    print(f'num_list:{num_list},judge:{judge}')
    level_stone=otoku_show.show_stone(num_list)

    #魚介のホーム画面データ
    num_list,judge=otoku_show.otoku_show_num(9999)
    # num_list,judge=otoku_show.otoku_show_num(otoku[2])
    print(f'num_list:{num_list},judge:{judge}')
    level_fish=otoku_show.show_fish(num_list)

    #肉食のホーム画面データ
    num_list,judge=otoku_show.otoku_show_num(4579)
    # num_list,judge=otoku_show.otoku_show_num(otoku[3])
    print(f'num_list:{num_list},judge:{judge}')
    level_animal=otoku_show.show_animal(num_list)

    return render_template("index.html",otoku=otoku,level_hana=level_hana,level_stone=level_stone,level_fish=level_fish,level_animal=level_animal)


@app.route("/charts")
@login_required
def charts():
    return redirect("/charts/cabbage")


@app.route("/charts/cabbage")
@login_required
def cabbage():
    name = "キャベツ"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))
    '''
    print(label_list)
    print(price_list)
    #print(type(label_list[0]))
    conn = sqlite3.connect("kakeibo.db")
    db = conn.cursor()
    plot_data = db.execute('SELECT transacted,price FROM test_buying WHERE user_id = ? AND item = ?', (session["user_id"],name)).fetchall()
    conn.close()
    print(type(plot_data))
    print(plot_data)

    print(len(plot_data))
    for i in range(len(plot_data)):
        print(plot_data[i])
        print(type(plot_data[i][0]))
    '''

    #return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price,plot_data=plot_data)
    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/greenonion")
@login_required
def greenonion():
    name = "ねぎ"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/lettuce")
@login_required
def lettuce():
    name = "レタス"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/potato")
@login_required
def potato():
    name = "ばれいしょ"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/onion")
@login_required
def onion():
    name = "たまねぎ"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/cucumber")
@login_required
def cucumber():
    name = "きゅうり"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/tomato")
@login_required
def tomato():
    name = "トマト"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/spinach")
@login_required
def spinach():
    name = "ほうれんそう"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/carrot")
@login_required
def carrot():
    name = "にんじん"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/chinesecabbage")
@login_required
def chinesecabbage():
    name = "はくさい"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/raddish")
@login_required
def raddish():
    name = "だいこん"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/eggplant")
@login_required
def eggplant():
    name = "なす"
    data = read_csv("yasai", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/bread")
@login_required
def bread():
    name = "食パン"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/instantnoodle")
@login_required
def instantnoodle():
    name = "即席めん"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/udon")
@login_required
def udon():
    name = "ゆでうどん"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/flour")
@login_required
def flour():
    name = "小麦粉"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/milk")
@login_required
def milk():
    name = "牛乳"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/cheese")
@login_required
def cheese():
    name = "チーズ"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/tofu")
@login_required
def tofu():
    name = "豆腐"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/canolaoil")
@login_required
def canolaoil():
    name = "食用油（キャノーラ油）"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/saladoil")
@login_required
def saladoil():
    name = "食用油（サラダ油）"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/margarine")
@login_required
def margarine():
    name = "マーガリン"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/mayonnaise")
@login_required
def mayonnaise():
    name = "マヨネーズ"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/soysauce")
@login_required
def soysauce():
    name = "しょう油"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/miso")
@login_required
def miso():
    name = "みそ"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/fishcake")
@login_required
def fishcake():
    name = "かまぼこ"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/cannedtuna")
@login_required
def cannedtuna():
    name = "まぐろ缶詰"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/butter")
@login_required
def butter():
    name = "バター"
    data = read_csv("kakou", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/importedbeef")
@login_required
def importedbeef():
    name = "輸入牛肉（冷蔵ロース）"
    data = read_csv("niku", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/domesticbeef")
@login_required
def domesticbeef():
    name = "国産牛肉（冷蔵ロース）"
    data = read_csv("niku", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/pork")
@login_required
def pork():
    name = "豚肉（ロース）"
    data = read_csv("niku", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/chicken")
@login_required
def chicken():
    name = "鶏肉（もも肉）"
    data = read_csv("niku", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/egg")
@login_required
def egg():
    name = "鶏卵 サイズ混合・10個入り）"
    data = read_csv("niku", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/tuna")
@login_required
def tuna():
    name = "まぐろ"
    data = read_csv("sakana", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/shrimp")
@login_required
def shrimp():
    name = "えび"
    data = read_csv("sakana", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/yellowtail")
@login_required
def yellowtail():
    name = "ぶり"
    data = read_csv("sakana", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


@app.route("/charts/salmon")
@login_required
def salmon():
    name = "さけ"
    data = read_csv("sakana", name)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))

    return render_template("charts/chart.html", label_list=label_list, price_list=price_list, name=name, last_price=last_price)


"""
@app.route("/kakeibo", methods=["GET"])
@login_required
def kakeibo():
    # 今日の1日と今日の日付を取得
    today = datetime.date.today()
    year = request.args.get('year', today.year)
    month = request.args.get('month', today.month)
    start_date = datetime.date(year,month,1)
    last_date = datetime.date(year,month,calendar.monthrange(year, month)[1])
    # 日付と税込金額を渡してほしい(カレンダー表示のため)
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute('SELECT transacted,sum FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    print(database)
    return render_template("kakeibo/index.html",database=database)
"""

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
        cur.execute('SELECT transacted,SUM(price) FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? GROUP BY transacted ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
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
    cur.execute('SELECT transacted,SUM(price) FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? GROUP BY transacted ORDER BY transacted ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    print(database)
    return jsonify(database)
    # return render_template("kakeibo/index.html", database=database)


# 今月のデータを取得するための関数
def thismonthdata():
    today = datetime.date.today()
    start_date = today.replace(day=1)
    last_date = today
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute('SELECT transacted,item,price,shares,gram FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC, item ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    return database


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    if request.method == "POST":
        if request.form.get("submit") == "test2":
            return redirect("/test2")
        elif request.form.get("submit") == "test1":
            return redirect("/test1")
        elif request.form.get("submit") == "test3":
            return redirect("/test3")
        elif request.form.get("submit") == "test4":
            return redirect("/test4")
    else:
        return render_template("register.html",database=thismonthdata())


@app.route("/test1", methods=["POST"])
@login_required
def test1():
    # 今月のデータを取得
    database = thismonthdata()

    regist_name = request.form.get("name")
    regist_price = request.form.get("price")
    regist_quantity = request.form.get("quantity")
    regist_date = request.form.get("date")
    regist_gram = request.form.get("gram")

    if not regist_name or not regist_price or not regist_quantity or not regist_date:
        return render_template("register.html",database=database)

    db = get_db()
    error = None
    # 日付と品目のペアがすでに存在する場合はエラーを返す
    result = db.execute("SELECT * FROM test_buying WHERE user_id = ? AND item = ? AND transacted = ?", (session["user_id"], regist_name, regist_date)).fetchone()

    if result:
        error="すでにデータが登録されている可能性があります。"
        if not regist_gram:
            regist_gram = None
        db.execute("UPDATE test_buying SET price = price + ?, shares = shares + ?, gram = ? WHERE user_id = ? AND item = ? AND transacted = ?", (regist_price,regist_quantity,regist_gram,session["user_id"],regist_name,regist_date))

    #if regist_price:
    #    regist_sum = int(float(regist_price) * tax)
    # sum(カラム)はいらないので、後で消したい。
    if not result:
        if not regist_gram:
            db.execute("INSERT INTO test_buying (user_id,item,price,shares,transacted,sum) VALUES (?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_date,regist_price))
        else:
            db.execute("INSERT INTO test_buying (user_id,item,price,shares,gram,transacted,sum) VALUES (?,?,?,?,?,?,?)",(session["user_id"],regist_name,regist_price,regist_quantity,regist_gram,regist_date,regist_price))

    db.commit()
    db.close()
    database = thismonthdata()
    return render_template('register.html', database=database, error=error)


@app.route("/test2", methods=["POST"])
@login_required
def test2():
    start_date = request.form.get("start_date")
    last_date = request.form.get("last_date")
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute('SELECT transacted,item,price,shares,gram FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC, item ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    return render_template('register.html', database=database)


@app.route("/test3", methods=["POST"])
@login_required
def test3():
    # 削除ボタン(テーブルの削除)
    data = request.json
    date = data['date']
    item = data['name']
    price = data['price']
    quantity = data['quantity']
    gram = data['gram']
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    if gram != 'None':
        cur.execute("DELETE FROM test_buying WHERE user_id = ? AND transacted = ? AND item = ? AND price = ? AND shares = ? AND gram = ?", (session["user_id"], date, item, price, quantity, gram))
    else:
        cur.execute("DELETE FROM test_buying WHERE user_id = ? AND transacted = ? AND item = ? AND price = ? AND shares = ?", (session["user_id"], date, item, price, quantity))
    conn.commit()
    database = cur.fetchall()
    conn.close()
    return jsonify(database)


@app.route("/test4", methods=["POST"])
@login_required
def test4():
     # 編集実行ボタンが押されたときの処理
    start_date = '2023-03-02'
    last_date = '2023-03-03'
    data = request.json
    date = data['date']
    item = data['name']
    price = data['price']
    quantity = data['quantity']
    gram = data['gram']
    if gram == 'None':
        gram = None
    conn = sqlite3.connect('kakeibo.db')
    cur = conn.cursor()
    cur.execute("UPDATE test_buying SET price=?,shares=?,gram=? WHERE user_id=? AND item=? AND transacted=?", (price, quantity, gram, session["user_id"], item, date))
    conn.commit()
    cur.execute('SELECT transacted,item,price,shares,gram FROM test_buying WHERE user_id = ? AND transacted BETWEEN ? AND ? ORDER BY transacted ASC, item ASC', (session["user_id"], start_date, last_date))
    database = cur.fetchall()
    conn.close()
    return jsonify(database)
    # return render_template('register.html', database=database, error=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    form = LoginForm()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # if form.validate_on_submit():
            db = get_db()

            username = form.username.data
            password = form.password.data

            # Ensure username was submitted
            if not username:
                return redirect("/login")

            # Ensure password was submitted
            elif not password:
                return redirect("/login")

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
            rows_count = db.execute("SELECT count(*) FROM users WHERE username = ?", (username,)).fetchall()

            # Ensure username exists and password is correct
            if rows_count[0][0] != 1 or not check_password_hash(rows[0][2], password):
                return redirect("/login")
            # Remember which user has logged in
            session["user_id"] = rows[0][1]

            db.close()

            # Redirect user to home page
            return redirect("/")
        #else:
        #    return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html",form=form)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            db = get_db()

            username = form.username.data
            password = form.password.data
            confirmation = form.confirmation.data

            duplication=db.execute("SELECT id FROM users WHERE username=?", (username,)).fetchall()
            if duplication:
                flash("このユーザー名はすでに登録されています。他のユーザー名でご登録下さい。")
                return redirect("/signup")
            else:
                if username=="" or password=="" or confirmation =="":
                    return redirect("/signup")
                elif not password==confirmation:
                    flash("パスワードが一致していません。")
                    return redirect("/signup")
                else:
                    db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (username, generate_password_hash(password)))
                    db.commit()
                    db.close()

                    flash("ユーザー登録に成功しました。")
                    return redirect("/login")

    else:
        return render_template("signup.html",form=form)



