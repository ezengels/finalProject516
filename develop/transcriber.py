import os

path = os.getcwd()
dir_list = os.listdir(path)
paths = [path + '/' + sub + '/' for sub in dir_list]
datafolder = paths[1]
datafolders = os.listdir(datafolder)

print(datafolders)