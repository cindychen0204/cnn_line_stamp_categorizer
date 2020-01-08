import os, glob
import cv2
import numpy as np

outfile = "../line_stamps/photos_stamps_add.npz"
photo_size = 32
# image data
x = []
# label data
y = []

line_stamps_path = "../line_stamps/"
categories = os.listdir(line_stamps_path)

for category in categories:
    files = glob.glob(line_stamps_path + category + "/*.png")
    for i, filename in enumerate(files):
        img= cv2.imread(filename)
        img = cv2.resize(img, (photo_size, photo_size))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.asarray(img)
        x.append(img)
        y.append(categories.index(category))
        print(categories.index(category))

np.savez(outfile, x = x, y = y)
print("保存しました：" + outfile, len(x))
