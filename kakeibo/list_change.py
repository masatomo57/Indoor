
from datetime import datetime as dt
import item_lists as il
'''
# yasai.csvを読み込む関数の定義
def read_csv(filename, item):
    count = 0
    price = []
    date = []
    data = {}
    csv_file = filename + "_converted.csv"
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[item] == '':
                price.append(None)
            else:
                price.append(row[item])
            date.append(row["DATE"])
            count += 1
    data["price"] = price
    data["date"] = date
    data["lastprice"] = price[len(price)-1]
    return data,count

def greenonion():
    name = "ねぎ"
    print(name)
    data,count = read_csv("yasai", name)
    print(count)
    label_list = data["date"]
    price_list = data["price"]
    last_price = data["lastprice"]
    if last_price != None:
        last_price = int(float(last_price))
    #print(label_list)

    conn = sqlite3.connect("kakeibo.db")
    db = conn.cursor()
    plot_data = db.execute('SELECT transacted,price FROM test_buying WHERE user_id = ? AND item = ?', ("kk",name)).fetchall()
    conn.close()
    l1,l2,l3=list_change(label_list,price_list,count,plot_data)
    print(l1)
    print(l2)
    print(l3)
'''


def list_change(label_list,price_list,count,plot_data,name):
    flag=0
    plot_list=[None for i in range(count)]#noneリストの作成
    #print(len(plot_list))
    #print(plot_list)
    #for i in range(count):
    for i in (plot_data):
        buy_day=dt.strptime(i[0],'%Y-%m-%d')
        for j in range(count):
            day=dt.strptime(label_list[j],'%Y-%m-%d')
            #print(day)
            #print(type(day))
            if buy_day < day:
                buy_dy=str(buy_day)
                buy_dy=buy_dy[0:10]
                flag=1
                label_list.insert(j,buy_dy)
                if name in il.yasai:
                    if i[3]==None:
                        pld=int(i[1]/i[2])
                    else:
                        pld=int(i[1]*il.yasai[name]/i[3])
                elif name in il.kakou:
                    if i[3]==None:
                        pld=int(i[1]/i[2])
                    else:
                        pld=int(i[1]*il.kakou[name]/i[3])
                elif name in il.sakana:
                    if i[3]==None:
                        pld=int(i[1]/i[2])
                    else:
                        pld=int(i[1]*il.sakana[name]/i[3])
                elif name in il.niku:
                    if i[3]==None:
                        pld=int(i[1]/i[2])
                    else:
                        pld=int(i[1]*il.niku[name]/i[3])
                else:
                    pld=int(i[1]/i[2])
                plot_list.insert(j,str(pld))
                ave = str((float(price_list[j-1]) + float(price_list[j])) / 2)
                # price_list.insert(j,None)
                price_list.insert(j,ave)
                break

        if flag==0 and buy_day.year >= 2020:
            buy_dy=str(buy_day)
            buy_dy=buy_dy[0:10]
            label_list.append(buy_dy)
            pld=int(i[1]/i[2])
            plot_list.append(str(pld))
            price_list.append(None)
    '''
    print(label_list)
    print(plot_list)
    print(price_list)
    print(len(label_list))
    print(len(plot_list))
    print(len(price_list))
    print(type(label_list))
    print(type(plot_list))
    print(type(price_list))
    '''
    return label_list,price_list,plot_list

#greenonion()
