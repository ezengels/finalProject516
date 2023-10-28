import os

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

print(images)
