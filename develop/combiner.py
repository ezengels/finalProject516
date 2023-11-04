import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

pdfs = []

for root, dirs, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)
    