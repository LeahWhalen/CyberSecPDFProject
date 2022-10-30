import os
import numpy as np
import panda as pd

# change directory


# class that defines pdfs and operates on them
class pdf_information:
    def __init__(self, pdf_text, pdf_strings):
        self.pdf = pdf.convert()
        self.pdf_strings = []
        self.pdf_objects = []

    # converts pdf to plain text?
    def convert(self, pdf):
        f = open(self.pdf, "r")
        pdf_as_str = f.read()
        self.pdf_strings = pdf_as_str.split(" ")
        print(pdf_strings)

    # sort by objects
    def convert_to_objects(self):

    def generate_lonely_forest(self):
        print(os.listdir("../input"))df=pd.read_csv("../input/metric_data.csv")
        df.head()