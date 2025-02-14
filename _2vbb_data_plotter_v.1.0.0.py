"""
The purpose of this code is after the retrieval of the data from 
the .txt file, we shall plot the Nuclear Matrix Element (labelled as sum)
in the kshell language. We plot the sum values as a function of the intermediate 
excited states.

Version 1.0.0 
Date: 14th of February 2025
"""

"""
Extractor code doing its magic to... extract data.
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


"""
Now we shall plot the figure.
"""
# Oxygen-22 isotope plot for emax=4.
import numpy as np
import matplotlib.pyplot as plt

data = r"C:\Users\dsedgh\Downloads\O22_emax4_data_from_eval.txt"
excited_states = np.arange(1, 31)

# Total sum of M_GT up till k-intermediate excited state.
plt.plot(excited_states, data_extractor(data, 5), color="red")
plt.scatter(excited_states, data_extractor(data, 5), color="red", marker='o', label="emax = 4")
plt.grid()
plt.legend()
plt.xlabel("Excited Intermediate States")
plt.ylabel("Total Sum of M_GT")
plt.title("M_GT sums as a function of K")
plt.show()

# Cntr of specific k-intermediate excited state.
plt.plot(excited_states, data_extractor(data, 4), color="red")
plt.scatter(excited_states, data_extractor(data, 4), color="red", marker='o', label="emax = 4")
plt.grid()
plt.legend()
plt.xlabel("Excited Intermediate States")
plt.ylabel("Cntr")
plt.title("Cntr as function of k")
plt.show()








