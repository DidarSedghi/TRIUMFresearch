"""
This code is attempting to address an indexing issue encountered
with previous code v.1.0.0 whereby the intermediate data file had 
problems indexing properly when in the loop. This was hard coded
since it was easier.

Version 1.0.1 
Date: 14th of February 2025
"""

"""
The purpose of this code is similar to the first version, but specifically
adapted for the intermediate excited state energy data. We extract the Ex(MeV)
and store in an array. Then, we correct for the ground state energy of intermediate
state by using the experimental value.
Next, we reconstruct the excited energy levels by adding E_gs to the Ex(MeV) we 
had extracted previously.
"""

import numpy as np


def data_extractor_intermediate(directory):
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
    print(matrix, len(matrix))
    print()
    print("matrix[34]: ", matrix[34])
    print()
    print("matrix[34][6]: ", matrix[34][6])
    
    """
    In the matrix data array, our desired data array starts in element 5
    of the matrix. Within each data array, the desired Ex(MeV) energy is in
    element 6.
    """
    
    # Part II: Putting extracted data elements into a vector array.
    Ex_column_data = []
    
    for index in range(6, 35):
        Ex_column_data.append(float(matrix[index][6]))
        print(matrix[index][6])
    print(Ex_column_data)
    print()
    # Part III: We now adjust for the excited states by putting in our own value for ground state energy.
    
    E_gs = -62.16550720
    new_excited_state = []
    for index in range(len(Ex_column_data)):
        new_excited_state.append(E_gs + Ex_column_data[index])
    print(new_excited_state)
        
        


    return 0

path = r"C:\Users\dsedgh\Downloads\summary_F22_sd-shell_EM1.8_2.0_om1.0_magnus_O22_e4_E16_s500_hw15_A22.txt"
data_extractor_intermediate(path)