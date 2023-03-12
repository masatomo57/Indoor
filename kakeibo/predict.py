#predict_price("/workspaces/Indoor/kakeibo/yasai_converted.csv", yasai_price=True)
#predict_price("/workspaces/Indoor/kakeibo/kakou_converted.csv", yasai_price=False)

# return が predict_data ならば予測値、predict_data_plus なら傾向を辞書系列で返す

#{'キャベツ': 177.4668072974555, 'ねぎ': 74.09617564745292, 'レタス': 123.92756996493614, 'ばれいしょ': 65.2357645647186, 'たまねぎ': 66.63329346924168, 'きゅうり': 58.02403955106861, 'トマト': 127.46279081116462, 'ほうれんそう': 175.59874831185013, 'にんじん': 68.70982042041148, 'はくさい': 89.07952593837898, 'だいこん': 176.19647309436516, 'なす': 60.83681133282948}

import pandas as pd
#import matplotlib.pyplot as plt
import datetime
import re
from sklearn.linear_model import LinearRegression

def predict_price(address, yasai_price=True):
  # 単回帰分析（線形）

  # df を作成
  df = pd.read_csv(address)

  # NaN を interpolate で前後の値から補完、fillna で平均値で補完
  df = df.interpolate()
  df = df.fillna(df.mean())

  # 年月日表示を最初にデータを得られた年を基準とした大まかな日数に変換
  DATE = [] # 日数を格納
  std = 0 # 基準とする年を格納する（野菜についての df ならば 2017 になるはず）
  for i in range(df.shape[0]):
    text = df.iloc[i, 0]
    text = re.split('[/-]', text)
    for j in range(len(text)):
      text[j] = int(text[j]) # 文字型から整数型に変換
      if i == 0 and j == 0:
        std = text[0] # 基準の年を取得
        #print("確認用 std:", std)
    text[0] = (text[0] - std) * 365
    text[1] = text[1] * 30.42
    text = text[0] + text[1] + text[2]
    #text = datetime.date(text[0],text[1], text[2])
    DATE.append(text)
  DATE = pd.Series(DATE).values # 値だけを取得

  prediction = [] # 予測した価格を格納

  for i in range(1, df.shape[1]):
    column_name = df.columns[i]

    target = df[column_name].values.reshape(-1,1)
    data = DATE.reshape(-1,1)

    clf = LinearRegression()
    clf.fit(data, target)

    # 描画用の記述
    #p_lin = clf.predict(data)
    #plt.scatter(data, target, label='data')
    #plt.plot(data, p_lin, color='darkorange', marker='', linestyle='-', linewidth=1, markersize=6, label='linear regression')
    #plt.legend()
    #print(clf.score(data, target))

    # 野菜の df ならば1週間ごとに更新なので、+7、それ以外は1か月更新なのでひと月の平均日数の +30.42
    if yasai_price == True:
      T = DATE[len(DATE)-1] + 7
    else:
      T = DATE[len(DATE)-1] + 30.42

    # 成型
    D = pd.Series(T)
    D = D.values.reshape(-1, 1)

    # 確認用
    #print(clf.predict(D)[0][0])

    # 確認用
    #print(column_name, clf.predict(D)[0][0])

    prediction.append(clf.predict(D)[0][0])

  predict_data = {}
  predict_data_plus = {}

  for i in range(1, df.shape[1]):
    predict_data[df.columns[i]] =  prediction[i - 1]

    if df.iloc[-1, i] < prediction[i - 1]:
      predict_data_plus[df.columns[i]] =  "上昇傾向"
    elif df.iloc[-1, i] > prediction[i - 1]:
      predict_data_plus[df.columns[i]] =  "下降傾向"
    else:
      predict_data_plus[df.columns[i]] =  "同じくらい"

  # predict_data ならば予測値、predict_data_plus なら傾向
  return predict_data_plus

#確認用
print(predict_price("/workspaces/Indoor/kakeibo/yasai_converted.csv", yasai_price=True))