import pandas as pd
import datetime
import re
from prophet import Prophet

# 時系列予測
def predict_price(address, yasai_price=True):

  # df を作成
  df = pd.read_csv(address)

  prediction = [] # 予測した価格を格納

  for i in range(1, df.shape[1]):
    column_name = df.columns[i]

    # データフレームの作成
    df_prophet = pd.DataFrame({'ds': df[df.columns[0]].values, 'y': df[column_name].values})

    model = Prophet()
    model.fit(df_prophet)

    # 未来の日付を定義
    future = model.make_future_dataframe(periods=7 if yasai_price else 30, freq='D')

    # 予測
    forecast = model.predict(future)

    # 最後の予測値を取得
    prediction.append(forecast.iloc[-1]['yhat'])

  predict_data = {}
  predict_data_plus = {}

  for i in range(1, df.shape[1]):
    predict_data[df.columns[i]] =  prediction[i - 1]

    if df.iloc[-1, i] < prediction[i - 1]:
      predict_data_plus[df.columns[i]] =  "上昇傾向"
    elif df.iloc[-1, i] > prediction[i - 1]:
      predict_data_plus[df.columns[i]] =  "下降傾向"
    else:
      # 最新のデータがない
      predict_data_plus[df.columns[i]] =  "同じくらい"

  # predict_data ならば予測値、predict_data_plus なら傾向
  return predict_data_plus
