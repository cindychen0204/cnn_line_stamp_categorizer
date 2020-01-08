import cnn_model
import keras
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

im_rows = 32
im_cols = 32
im_color = 3
in_shape = (im_rows,im_cols,im_color)
nb_classes = 7

# Read picture data
photos = np.load("../line_stamps/photos_stamps_add.npz")
x = photos["x"]
y = photos["y"]

# read data and convert in 3D
x = x.reshape(-1,im_rows,im_cols,im_color)
x = x.astype("float32")/255
# reverse label data into one-hot vector
y = keras.utils.np_utils.to_categorical(y.astype("int32"),nb_classes)
# categorize data into "training" and "testing" data
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
# obtain cnn model
model = cnn_model.get_model(in_shape, nb_classes)

# start training
hist = model.fit(x_train, y_train,
              batch_size=32,
              epochs=20,
              verbose=1,
              validation_data=(x_test, y_test))

# Assess model
score = model.evaluate(x_test, y_test, verbose=1)
print("accuracy rate=", score[1], "loss=", score[0])

# draw process
# plot accuracy rate
plt.plot(hist.history["acc"])
plt.plot(hist.history["val_acc"])
plt.title("Accuracy")
plt.legend(["train", "test"], loc="upper left")
plt.show()

# plot lost
plt.plot(hist.history["loss"])
plt.plot(hist.history["val_loss"])
plt.title("Loss")
plt.legend(["train", "test"], loc="upper left")
plt.show()

model.save_weights("../line_stamps/stamp-model-light_add.hdf5")
print("save weight")
