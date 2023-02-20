import os

from flask import Flask, render_template, flash, redirect, request, url_for, session, g
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import apology, login_required, tax
from forms import LoginForm, SignUpForm
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECret_KEY'] = os.urandom(16)
# Custom filter
app.jinja_env.filters["tax"] = tax

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

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/charts")
@login_required
def charts():
    return render_template("charts.html")


@app.route("/kakeibo")
@login_required
def kakeibo():
    return render_template("kakeibo.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    form = LoginForm()
    if form.validate_on_submit():
        # process form data
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

'''
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
'''

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