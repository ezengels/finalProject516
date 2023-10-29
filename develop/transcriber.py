import os
import cv2
import pytesseract

images = []

path = os.getcwd()
dir_list = os.listdir(path)
paths = [path + '/' + sub + '/' for sub in dir_list]
datafolder = paths[1]
for root, dirs, files in os.walk(datafolder, topdown = True, onerror = None):
	for name in files:
		images.append(os.path.join(root, name))
		
for image in images:
	image = cv2.imread(image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bilateralFilter(image, 3, 10, 10)
	# image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    
	pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
	with open('test.pdf', 'w+b') as f:
		f.write(pdf)

