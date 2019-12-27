import cnn_model
import keras
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

#入力と出力を指定
im_rows=32
im_cols=32
im_color=3
in_shape=(im_rows,im_cols,im_color)
nb_classes=7

#写真データを読み込み
photos=np.load("../line_stamps/photos_stamps_add.npz")
x=photos["x"]
y=photos["y"]

#読み込んだデータを三次元配列に変換
x=x.reshape(-1,im_rows,im_cols,im_color)
x=x.astype("float32")/255
#ラベルデータをone-hotベクトルに直す
y=keras.utils.np_utils.to_categorical(y.astype("int32"),nb_classes)
#学習用とテスト用に分ける
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8)
#cnnモデルを取得
model=cnn_model.get_model(in_shape,nb_classes)

#学習を実行
hist=model.fit(x_train,y_train,
              batch_size=32,
              epochs=20,
              verbose=1,
              validation_data=(x_test,y_test))

#モデルを評価
score=model.evaluate(x_test,y_test,verbose=1)
print("正解率=",score[1],"loss=",score[0])

#学習の様子をグラフへ描写
#正解率の推移をプロット
plt.plot(hist.history["acc"])
plt.plot(hist.history["val_acc"])
plt.title("Accuracy")
plt.legend(["train","test"],loc="upper left")
plt.show()

#ロスの推移をプロット
plt.plot(hist.history["loss"])
plt.plot(hist.history["val_loss"])
plt.title("Loss")
plt.legend(["train","test"],loc="upper left")
plt.show()

model.save_weights("../line_stamps/stamp-model-light_add.hdf5")
print("ウェイトを保存しました")
