"""
The purpose of this code is to extract data given a certain file
whereby the data is put into an array for use in plotting and 
other manipulations.

Version 1.0.0 
Date: 10th of February 2025
"""
import numpy as np

"""
The extractor function will take an in as input a directory
path and a column index. It will go through that file and 
extract all the data under the column indicated.
"""

def data_extractor(directory, column):
    """
    directory = path to file
    column = integer number of column index
    """
    
    # Part I: Extract data and put into a matrix.
    matrix = [] # empty array to be filled with data.
    with open(directory, "r") as doc:
        for line in doc:
            #print(line)
            element = line.split() # this will put each row into a list.
            print("element: ", element)
            matrix.append(element) # each data row is put into a 2D matrix.
        #print("This is 2D matrix: ", matrix, "\n and this is a list inside of matrix: ", matrix[0], matrix[1], 
        #"\n and this is an element of a list: ", matrix[0][2], matrix[1][3])
    

    # Part II: Extract specific column of the data.
    column_data = [] # an empty array for the column data.
    print(f"Column {column}: ")

    # This will go through matrix and pick data from desired column.
    for index in range(1, len(matrix)):
        column_data.append(float(matrix[index][column - 1]))
    #print(column_data)
    for j in range(len(column_data)):
        print(column_data[j])
    #return print(f"Data extracted successfully for column {column}.")
    return column_data 

#path = r"C:\Users\dsedgh\Downloads\summary_F22_sd-shell_EM1.8_2.0_om1.0_magnus_O22_e4_E16_s500_hw15_A22.txt"
path = r"C:\Users\dsedgh\Downloads\O22_emax4_data_from_eval.txt"
data_extractor(path, 4)