# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

for x in range(1,5,1):
# initializing variables with values
    fileName = 'ECE509sample%d.pdf' % (x)
    documentTitle = 'sample'
    title = 'ECE 509 CYBER SECURITY F2022'
    subTitle = 'The largest thing now!!'
    textLines = [
        'Houston we have lift off',
        'PDF#%d ECE509 TEST.' % (x),
    ]
    image = 'ECE509_image.jpg'
    
    # creating a pdf object
    pdf = canvas.Canvas(fileName)
      
    # setting the title of the document
    pdf.setTitle(documentTitle)
    
    # registering a external font in python
    pdfmetrics.registerFont(
        TTFont('TNR', 'times.ttf'))
      
    # creating the title by setting it's font 
    # and putting it on the canvas
    pdf.setFont('TNR', 36)
    pdf.drawCentredString(300, 770, title)
    
    # creating the subtitle by setting it's font, 
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)
    
    # drawing a line
    pdf.line(30, 710, 550, 710)
      
    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)
      
    for line in textLines:
        text.textLine(line)
          
    pdf.drawText(text)
    
    # drawing a image at the 
    # specified (x.y) position
    pdf.drawInlineImage(image, 5, -50)
      
    # saving the pdf
    pdf.save()








