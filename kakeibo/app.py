<<<<<<< HEAD
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

db = SQLAlchemy()
csrf = CSRFProtect()
# LoginManagerをインスタンス化する
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.signup"
# login_message属性にログイン後に表示するメッセージを指定する
# ここでは何も表示しないよう空を指定する
login_manager.login_message = ""


# create_app関数を作成する
def create_app(config_key):
    # Flaskインスタンス生成
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    csrf.init_app(app)
    # login_managerをアプリケーションと連携する
    login_manager.init_app(app)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # これから作成するauthパッケージからviewsをimportする
    from apps.auth import views as auth_views

    # register_blueprintを使いviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # カスタムエラー画面を登録する
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    return app


# 登録したエンドポイント名の関数を作成し、404や500が発生した際に指定したHTMLを返す
def page_not_found(e):
    """404 Not Found"""
    return render_template("404.html"), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template("500.html"), 500
=======
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
>>>>>>> 7675cdf78d400179db34065f305dc0df7e7bc523
