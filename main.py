#!/usr/bin/env python3
from PIL import Image
import sys

# images = [
    # Image.open("/Users/apple/Desktop/" + f)
    # for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
# ]
images = [Image.open(f'N{i}.jpg') for i in range(1, 10)]

pdf_path = "MyPdf.pdf"

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
sys.exit(0)



from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
imagelist = [f'P{i}.png' for i in range(1, 10)]
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")

