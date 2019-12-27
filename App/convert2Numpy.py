import os,glob,random
import cv2
import numpy as np

outfile = "../line_stamps/photos_stamps_add.npz"#保存ファイル名
photo_size = 32
x=[]#画像データ
y=[]#ラベルデータ

line_stamps_path = "../line_stamps/"
categories = os.listdir(line_stamps_path)
#print(len(categories))

for category in categories:
    files = glob.glob(line_stamps_path + category + "/*.png")
    for i, filename in enumerate(files):
        #画像ファイルを読む
        img= cv2.imread(filename)
        #print(img.shape)
        img = cv2.resize(img, (photo_size, photo_size))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.asarray(img)
        x.append(img)
        y.append(categories.index(category))
        print(categories.index(category))
        #ファイルへ保存

np.savez(outfile, x = x, y = y)#xとyがnumpyのリストとして与えられる
print("保存しました：" + outfile, len(x))
