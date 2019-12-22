import os,glob,random
import cv2
import numpy as np

outfile="image/photos_ramen_add.npz"#保存ファイル名
max_photo=120
photo_size=32
x=[]#画像データ
y=[]#ラベルデータ

def main():
    #各画像のフォルダーを読む
    glob_files("./image/tantan",0)
    glob_files("./image/iekei",1)
    glob_files("./image/jirou",2)
    glob_files("./image/shoyu",3)
    glob_files("./image/sio",4)
    glob_files("./image/udon",5)

    #ファイルへ保存
    np.savez(outfile,x=x,y=y)#xとyがnumpyのリストとして与えられる
    print("保存しました："+outfile,len(x))

#path以下の画像を読み込む
def glob_files(path,label):
    files=glob.glob(path+"/*.jpg")
    random.shuffle(files)
    #各ファイルを処理
    num=0
    #print(files)
    for f in files:
        if num >=max_photo:break
        num+=1
        #画像ファイルを読む
        img=cv2.imread(f)
        img=cv2.resize(img, (photo_size,photo_size ))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=np.asarray(img)
        x.append(img)
        y.append(label)

    print(num)

if __name__=="__main__":
    main()
