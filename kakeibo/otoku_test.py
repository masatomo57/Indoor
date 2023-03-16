
#-----------------------------
#川島20230305
#お得の計算コードを作ってみる
#-----------------------------

import sqlite3
from pandas import read_csv
import item_lists as il
import numpy as np
import datetime


def otoku(username):
    user_id = username
    conn = sqlite3.connect("kakeibo.db")
    db = conn.cursor()
    userskakeibo = db.execute('SELECT item,transacted,price,shares,gram FROM test_buying WHERE user_id = ?', (user_id,)).fetchall()
    print(userskakeibo)

    yasai_data=read_csv("yasai_converted.csv", header=0,index_col='DATE',parse_dates=True)
    kakou_data=read_csv("kakou_converted.csv", header=0,index_col='DATE',parse_dates=True)
    sakana_data=read_csv("sakana_converted.csv", header=0,index_col='DATE',parse_dates=True)
    niku_data=read_csv("niku_converted.csv", header=0,index_col='DATE',parse_dates=True)

    yasai_otoku_price = 0
    kakou_otoku_price = 0
    sakana_otoku_price = 0
    niku_otoku_price = 0
    total_otoku_price = 0

    otoku_price = 0
    point_yasai = 0
    point_kakou = 0
    point_sakana = 0
    point_niku = 0

    for i in range(len(userskakeibo)):
        #家計簿の品目
        item_name = userskakeibo[i][0]
        #品目を買った日付
        db_times = datetime.datetime.strptime(userskakeibo[i][1],'%Y-%m-%d')
        #print(f'db_times:{db_times}')

        #商品が野菜なら野菜データと比較
        if item_name in il.yasai:
            #野菜csvのどの時間と比較すべきか探す
            for j in range(len(yasai_data)):
                #csvが古い年代から新しい年代にソートされている前提
                csv_times=yasai_data.index[j].to_pydatetime()
                if db_times < csv_times:
                    #ポイント計算
                    if yasai_data.at[yasai_data.index[j-1],item_name]-yasai_data.at[yasai_data.index[j],item_name] >0:
                        point_yasai +=1
                    if np.isnan(yasai_data.at[yasai_data.index[j],item_name]) == True:
                        #print(f'{item_name}はお得を計算できなかった')
                        break
                    else:
                        if userskakeibo[i][4] == None:
                            #print('gramなし')
                            otoku_price = yasai_data.at[yasai_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        else:
                            #print('gramあり')
                            otoku_price = yasai_data.at[yasai_data.index[j],item_name]*(userskakeibo[i][4]/il.yasai[item_name]) - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        '''
                        print(f'yasai_name:{item_name}')
                        print(f'kakeibo_price:{userskakeibo[i][2]}')
                        print(f'shares:{userskakeibo[i][3]}')
                        print(f'yasai_data_price:{yasai_data.at[yasai_data.index[j],item_name]}')
                        print(f'otoku_price:{otoku_price}')
                        '''
                        yasai_otoku_price += otoku_price
                        break
                    #otoku_price = 0
        #商品が加工食品なら加工食品データと比較
        elif item_name in il.kakou:
            #加工csvのどの時間と比較すべきか探す
            for j in range(len(kakou_data)):
                csv_times=kakou_data.index[j].to_pydatetime()
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < csv_times:
                    #ポイント計算
                    if kakou_data.at[kakou_data.index[j-1],item_name] - kakou_data.at[kakou_data.index[j],item_name] >0:
                        point_kakou +=1
                    if np.isnan(kakou_data.at[kakou_data.index[j],item_name]) == True:
                        break
                    else:
                        if userskakeibo[i][4] == None:
                            otoku_price = kakou_data.at[kakou_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        else:
                            otoku_price = kakou_data.at[kakou_data.index[j],item_name]*(userskakeibo[i][4]/il.kakou[item_name]) - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        kakou_otoku_price += otoku_price
                        break
                    #otoku_price = 0
        #商品が魚なら魚データと比較
        elif item_name in il.sakana:
            #加工csvのどの時間と比較すべきか探す
            for j in range(len(sakana_data)):
                csv_times=sakana_data.index[j].to_pydatetime()
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < csv_times:
                    #ポイント計算
                    if sakana_data.at[sakana_data.index[j-1],item_name] -sakana_data.at[sakana_data.index[j],item_name] >0:
                        point_sakana +=1
                    if np.isnan(sakana_data.at[sakana_data.index[j],item_name]) == True:
                        break
                    else:
                        if userskakeibo[i][4] == None:
                            otoku_price = sakana_data.at[sakana_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        else:
                            otoku_price = sakana_data.at[sakana_data.index[j],item_name]*(userskakeibo[i][4]/il.sakana[item_name]) - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        sakana_otoku_price += otoku_price
                        break
                    #otoku_price = 0
        #商品が肉なら肉データと比較
        elif item_name in il.niku:
            #加工csvのどの時間と比較すべきか探す
            for j in range(len(niku_data)):
                csv_times=niku_data.index[j].to_pydatetime()
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < csv_times:
                    #ポイント計算
                    if niku_data.at[niku_data.index[j-1],item_name] -niku_data.at[niku_data.index[j],item_name] >0:
                        point_niku += 1
                    if np.isnan(niku_data.at[niku_data.index[j],item_name]) == True:
                        break
                    else:
                        if userskakeibo[i][4] == None:
                            otoku_price = niku_data.at[niku_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        else:
                            otoku_price = niku_data.at[niku_data.index[j],item_name]*(userskakeibo[i][4]/il.niku[item_name]) - (userskakeibo[i][2] / userskakeibo[i][3])
                            otoku_price = userskakeibo[i][3] * otoku_price
                        niku_otoku_price += otoku_price
                        break
                    #otoku_price = 0
    #データベースを閉じる
    conn.close()

    #お得の総計を計算
    total_otoku_price = yasai_otoku_price + kakou_otoku_price + sakana_otoku_price + niku_otoku_price
    total_otoku_price = np.trunc(total_otoku_price)
    yasai_otoku_price = np.trunc(yasai_otoku_price)
    kakou_otoku_price = np.trunc(kakou_otoku_price)
    sakana_otoku_price = np.trunc(sakana_otoku_price)
    niku_otoku_price = np.trunc(niku_otoku_price)
    '''
    print(f'yasai:{yasai_otoku_price}')
    print(f'kakou:{kakou_otoku_price}')
    print(f'sakana:{sakana_otoku_price}')
    print(f'niku:{niku_otoku_price}')
    print(f'total:{total_otoku_price}')
    '''
    return yasai_otoku_price, kakou_otoku_price, sakana_otoku_price, niku_otoku_price, total_otoku_price, point_yasai, point_kakou, point_sakana, point_niku

#user_name = 'kk'
#ans = otoku(user_name)
#print(ans)
