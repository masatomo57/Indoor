
#お得から見せるイラスト番号を計算する．
#ホーム画面はgifで動きをつけたいが，処理速度が遅くなってしまい，見送った．今後のアップデート候補としてこのコードを残す．
import numpy as np
from PIL import Image
#お得をどの単位で区切るか決める
df_num = [10,10,5,3,2,0]
#show_num = [0,0,0,0,0,0]

#お得額を入れる
def otoku_show_num(otoku):
    show_num = [0,0,0,0,0,0]
    otoku=int(otoku)
    #print(type(otoku))
    #show_num = []
    if otoku >= 0:
        plamai = True
        otoku_len = len(str(otoku))
        #print(f'otoku_len:{otoku_len}')
        if otoku_len >= 6:
            otoku_len = 6
        for i in range(-1,-1*otoku_len -1,-1):
            #print(i)
            show_num[i]=df_num[i]
        #print(f'ans-i:{show_num}')

        ans =str(otoku)

        if otoku_len == 2:
            ans =str(otoku)
            if int(ans[-2]) <= 5:
                show_num[-2]=1
        if otoku_len == 3:
            if int(ans[-3]) <= 3:
                show_num[-3]=1
            elif int(ans[-3])<=6:
                show_num[-3]=2
        if otoku_len == 4:
            pu = int(int(ans[-4])/2 + 1)
            show_num[-4]=pu
        if otoku_len == 5:
            pu =int(ans[-5])
            show_num[-5]=pu
        if otoku_len >= 6:
            pu =int(ans[-6])
            show_num[-6]=pu
        #print(f'40:{show_num}')

    else:
        #お得がマイナスの場合
        plamai = False
        otoku = 0#強制的にお得価格を0にすることで何もプロットしないようにする，アップデートを考え中
        #otoku *= -1
        otoku_len = len(str(otoku))
        #print(f'otoku_len:{otoku_len}')
        if otoku_len >= 6:
            otoku_len = 6
        for i in range(-1,-1*otoku_len -1,-1):
            show_num[i]=df_num[i]
        #print(f'ans-i:{show_num}')

        ans =str(otoku)

        if otoku_len == 2:
            ans =str(otoku)
            if int(ans[-2]) <= 5:
                show_num[-2]=1
        if otoku_len == 3:
            if int(ans[-3]) <= 3:
                show_num[-3]=1
            elif int(ans[-3])<=6:
                show_num[-3]=2
        if otoku_len == 4:
            pu = int(int(ans[-4])/2 + 1)
            show_num[-4]=pu
        if otoku_len == 5:
            pu =int(ans[-5])
            show_num[-5]=pu
        if otoku_len >= 6:
            pu =int(ans[-6])
            show_num[-6]=pu
        #print(f'40:{show_num}')

    return show_num, plamai

#----yasai------------------------------------------------------------------------------------------------------------------------------------
#otoku_show_numから出たリストを受け取る
def show_hana(num_list):
    posi = []
    width = 1000
    height = 1000
    num = 0
    for i in num_list:
        num += i
    #print(num)
    #print(num_list)
    if num < 5:
        width =550
        height =341
    elif num<10:
        width=600
        height=500
    elif num<20:
        width = 800
        height=600
    elif num<31:
        width=1000
        height=800

    check = []
    images1 = []
    images2 = []
    images3 = []
    flag1 = 0
    flag = 0
    for i in num_list:
        #print(i)
        flag +=1
        for j in range(i):
            if flag == 1:
                rand_num=str(np.random.randint(1,5))
                #img_name='hana2/'+str(flag)+'_'+rand_num+'.png'
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                #img_name='hana2/'+str(flag)+'_'+rand_num+'.png'
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                #img_name='hana2/'+str(flag)+'_'+rand_num+'.png'
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像
                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1=1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 2:
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)
                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 3:
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)
                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 4:
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)
                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 5:
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#小さい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#小さい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/hana/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#小さい画像
                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])


    #print(len(coordinates))
    #print(posi)
    #print(check)
    #print(width)
    #print(height)
    pictures = []
    # 画像を合成する
    canvas1 = Image.new("RGB", (width, height), (244, 177, 131))
    for i in range(len(images1)):
        canvas1.paste(images1[i], posi[i],images1[i])
    # 画像を保存する
    #canvas1.save('static/hanabatake1.jpg')
    pictures.append(canvas1)
    # 画像を合成する
    canvas2 = Image.new("RGB", (width, height), (244, 177, 131))
    for i in range(len(images2)):
        canvas2.paste(images2[i], posi[i],images2[i])
    # 画像を保存する
    #canvas2.save('static/hanabatake2.jpg')
    pictures.append(canvas2)
    # 画像を合成する
    canvas3 = Image.new("RGB", (width, height), (244, 177, 131))
    for i in range(len(images3)):
        canvas3.paste(images3[i], posi[i],images3[i])
    # 画像を保存する
    #canvas3.save('static/hanabatake3.jpg')
    pictures.append(canvas3)

    #gifを保存する
    #print(pictures)
    pictures[0].save('static/hanabatake.gif',save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)
    #pictures[0].save('hanabatake.gif',save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0,disposal=2)

    return num



