from flask import Flask, render_template, g, flash, redirect, request, url_for

app = Flask(__name__)


# データベースを呼び出す関数の定義、データベースができたらコメントアウト外してください。
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db')
    return g.db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/login")
def login():
    return render_template("login.html")