#$python3 create_gif.py フォルダ名(語尾に'/'は付けない)

#ライブラリのインポート
from PIL import Image
import os
import sys
from natsort import natsorted

path = sys.argv[1]
print(path)

files = natsorted(os.listdir(path))
#print(files)

#画像を入れる箱を準備
pictures=[]

#画像を箱に入れていく
for filename in files:
    filename = path + '/' + filename
    #print(filename)
    img = Image.open(filename)
    pictures.append(img)
#gifアニメを出力する
out_name1 = 'gif_list/' + sys.argv[1] + '.gif'
print(out_name1)
pictures[0].save(out_name1,save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)
out_name2 = '../static/' + sys.argv[1] + '.gif'
print(out_name2)
pictures[0].save(out_name2,save_all=True, append_images=pictures[1:],optimize=True, duration=500, loop=0)