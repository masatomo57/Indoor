# ライブラリのインストール
#!pip install beautifulsoup4
#!pip install openpyxl

#必要に応じて以下でインポートしているライブラリもインストールしてください

# ライブラリのインポート
import requests
import bs4
import pandas as pd
import numpy as np
import re
import datetime

# 農林水産省が調査した野菜に関するデータを、pandasのデータフレーム型で返す関数
def get_data():

    # データを提供してくれる農林水産省のページの読み込み
    url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_yasai/h22index.html"
    res = requests.get(url)
    html_text = bs4.BeautifulSoup(res.text, 'html.parser')

    # aタグの〇〇行目 多分[221]で出る 保険として周辺2行ずつ確認
    candidate1 = html_text.find_all("a")[219]
    candidate2 = html_text.find_all("a")[220]
    candidate3 = html_text.find_all("a")[221]
    candidate4 = html_text.find_all("a")[222]
    candidate5 = html_text.find_all("a")[223]

    # 候補をリストに格納
    candidate_list = [candidate1, candidate2, candidate3, candidate4, candidate5]

    # 「価格推移グラフのバックデータ(EXCEL : 99KB)」を狙い撃つ
    for i in range(len(candidate_list)):
        if "価格推移" in candidate_list[i].text:
            url = candidate_list[i].attrs["href"]
        else:
            pass

    # 農林水産省が提供するデータのダウンロードリンク
    url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_yasai" + url[1:]

    # 農林水産省が提供するデータのダウンロードリンク
    #url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_yasai/attach/xls/h22index-57.xlsx"

    # data.xlsxとしてダウンロード
    filename='yasai_data.xlsx'
    urlData = requests.get(url).content
    with open(filename ,mode='wb') as f:
        f.write(urlData)

    # data.xlsxをpandasのデータフレーム型で読み込む
    df = pd.read_excel('yasai_data.xlsx', index_col=0, header=1)

    # データフレーム内の不要な部分を削除
    df1 = df.dropna(how='all').dropna(how='all', axis=0)

    # データ抜け部分のうち、「-」で置換されている部分を空にする
    df1.replace("-", np.nan, inplace=True)

    # 一旦csvファイルとして出力
    df1.to_csv('data1.csv')

    # 出力したcsvファイルをデータフレーム型で読み込む（日付部分のカラム名を作成）
    df2 = pd.read_csv("data1.csv")

    # 日付データをdatetimeのdate型に変換したものを格納しておくリスト
    date_list = []

    # リスト内にdate型のデータを格納
    for i in range(len(df2)):

        # 平成/令和〇年〇月〇日の週
        sentence = df2.iloc[i, 0]

        # 成、和、年、月、日で文字列を分割
        spilited_sentence = re.split('[成和年月日]', sentence)

        # 平成元年を平成1年に変換
        if spilited_sentence[1] == "元":
            spilited_sentence[1] = 1

        # 「の週」の部分を削除
        del spilited_sentence[-1]

        # 数字を数値型に変換
        for i in range(1, len(spilited_sentence)):
            spilited_sentence[i] = int(spilited_sentence[i])

        # 西暦に変換
        if spilited_sentence[0] == "平":
            spilited_sentence[0] = 1988 + spilited_sentence[1]
        elif spilited_sentence[0] == "令":
            spilited_sentence[0] = 2018 + spilited_sentence[1]

        # date型に変換
        date_data = datetime.date(spilited_sentence[0], spilited_sentence[2], spilited_sentence[3])

        # リストに追加
        date_list.append(date_data)

    # データフレームにDATEカラムを作成し、そこにリストの内容を格納
    df2["DATE"]= date_list

    # DATEカラムを一番左側に移動させ、もともと日付の入っていたカラムを削除
    df2 = df2[['DATE', 'キャベツ', 'ねぎ', 'レタス', 'ばれいしょ', 'たまねぎ', 'きゅうり', 'トマト', 'ほうれんそう', 'にんじん', 'はくさい', 'だいこん', 'なす']]

    df2.to_csv('DATA.csv')

    return df2

#動作テスト用
#print(get_data())
