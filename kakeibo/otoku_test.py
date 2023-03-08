
#-----------------------------
#川島20230305
#お得の計算コードを作ってみる
#-----------------------------

import sqlite3
from pandas import read_csv
import item_lists as il
import numpy as np
import datetime


'''
def weekly_otoku_calculate(filename, kind, database):
    conn = sqlite3.connect(database)
    db = conn.cursor()

    users = db.execute("SELECT username FROM users").fetchall()
    print(users)

    otoku_price = 0

    data=read_csv(filename, header=0)
    print('doko')
    print(data)
    items=data.columns[2:]
    print(items)

    conn.close()

def monthly_otoku_calculate(filename, kind, database):
    user_id = 'kk'
    conn = sqlite3.connect(database)
    db = conn.cursor()

    users = db.execute("SELECT username FROM users").fetchall()
    print(users)

    otoku_price = 0

    #data=read_csv(filename, header=0,index_col='DATE')
    data=read_csv(filename, header=0,index_col='DATE',parse_dates=True)
    print(data)
    print('check1')
    print(data.index)
    print(data.at[data.index[0],'食パン'])
    print(type(data.at[data.index[0],'食パン']))
    #print(data.)
    if data.index[0]>data.index[1]:
        print('a')
    else:
        print('b')
    #data2=read_csv(filename, header=0,index_col='食パン')
    #print(data2)

    #items2=data.columns[:1]
    #print(items2)

    items=data.columns[0:]
    print(items)#touple
    print(items[0])
    if items[0] == "食パン":
        print("ok")
    for i in range(len(items)):
        if items[i] in il.yasai:
            print(f'{items[i]}はyasaiです')
        elif items[i] in il.kakou:
            print(f'{items[i]}はkakouです')
        elif items[i] in il.sakana:
            print(f'{items[i]}はsakanaです')
        elif items[i] in il.niku:
            print(f'{items[i]}はnikuです')
        else:
            print(f'{items[i]}はお得を比較できません')

    kakei_data = db.execute('SELECT item,transacted,sum FROM test_buying WHERE user_id = ?', (user_id,)).fetchall()
    print('check2')
    #print(type(datetime.datetime.strptime(kakei_data[0][1])))

    dt = datetime.datetime.strptime(kakei_data[0][1],'%Y-%m-%d')
    print(dt)
    print('check3')
    print(kakei_data[0][2])
    print(type(kakei_data[0][2]))
    if data.at[data.index[0],'食パン'] > kakei_data[0][2]:
        print('買ったトマトはデータの食パンより安い')
    else:
        print('損してる')

    if dt >data.index[0]:
        print(f'{data.index[0]}の方が前')
    else:
        print(f'{data.index[0]}の方が後')

    for i in range(len(kakei_data)):
        if kakei_data[i][0] in il.yasai:
            print(f'{kakei_data[i][0]}はyasaiです')
        elif kakei_data[i][0] in il.kakou:
            print(f'{kakei_data[i][0]}はkakouです')
        elif kakei_data[i][0] in il.sakana:
            print(f'{kakei_data[i][0]}はsakanaです')
        elif kakei_data[i][0] in il.niku:
            print(f'{kakei_data[i][0]}はnikuです')
        else:
            print(f'{kakei_data[i][0]}はお得を比較できません')
    print(kakei_data[0][1])
    hi = kakei_data[0][1]
    print(hi[0])
    #if hi[2] ==

    conn.close()
'''

def otoku(username):
    user_id = username
    conn = sqlite3.connect("kakeibo.db")
    db = conn.cursor()
    userskakeibo = db.execute('SELECT item,transacted,sum,shares FROM test_buying WHERE user_id = ?', (user_id,)).fetchall()

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

    for i in range(len(userskakeibo)):
        print(f'i:{i}')
        #家計簿の品目
        item_name = userskakeibo[i][0]
        print(f'item_name:{item_name}')
        #品目を買った日付
        db_times = datetime.datetime.strptime(userskakeibo[i][1],'%Y-%m-%d')
        print(f'db_times:{db_times}')

        #商品が野菜なら野菜データと比較
        if item_name in il.yasai:
            #野菜csvのどの時間と比較すべきか探す
            for j in range(len(yasai_data)):
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < yasai_data.index[j] and np.isnan(yasai_data.at[yasai_data.index[j],item_name]) != True:
                    otoku_price = yasai_data.at[yasai_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
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
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < kakou_data.index[j] and np.isnan(kakou_data.at[kakou_data.index[j],item_name]) != True:
                    otoku_price = kakou_data.at[kakou_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                    kakou_otoku_price += otoku_price
                    break
                    #otoku_price = 0
        #商品が魚なら魚データと比較
        elif item_name in il.sakana:
            #加工csvのどの時間と比較すべきか探す
            for j in range(len(sakana_data)):
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < sakana_data.index[j] and np.isnan(sakana_data.at[sakana_data.index[j],item_name]) != True:
                    otoku_price = sakana_data.at[sakana_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
                    sakana_otoku_price += otoku_price
                    break
                    #otoku_price = 0
        #商品が肉なら肉データと比較
        elif item_name in il.niku:
            #加工csvのどの時間と比較すべきか探す
            for j in range(len(niku_data)):
                #csvが古い年代から新しい年代にソートされている前提
                if db_times < niku_data.index[j] and np.isnan(niku_data.at[niku_data.index[j],item_name]) != True:
                    otoku_price = niku_data.at[niku_data.index[j],item_name] - (userskakeibo[i][2] / userskakeibo[i][3])
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
    return yasai_otoku_price, kakou_otoku_price, sakana_otoku_price, niku_otoku_price, total_otoku_price



# 毎週水曜日0時に実行する。前週月曜日から日曜日までのお得を計算する。
#weekly_otoku_calculate("yasai.csv", "野菜", "kakeibo.db")
# 毎月1日0時に実行する。先月1日から末日までのお得を計算する。
#monthly_otoku_calculate("kakou_converted.csv", "加工食品", "kakeibo.db")

#user_name = 'kk'
#otoku(user_name)

