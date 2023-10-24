import cv2
import re
import pytesseract
from pytesseract import Output

img = cvs.imread('00001.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.bilateralFilter(img, 3, 10, 10)

def threshold(img):
