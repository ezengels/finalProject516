import cv2
import pytesseract

for image in imagepaths:
	l = imagepaths.index(image)
	image = cv2.imread(image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bilateralFilter(image, 3, 10, 10)
	# image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
	pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
	with open(pdffolder + pdfnames[l] + '.pdf', 'w+b') as f:
		f.write(pdf)