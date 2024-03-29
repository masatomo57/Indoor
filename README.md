# おトクに！家計簿
## Overview
あなたがどれだけおトクに買い物できたかがわかる、家計簿Webアプリケーション。
CODEGYM Academy 2022秋のチーム開発で開発したものです。

## Description
家計簿に買ったもののデータを登録し、農林水産省が公開している食品の価格動向のデータ
https://www.maff.go.jp/j/zyukyu/anpo/kouri/
と比較してあなたがどれだけおトクに買い物できたかどうかがわかります。このWebアプリケーションは大きく4つのページからなります。

### ホーム画面
今までに貯めたおトクの総計、カテゴリーごとのおトクの総計を数字とイラストで見ることができます。

### 物価チャート画面
価格動向のデータを最もメジャーな単位に変換してチャートにして表示しています。

### データ登録画面
買ったものを登録することができます。農林水産省で公開されているデータ以外も登録ができます。個数は1/2や1/4も選択できます。

### 家計簿
買った金額をカレンダー上で見ることができます。

## Requirements
Flask
Flask-Session
requests
Flask-WTF
Flask-Login
flask-wtf
Flask-Mail
Werkzeug
WTForms
email_validator
beautifulsoup4
requests
bs4
pandas
numpy
datetime
schedule
tika
ipython
openpyxl
scikit-learn

```
pip install -r requirements.txt
```

## Usage
```
git clone https://github.com/masatomo57/Indoor.git
```
