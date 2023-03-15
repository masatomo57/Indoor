#ライブラリのインストール
import requests
from tika import parser
import pandas as pd
import re
from IPython.lib.display import splitext
import bs4
import datetime
import numpy as np

#=========================================

def download_pdf(url):
  # sample.pdfとしてダウンロード
  filename='sample.pdf'
  urlData = requests.get(url).content
  with open(filename ,mode='wb') as f:
    f.write(urlData)

#=========================================

def get_date(date, day=True):

  # day=True ならば datetime.date(年, 月, 日)
  # day=False ならば datetime.date(年, 月, 1)
  # が返ってくる


  date = re.split('[【】]', date)
  date = re.split('[成和年月日]', date[0])
  date_ = ["調整用のdate[0]"]
  for i in range(len(date)):
    date_.append(date[i])
  date = date_

  if date[1] == "元":
    date[1] = 1

  #不要部分を削除
  del date[0]
  if day == True:
    del date[4:]
  else:
    del date[3:]



  # 数字を数値型に変換
  for i in range(1, len(date)):
    date[i] = int(date[i])

  # 西暦に変換
  if date[0] == "平":
    date[0] = 1988 + date[1]
  elif date[0] == "令":
    date[0] = 2018 + date[1]

  # date型に変換
  if day == True:
    date = datetime.date(date[0], date[2], date[3])
  else:
    date = datetime.date(date[0], date[2], 1)


  return date

#=========================================

def taking_new_data(word, date_=True, url_=False):
  # データを提供してくれる農林水産省のページの読み込み
  yasai_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_yasai/h22index.html"
  yasai_to_pdf_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_yasai"

  kakou_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/gaiyou.html"
  kakou_to_pdf_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri"

  niku_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_gyuniku/index.html"
  niku_to_pdf_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_gyuniku"

  sakana_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_gyuniku/fish/index.html"
  sakana_to_pdf_url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/k_gyuniku/fish"

  if word == "yasai":
    url = yasai_url
    to_pdf_url = yasai_to_pdf_url
  elif word == "kakou":
    url = kakou_url
    to_pdf_url = kakou_to_pdf_url
  elif word == "niku":
    url = niku_url
    to_pdf_url = niku_to_pdf_url
  elif word == "sakana":
    url = sakana_url
    to_pdf_url = sakana_to_pdf_url
  else:
    print('引数として"yasai", "kakou", "niku", "sakana"から取得したいデータに関する単語を1つ入力してください。')
    return

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

  # 新たに配布されたpdfを探す
  for i in range(len(candidate_list)):
    if "【" in candidate_list[i].text:
      if "過去" in candidate_list[i].text:
        pass
      elif "品目" in candidate_list[i].text:
        pass
      else:
        url = candidate_list[i].attrs["href"]
        date = candidate_list[i].text

  to_pdf_url += url[1:]

  if word == "yasai":
    date = get_date(date, day=True)
  else:
    date = get_date(date, day=False)

  if date_ == True and url_ == False:
    return date
  elif date_ == False and url_ == True:
    return to_pdf_url
  else:
    return None

#=========================================

