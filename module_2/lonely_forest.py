import os
import numpy as np
import panda as pd

# change directory


# class that defines pdfs and operates on them
class pdf_information:
    def __init__(self, pdf_text, pdf_strings):
        self.pdf = pdf.convert()
        self.pdf_strings = []

    def convert(self, pdf):
        f = open(self.pdf, "r")
        pdf_as_str = f.read()
        self.pdf_strings = pdf_as_str.split(" ")
        print(pdf_strings)

    def generate_lonely_forest(self):
        