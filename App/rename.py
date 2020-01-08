import glob
import os.path
from os import path

line_stamps_path = "../line_stamps/"
categories = os.listdir(line_stamps_path)
print(categories)

for category in categories:
    files = glob.glob(line_stamps_path + category + "/*.png")
    for i, old_fileName in enumerate(files):
        new_name = os.path.join(line_stamps_path + category, '{0:03d}'.format(i) + ".png")
        if (path.exists(new_name)):
            new_name = os.path.join(line_stamps_path + category, '{0:04d}'.format(i) + ".png")
        os.rename(old_fileName, new_name)
    print(category + " : " + str(len(files)))
