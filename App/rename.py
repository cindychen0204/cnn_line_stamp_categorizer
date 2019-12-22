import glob
import os


line_stamps_path = "../line_stamps/"

categories = os.listdir(line_stamps_path)
#print

files = []
for category in categories:
    files = glob.glob(line_stamps_path + category + "/*.png")
    for i, old_fileName in enumerate(files):
        print(old_fileName)
        new_name = os.path.join(line_stamps_path + category, '{0:03d}'.format(i) + ".png")
        os.rename(old_fileName, new_name)
        print("Change Name from " + old_fileName + " -> " + new_name)
