import re

for title in titles:
    group = []
    for path in pdfs:
        if re.search(title, path):
            group.append(path)
    merger = PdfMerger()
    for page in group:
        merger.append(page)
    merger.write("combined/" + title + ".pdf")
    merger.close()