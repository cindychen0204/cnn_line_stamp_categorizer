import cnn_model
import keras
import matplotlib.pyplot as plt
import numpy as np
import cv2

photo = "../line_stamps/testimages/sad-5.png"
labels = ['angry', 'excited', 'fear', 'Happy', 'sad', 'shock']

model=cnn_model.get_model((32,32,3),7)#画像のshape、ラベルデータの数
model.load_weights("../line_stamps/stamp-model-light_add.hdf5")

img=cv2.imread(photo)
img=cv2.resize(img, (32,32))#画像のshape
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img)
#plt.show()

#array
x=np.asarray(img)
x=x.reshape(-1,32,32,3)#画像のshape
x=x/255

#予測する
pre=model.predict([x])[0]
idx=pre.argmax()
per=int(pre[idx]*100)

print(per, " with ",  labels[idx])

if per >= 60:
    print("これは"+str(per)+"%の確率で"+labels[idx]+"です。")
else:
    print("よくわかりません。")