def get_new_date(word, date, to_pdf_url):
  download_pdf(to_pdf_url)
  file_data = parser.from_file("sample.pdf")
  text = file_data["content"]
  spilit_sentence = re.split('[\n]', text)

  if word == "yasai":
    for i in range(len(spilit_sentence)):
      if "キャベツ ねぎ" in spilit_sentence[i]:
        names = spilit_sentence[i]
        names = re.split('[ ]', names)
        #columns = [["DATE"]]
        columns = ["DATE"]
        for j in range(len(names)):
          #columns[0].append(names[j])
          columns.append(names[j])


  elif word == "kakou":
    columns = ["DATE", "食パン","即席めん","ゆでうどん","小麦粉","牛乳","チーズ","豆腐","食用油（キャノーラ油）","食用油（サラダ油）","マーガリン","マヨネーズ","しょう油","みそ","かまぼこ","まぐろ缶詰","バター"]

  elif word == "niku":
    columns = ["DATE", "輸入牛肉（冷蔵ロース）", "国産牛肉（冷蔵ロース）", "豚肉（ロース）", "鶏肉（もも肉）", "鶏卵（サイズ混合・10個入り）"]

  elif word == "sakana":
    columns = ["DATE", "まぐろ", "えび", "ぶり", "さけ"]


  if word == "yasai":
    for i in range(len(spilit_sentence)):
      if "価格 " in spilit_sentence[i]:
        prices = spilit_sentence[i]
        prices = re.split('[ ]', prices)
        del prices[0]
        for j in range(len(prices)):
          prices[j] = int(prices[j])
        mod = [1.2, 0.1, 0.3, 0.2, 0.175, 0.175, 2, 1]
        prices = np.multiply(prices,mod)
        data = [[date]]
        for j in range(len(prices)):
          #prices[j] = int(prices[j])
          data[0].append(prices[j])

  elif word == "kakou":
    try:
      for i in range(len(spilit_sentence)):
        if "◆" in spilit_sentence[i]:
          contain_date = spilit_sentence[i]
        elif "円/kg 円/個" in spilit_sentence[i]:
          contain_a = spilit_sentence[i + 2]
        elif "円/500g" in spilit_sentence[i]:
          contain_b = spilit_sentence[i + 2]

      a = re.split('[ ]', contain_a)
      b = re.split('[ ]', contain_b)

      data = [[date]]
      for i in range(len(b)):
        a.append(b[i])

      # 数字を浮動小数点型に変換
      for j in range(len(a)):
        a[j] = float(a[j])
      mod = [0.37, 1, 2, 1, 1, 1.35, 3.5, 1, 1, 1, 0.9, 1, 0.75, 1, 1, 1]
      a = np.multiply(a,mod)
      data = [[date]]
      for i in range(len(a)):
        #a[i] = float(a[i])
        data[0].append(a[i])


    except:
      pass

  else:
    for i in range(len(spilit_sentence)):
      if "価格 " in spilit_sentence[i]:
        prices = spilit_sentence[i]
        prices = re.split('[ ]', prices)
        del prices[0]
        data = [[date]]
        for j in range(len(prices)):
          prices[j] = int(prices[j])
          data[0].append(prices[j])

  df = pd.DataFrame(columns = columns)
  df1 = pd.DataFrame(data, columns = columns)
  df = pd.concat([df, df1], axis=0)

  if word == "yasai":
    df["ばれいしょ"] = np.nan
    df["きゅうり"] = np.nan
    df["ほうれんそう"] = np.nan
    df["なす"] = np.nan
    df = df[['DATE', 'キャベツ', 'ねぎ', 'レタス', 'ばれいしょ', 'たまねぎ', 'きゅうり', 'トマト', 'ほうれんそう', 'にんじん', 'はくさい', 'だいこん', 'なす']]



  return df

#=========================================

def merge_csv(word):

  # 蓄積データがまとまったcsvファイルのパスを指定

  if word == "yasai":
    csv = pd.read_csv("/workspaces/Indoor/kakeibo/yasai_converted.csv")
  elif word == "kakou":
    csv = pd.read_csv("/workspaces/Indoor/kakeibo/kakou_converted.csv")
  elif word == "niku":
    csv = pd.read_csv("/workspaces/Indoor/kakeibo/niku_converted.csv")
  elif word == "sakana":
    csv = pd.read_csv("/workspaces/Indoor/kakeibo/sakana_converted.csv")
  else:
    print('引数として"yasai", "kakou", "niku", "sakana"から取得したいデータに関する単語を1つ入力してください。')
    return

  if "Unnamed: 0" in csv.columns[0]:
    csv = csv.drop("Unnamed: 0", axis=1)

  date = taking_new_data(word, date_=True, url_=False)
  #print(date)
  url = taking_new_data(word, date_=False, url_=True)
  df = get_new_date(word, date, url)
  #print(df.iloc[-1, 0])

  merged = pd.concat([csv, df], axis=0)
  merged = merged.reset_index()
  merged = merged.drop("index", axis=1)

  if date == df.iloc[-1, 0]:
    print(word,":すでに最新データが反映されています")
    return None

  #words = "/workspaces/Indoor/kakeibo/" + word + "_converted.csv"
  #テスト用↓
  words = "/workspaces/Indoor/kakeibo/" + word + "_converted1.csv"

  merged.to_csv(words, index=False)
  print(word,":データを更新しました")

  #return merged
  # return はテスト用

#=========================================

merge_csv("yasai")