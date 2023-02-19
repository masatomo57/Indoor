from flask import Flask, render_template, g, flash, redirect, request, url_for
from forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, LoginManager
from flask_wtf.csrf import CSRFProtect

from config import config

csrf = CSRFProtect()
# LoginManagerをインスタンス化する
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "signup"
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

    # カスタムエラー画面を登録する
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    return app


# データベースを呼び出す関数の定義、データベースができたらコメントアウト外してください。
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('birthdays.db')
    return g.db


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # SignUpFormをインスタンス化する
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # メールアドレス重複チェックをする
        if user.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです")
            return redirect(url_for("auth.signup"))

        # ユーザー情報を登録する
        db.session.add(user)
        db.session.commit()

        # ユーザー情報をセッションに格納する
        login_user(user)

        # GETパラメータにnextキーが存在し、値がない場合はユーザーの一覧ページへリダイレクトする
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("detector.index")
        return redirect(next_)

    return render_template("auth/signup.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # メールアドレスからユーザーを取得する
        user = User.query.filter_by(email=form.email.data).first()

        # ユーザーが存在しパスワードが一致する場合はログインを許可する
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))

        # ログイン失敗メッセージを設定する
        flash("メールアドレスかパスワードか不正です")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/charts")
def charts():
    return render_template("charts.html")
'''
from app import db
from auth.forms import LoginForm, SignUpForm
from crud.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

# Blueprintを使ってauthを生成する
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


# indexエンドポイントを作成する
@auth.route("/")
def index():
    return render_template("auth/index.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    # SignUpFormをインスタンス化する
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # メールアドレス重複チェックをする
        if user.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです")
            return redirect(url_for("auth.signup"))

        # ユーザー情報を登録する
        db.session.add(user)
        db.session.commit()

        # ユーザー情報をセッションに格納する
        login_user(user)

        # GETパラメータにnextキーが存在し、値がない場合はユーザーの一覧ページへリダイレクトする
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("index")
        return redirect(next_)

    return render_template("auth/signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # メールアドレスからユーザーを取得する
        user = User.query.filter_by(email=form.email.data).first()

        # ユーザーが存在しパスワードが一致する場合はログインを許可する
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))

        # ログイン失敗メッセージを設定する
        flash("メールアドレスかパスワードか不正です")
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

 '''