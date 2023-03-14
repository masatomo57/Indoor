import secrets

# BaseConfigクラスを作成する
class BaseConfig:
    # SECRET_KEYは、自由に変更してOK!
    SECRET_KEY = secrets.token_hex(32)
    WTF_CSRF_SECRET_KEY = secrets.token_hex(32)

# BaseConfigクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# config辞書にマッピングする
config = {
    "local": LocalConfig,
    "base": BaseConfig,
}
