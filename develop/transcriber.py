import os
import re
import cv2
import pytesseract

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

# Reduce1 Script

for image in imagepaths:
	l = imagepaths.index(image)
	image = cv2.imread(image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bilateralFilter(image, 3, 10, 10)
	# image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
	pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
	with open(pdffolder + pdfnames[l] + '.pdf', 'w+b') as f:
		f.write(pdf)