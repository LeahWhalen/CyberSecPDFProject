import os
import numpy as np
import pandas as pd
import csv
from pycaret.anomaly import *
from pycaret.datasets import get_data

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

        # creates the pdf_as_str attribute
        self.pdf_as_str = f.read()

        self.pdf_strings = self.pdf_as_str.split("\n")
        print(self.pdf_strings[1] + "\n\n")
        print(self.pdf_as_str)

        obj_indices = []
        temp_object = []
        pdf_objects = []
        in_object = 0

        # create the pdf as object attribute
        # TODO: finish this
        # count = 0
        # for strings in self.pdf_strings:
        #     # print(strings)
        #     if (strings.find("obj") != -1) or (in_object == 1):
        #         in_object = 1
        #         print("inside an object")
        #         obj_indices.append(strings)
        #         temp_object.append(strings)
        #         # print(strings)
        #         if(strings.find("endobj") != -1):
        #             count = count + 1
        #             print(count)
        #             in_object = 0
        #             temp = temp_object.copy()
        #             pdf_objects.append(temp)
        #             temp_object = []

        # self.object_count = count
        # self.pdf_objects = pdf_objects
        # print(pdf_objects)

        # TODO: parse out body
        # TODO: move this class to a pdf parser file




def main():
    PDF = PDFInformation((current_directory+"Malicious_PFD_1/test2.pdf"))

    # create the csv from the data
    with open("pdf_csv.csv", "w") as csv_f:
        writer = csv.writer(csv_f)

        # add all the pdfs to arrays and convert them
        pdf_array = []
        headers = []
        for i in range(1, 11):
            # gets name of file and reads it in
            pdf_file_name = current_directory+"Malicious_PFD_1/test"+str(i)+".pdf"
            pdf_name_short = "test"+str(i)+".pdf"
            print(pdf_file_name)

            # cut line by line
            f = open(pdf_file_name, "r")
            pdf_as_str = f.read()

            # encodes data into characters
            pdf_strings = pdf_as_str.split('/n')
            pdf_chars = list(pdf_as_str)
            pdf_numbers = []
            for character in pdf_chars:
                pdf_numbers.append(ord(character))
            # print(pdf_numbers)

            # add headers to a list
            headers.append(pdf_name_short)

            # append for dataframe
            pdf_array.append(pdf_numbers)

            f.close()

        df = pd.DataFrame(pdf_array)
        df = df.transpose()
        dataset = df.set_axis(headers, axis='columns')
        print(df)
        # writer.writerows(pdf_array)
        csv_f.close()

    print(dataset)

    # data parsing
    data = dataset.sample(frac=0.95, random_state=786)
    data_unseen = dataset.drop(data.index)
    
    data.reset_index(drop=True, inplace=True)
    data_unseen.reset_index(drop=True, inplace=True)
    
    exp_ano101 = setup(data, normalize = True)
    
    # iforest model
    iforest = create_model('iforest')
    iforest_predictions = predict_model(model = iforest, data = data_unseen)
    iforest_predictions.head()
    print(iforest)
    print(iforest_predictions)
    # iforest_chars = iforest_predictions.apply(chr)
    print(iforest_chars)
    
    iforest_results = assign_model(iforest)
    iforest_results.head()
    
    # plot_model(iforest, plot = 'tsne')
    plot_model(iforest, plot = 'umap')

    # svm model
    svm = create_model('svm')
    svm_predictions = predict_model(model = svm, data = data_unseen)
    svm_predictions.head()
    print(svm)
    print(svm_predictions)
    
    svm_results = assign_model(svm)
    svm_results.head()
    
    # plot_model(iforest, plot = 'tsne')
    plot_model(svm, plot = 'umap')



if __name__ == "__main__":
    main()


