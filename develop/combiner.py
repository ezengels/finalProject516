import os
import re
pdffolder = ''
pdfs = []
titles = []

path = os.getcwd()
dir_list = os.listdir(path)
paths = [sub + '/' for sub in dir_list]

for path in paths:
    if re.search("transcribed", path):
        pdffolder = pdffolder + path
if pdffolder:
    for root, dirs, files in os.walk(pdffolder, topdown = True, onerror = None):
        for pdf in files:
            pdfs.append(os.path.join(root, pdf))

pattern = re.compile('\/(?P<title>\D*)')
for path in pdfs:
    t = pattern.search(path)
    if t:
        titles.append('%s' % (t.group('title')))
titles = list(set(titles))