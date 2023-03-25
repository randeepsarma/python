from PyPDF2 import PdfMerger

import os

merger = PdfMerger()

files = os.listdir()
# print(files)
for pdf in files:
    if pdf == "main.py":
        continue
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
