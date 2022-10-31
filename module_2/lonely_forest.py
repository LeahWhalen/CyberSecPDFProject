import os
import numpy as np
import pandas as pd

# change directory
current_directory = os.getcwd().replace("module_2", "")
os.chdir(current_directory)

# class that defines pdfs and operates on them
class PDFInformation:
    #attributes:
    # pdf - raw text of the pdf
    # pdf_as_str = divide pdf raw text into lines
    # pdf_objects = divide pdf into objects

    def __init__(self, pdf_dir):
        self.pdf = self.convert(pdf_dir)

    # converts pdf to plain text?
    def convert(self, pdf_dir):
        f = open(pdf_dir, "r")

        self.pdf_as_str = f.read()

        self.pdf_strings = self.pdf_as_str.split("\n")
        print(self.pdf_strings[1] + "\n\n")

        obj_indices = []
        temp_object = []
        pdf_objects = []
        in_object = 0

        count = 0
        for strings in self.pdf_strings:
            # print(strings)
            if (strings.find("obj") != -1) or (in_object == 1):
                in_object = 1
                print("inside an object")
                obj_indices.append(strings)
                temp_object.append(strings)
                # print(strings)
                if(strings.find("endobj") != -1):
                    count = count + 1
                    print(count)
                    in_object = 0
                    temp = temp_object.copy()
                    pdf_objects.append(temp)
                    temp_object = []


        self.object_count = count
        self.pdf_objects = pdf_objects
        print(pdf_objects)


def main():
    PDF = PDFInformation((current_directory+"Malicious_PFD_1/test1.pdf"))


if __name__ == "__main__":
    main()
