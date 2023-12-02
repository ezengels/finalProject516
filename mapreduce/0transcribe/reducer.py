#!/bin/python3
import cv2
import pytesseract
import re
import sys

pattern = re.compile('(?P<book>\w*)\/(?P<page>\d*)\.jpg')

for line in sys.stdin:
	book = ''
	page =''
	imagepath = line
	h = pattern.search(imagepath)
	if h:
		book = h.group('book')
		page = h.group('page')

	image = cv2.imread(imagepath)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bilateralFilter(image, 3, 10, 10)
	# image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
	pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
	with open(book + page + '.pdf', 'wb') as f:
		f.write(pdf)