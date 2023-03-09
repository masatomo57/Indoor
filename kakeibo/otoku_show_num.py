
#お得から見せるイラスト番号計算する．
import numpy as np
#お得をどの単位で区切るか決める
delim = [100000,10000,1000,100,10]


def otoku_show_num(otoku):
    show_num = []
    if otoku >= 0:
        plamai = True
        #お得がプラスの場合
        for i in delim:
            #print(i)
            ans = otoku // i
            otoku = otoku % i
            show_num.append(ans)
    else:
        #お得がマイナスの場合
        plamai = False
        otoku *= -1
        for i in delim:
            #print(i)
            ans = otoku // i
            otoku = otoku % i
            show_num.append(ans)

    return show_num, plamai

#リストを受け取る
def img_show_posi(num_list):
    posi = []
    width = 100
    height = 100
    num = 0
    for i in num_list:
        num += i
    print(num)

    while num >= len(posi):
        x_posi = np.random.randint(0,width)
        y_posi = np.random.randint(0,height)
        #if x_posi in posi
        posi.append([x_posi,y_posi])
        #重複を消す
        posi = list(map(list,set(map(tuple,posi))))
    #posi = np.random.randint(width,height,(num,2))
    print(posi)
    return posi


#num,judge = otoku_show_num(-234345)
#print(num)
#print(judge)
#posi = img_show_posi(num)
#print(posi)