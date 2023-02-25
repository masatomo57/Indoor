#実行に2分くらいかかる場合があるので、気長に待ってください
#get_kakou_data() で最新版と過去のデータを取得し、DateFrame型で返します。このときkakou.csvが作成されます。
#このcsvファイルが存在する状況で
#reload_kakou_data(csv_file, name) を実行すると、最新データを新たに取得して、csvファイルに結合します。これは毎月の更新作業時に使用します。

#ライブラリのインストール
import requests
from tika import parser
import pandas as pd
import re
from IPython.lib.display import splitext
import bs4
import datetime

#=================================================================

def download_pdf(url):
  # sample.pdfとしてダウンロード
  filename='sample.pdf'
  urlData = requests.get(url).content
  with open(filename ,mode='wb') as f:
    f.write(urlData)

#=================================================================

def to_datetime(date):
  # 平成元年を平成1年に変換
  if date[1] == "元":
    date[1] = 1

  #不要部分を削除
  del date[0]
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
  date = datetime.date(date[0], date[2], 1)

  return date

#=================================================================

def read_pdf(text):
  spilit_sentence = re.split('[\n]', text)

  try:
    for i in range(len(spilit_sentence)):
      if "◆" in spilit_sentence[i]:
        contain_date = spilit_sentence[i]
      elif "円/kg 円/個" in spilit_sentence[i]:
        contain_a = spilit_sentence[i + 2]
      elif "円/500g" in spilit_sentence[i]:
        contain_b = spilit_sentence[i + 2]

    date = re.split('[【】]', contain_date)
    # 平成/令和〇年〇月〇日の週

    # 成、和、年、月、日で文字列を分割
    date = re.split('[ 成和年月⽉（）]', date[0])

    date = to_datetime(date)

    a = re.split('[ ]', contain_a)
    b = re.split('[ ]', contain_b)

    for i in range(len(b)):
      a.append(b[i])

    # 数字を浮動小数点型に変換
    for i in range(len(a)):
      a[i] = float(a[i])

    data = [[date]]
    for i in range(len(a)):
      data[0].append(a[i])

    #確認用
    #print(data)

    return data

  except:
    pass

#=================================================================

def read_new_pdf(text):
  spilit_sentence = re.split('[\n]', text)

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

    for i in range(len(b)):
      a.append(b[i])

    # 数字を浮動小数点型に変換
    for i in range(len(a)):
      a[i] = float(a[i])

    return a

  except:
    pass

#=================================================================

def taking_new_kakou_data(url_only=False):
  # データを提供してくれる農林水産省のページの読み込み
  url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/gaiyou.html"
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
    if "【" in candidate_list[i].text:
      url = candidate_list[i].attrs["href"]
      date = candidate_list[i].text
    elif "過去の調査結果" in candidate_list[i].text:
      url_to_list = candidate_list[i].attrs["href"]
      url_to_list = "https://www.maff.go.jp" + url_to_list

      if url_only==True:
        return url_to_list

    else:
      pass

  # 農林水産省が提供するデータのダウンロードリンク
  url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri" + url[1:]

  # 農林水産省が提供するデータのダウンロードリンク
  #url = "https://www.maff.go.jp/j/zyukyu/anpo/kouri/attach/pdf/gaiyou-9.pdf"

  download_pdf(url)

  date = re.split('[【】]', date)
  # 平成/令和〇年〇月〇日の週

  # 成、和、年、月、日で文字列を分割
  date = re.split('[成和年月日]', date[0])
  date_ = ["調整用のdate[0]"]
  for i in range(len(date)):
    date_.append(date[i])
  date = date_

  date = to_datetime(date)

  file_data = parser.from_file("sample.pdf")
  text = file_data["content"]

  a = read_new_pdf(text)

  data = [[date]]
  for i in range(len(a)):
    data[0].append(a[i])

  return data

#=================================================================

def take_new_kakou_data():

  data = taking_new_kakou_data()

  df = pd.DataFrame(columns = name)
  df1 = pd.DataFrame(data, columns = name)
  df = pd.concat([df, df1], axis=0)

  return df

#=================================================================

def take_past_kakou_data():
  url_to_list = taking_new_kakou_data(url_only=True)
  res_list = requests.get(url_to_list)
  html_text_list = bs4.BeautifulSoup(res_list.text, 'html.parser')

  df = pd.DataFrame(columns = name)

  for i in range(len(html_text_list.find_all("a"))):
    if "月分" in html_text_list.find_all("a")[i].text:

      url_to_pdf = html_text_list.find_all("a")[i].attrs["href"]
      url_to_pdf = "https://www.maff.go.jp/j/zyukyu/anpo/kouri" + url_to_pdf[1:]

      download_pdf(url_to_pdf)

      file_data = parser.from_file("sample.pdf")
      text = file_data["content"]

      data = read_pdf(text)

      df1 = pd.DataFrame(data, columns = name)
      df = pd.concat([df, df1], axis=0)

  return df

#=================================================================

def get_kakou_data():
  df = pd.concat([take_new_kakou_data(), take_past_kakou_data()], axis=0)
  df.to_csv("kakou.csv")
  return df

#=================================================================

def reload_kakou_data(csv_file, name):
  DF = pd.read_csv(csv_file)
  DF = DF.drop('Unnamed: 0', axis=1)
  df = pd.DataFrame(columns = name)
  data = taking_new_kakou_data()
  df1 = pd.DataFrame(data, columns = name)
  df = pd.concat([df, df1], axis=0)
  DF = pd.concat([DF, df], axis=0)
  DF.to_csv("kakou.csv")
  return DF

#=================================================================

name = ["DATE", "食パン","即席めん","ゆでうどん","小麦粉","牛乳","チーズ","豆腐","食用油（キャノーラ油）","食用油（サラダ油）","マーガリン","マヨネーズ","しょう油","みそ","かまぼこ","まぐろ缶詰","バター"]

#=================================================================

#動作確認用
get_kakou_data()
#reload_kakou_data("/content/kakou.csv", name)