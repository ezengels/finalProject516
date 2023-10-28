import cv2
import re
import pytesseract
from pytesseract import Output

img = cvs.imread('00001.jpg')

#image preprocessing

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.bilateralFilter(img, 3, 10, 10)

def threshold(img):
    img = cv2.threshold(img, 0, 230, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

# boxing characters

h, w, c = img.shape

boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()