#------kakou--------------------------------------------------------------------------------------------------------------
#otoku_show_numから出たリストを受け取る
def show_stone(num_list):
    posi = []
    width = 1000
    height = 1000
    num = 0
    for i in num_list:
        num += i
    #print(num)
    #print(num_list)
    if num < 5:
        width =550
        height =341
    elif num<10:
        width=600
        height=500
    elif num<20:
        width = 800
        height=600
    elif num<31:
        width=1000
        height=800

    check = []
    images1 = []
    images2 = []
    images3 = []
    flag1 = 0
    flag = 0
    for i in num_list:
        #print(i)
        flag +=1
        for j in range(i):
            if flag == 1:
                rand_num=str(np.random.randint(1,2))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(3,4))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(5,6))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1=1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 2:
                rand_num=str(np.random.randint(1,2))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(3,4))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(5,6))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 3:
                rand_num=str(np.random.randint(1,2))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(3,4))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(5,6))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 4:
                rand_num=str(np.random.randint(1,2))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(3,4))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(5,6))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 5:
                rand_num=str(np.random.randint(1,2))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(3,4))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(5,6))
                img_name='images/stone/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])


    #print(len(coordinates))
    #print(posi)
    #print(check)
    #print(width)
    #print(height)

    pictures = []
    # 画像を合成する
    canvas1 = Image.new("RGB", (width, height), (150, 190, 157))
    for i in range(len(images1)):
        canvas1.paste(images1[i], posi[i],images1[i])
    # 画像を保存する
    #canvas1.save('static/kakoujou1.jpg')
    pictures.append(canvas1)
    # 画像を合成する
    canvas2 = Image.new("RGB", (width, height), (150, 190, 157))
    for i in range(len(images2)):
        canvas2.paste(images2[i], posi[i],images2[i])
    # 画像を保存する
    #canvas2.save('static/kakoujou2.jpg')
    pictures.append(canvas2)
    # 画像を合成する
    canvas3 = Image.new("RGB", (width, height), (150, 190, 157))
    for i in range(len(images3)):
        canvas3.paste(images3[i], posi[i],images3[i])
    # 画像を保存する
    #canvas3.save('static/kakoujou3.jpg')
    pictures.append(canvas3)

    #gifを保存する
    pictures[0].save('static/kakoujou.gif',save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)

    return num


#------fish--------------------------------------------------------------------------------------------------------------
#otoku_show_numから出たリストを受け取る
def show_fish(num_list):
    posi = []
    width = 1000
    height = 1000
    num = 0
    for i in num_list:
        num += i
    #print(num)
    #print(num_list)
    if num < 5:
        width =550
        height =341
    elif num<10:
        width=600
        height=500
    elif num<20:
        width = 800
        height=600
    elif num<31:
        width=1000
        height=800

    check = []
    images1 = []
    images2 = []
    images3 = []
    flag1 = 0
    flag = 0
    for i in num_list:
        #print(i)
        flag +=1
        for j in range(i):
            if flag == 1:
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1=1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 2:
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 3:
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 4:
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 5:
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/fish/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])


    #print(len(coordinates))
    #print(posi)
    #print(check)
    #print(width)
    #print(height)
    # 画像を合成する

    pictures = []
    # 画像を合成する
    canvas1 = Image.new("RGB", (width, height), (50, 60, 157))
    for i in range(len(images1)):
        canvas1.paste(images1[i], posi[i],images1[i])
    # 画像を保存する
    #canvas1.save('static/suizokukan1.jpg')
    pictures.append(canvas1)
    # 画像を合成する
    canvas2 = Image.new("RGB", (width, height), (50, 60, 157))
    for i in range(len(images2)):
        canvas2.paste(images2[i], posi[i],images2[i])
    # 画像を保存する
    #canvas2.save('static/suizokukan2.jpg')
    pictures.append(canvas2)
    # 画像を合成する
    canvas3 = Image.new("RGB", (width, height), (50, 60, 157))
    for i in range(len(images3)):
        canvas3.paste(images3[i], posi[i],images3[i])
    # 画像を保存する
    #canvas3.save('static/suizokukan3.jpg')
    pictures.append(canvas3)

    #gifを保存する
    pictures[0].save('static/suizokukan.gif',save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)

    return num


