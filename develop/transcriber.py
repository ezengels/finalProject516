import os
import cv2
import pytesseract

images = []

path = os.getcwd()
dir_list = os.listdir(path)
paths = [path + '/' + sub + '/' for sub in dir_list]
datafolder = paths[1]
datafolders = os.listdir(datafolder)
for folder in datafolders:
    datafiles = []
    datafiles.append(datafolder + folder + '/')
    for subfolder in datafiles:
        pathslist = []
        files = os.listdir(subfolder)
        for file in files:
            filepath = subfolder + '/' + file
            images.append(filepath)

for image in images:
	image = cv2.imread(image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bilateralFilter(image, 3, 10, 10)
    
	print(pytesseract.image_to_string(image))
