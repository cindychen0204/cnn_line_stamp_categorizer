import cnn_model
import keras
import matplotlib.pyplot as plt
import numpy as np
import cv2

# DECIDE TEST DATA
PHOTO = "../line_stamps/testimages/sad-5.png"

labels = ['angry', 'excited', 'fear', 'happy', 'sad', 'shock']
model=cnn_model.get_model((32, 32, 3), 7)  # shape of stamps, and labels number
model.load_weights("../line_stamps/stamp-model-light_add.hdf5")

img = cv2.imread(PHOTO)
img = cv2.resize(img, (32,32))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

# array
x = np.asarray(img)
x = x.reshape(-1, 32, 32, 3)
x = x/255

# start predict
pre = model.predict([x])[0]
idx = pre.argmax()
per = int(pre[idx]*100)

print(per, " with ", labels[idx])

if per >= 60:
    print("This is " + labels[idx] + " with " + str(per) + "% accuracy.")
else:
    print("I do not know。")