#------animal--------------------------------------------------------------------------------------------------------------
#otoku_show_numから出たリストを受け取る
def show_animal(num_list):
    posi = []
    width = 1000
    height = 1000
    num = 0
    for i in num_list:
        num += i
    #print(num)
    #print(num_list)
    if num < 5:
        width =550
        height =341
    elif num<10:
        width=600
        height=500
    elif num<20:
        width = 800
        height=600
    elif num<=31:
        width=1000
        height=800

    check = []
    images1 = []
    images2 = []
    images3 = []
    flag1 = 0
    flag = 0
    for i in num_list:
        flag +=1
        for j in range(i):
            if flag == 1:
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1=1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 2:
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 3:
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 4:
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])

            elif flag == 5:
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images1.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images2.append(img)#大きい画像
                rand_num=str(np.random.randint(1,5))
                img_name='images/animal/'+str(flag)+'_'+rand_num+'.png'
                img = Image.open(img_name)
                images3.append(img)#大きい画像

                x_size=img.size[0]
                y_size=img.size[1]
                flag1=0

                while flag1 == 0:
                    x_posi = np.random.randint(0,width - x_size)
                    y_posi = np.random.randint(0,height - y_size)
                    flag1 = 1
                    for i in check:
                        if x_posi>=i[0] and y_posi>=i[1]:
                            if x_posi-i[0]<=i[2] and y_posi-i[1]<=i[3]:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<i[0] and y_posi<i[1]:
                            if i[0]-x_posi<x_size and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi>=i[0] and y_posi<=i[1]:
                            if x_posi-i[0]<i[2] and i[1]-y_posi<y_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1
                        elif x_posi<=i[0] and y_posi>=i[1]:
                            if y_posi-i[1]<i[3] and i[0]-x_posi<x_size:
                                flag1=0
                                width+=10
                                height+=10
                                break
                            else:
                                flag1=1

                    if flag1==1:
                        posi.append([x_posi,y_posi])
                        check.append([x_posi,y_posi,x_size,y_size])


    #print(len(coordinates))
    #print(posi)
    #print(check)
    #print(width)
    #print(height)
    # 画像を合成する

    pictures = []
    # 画像を合成する
    canvas1 = Image.new("RGB", (width, height), (50, 190, 57))
    for i in range(len(images1)):
        canvas1.paste(images1[i], posi[i],images1[i])
    # 画像を保存する
    #canvas1.save('static/zoo1.jpg')
    pictures.append(canvas1)
    # 画像を合成する
    #print(len(posi))
    #print(len(images2))
    canvas2 = Image.new("RGB", (width, height), (50, 190, 57))
    for i in range(len(images2)):
        canvas2.paste(images2[i], posi[i],images2[i])
    # 画像を保存する
    #canvas2.save('static/zoo2.jpg')
    pictures.append(canvas2)
    # 画像を合成する
    canvas3 = Image.new("RGB", (width, height), (50, 190, 57))
    for i in range(len(images3)):
        canvas3.paste(images3[i], posi[i],images3[i])
    # 画像を保存する
    #canvas3.save('static/zoo3.jpg')
    pictures.append(canvas3)

    #gifを保存する
    pictures[0].save('static/zoo.gif',save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)

    return num



num,judge = otoku_show_num(9999334)
print(num)
print(judge)
#img_show_posi(num)
level = show_hana(num)
level = show_stone(num)
level = show_fish(num)
level = show_animal(num)
#print(level)
