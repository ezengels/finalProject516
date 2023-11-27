import os
import re

imagepaths = []
pathsshort = []
pdfnames = []
inputfolder = ''
pdffolder = ''

path = os.getcwd()
dir_list = os.listdir(path)
paths = [sub + '/' for sub in dir_list]
for path in paths:
	if re.search("input", path):
		inputfolder = inputfolder + path
	elif re.search("transcribed", path):
		pdffolder = pdffolder + path

for root, dirs, files in os.walk(inputfolder, topdown = True, onerror = None):
	for name in files:
		imagepaths.append(os.path.join(root, name))

pattern = re.compile('(?P<local>\w*\/\d*\.jpg)')
for i in imagepaths:
	h = pattern.search(i)
	if h:
		pathsshort.append('%s' % (h.group('local')))

for path in pathsshort:
	path = path.replace('.jpg', '')
	path = path.replace('/', '')
	pdfnames.append(path)

print(imagepaths)