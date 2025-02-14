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

Included in this code is also an implementation which will calculate the average
energy of the final and initial state by giving it the summary files of final and 
initial states.
"""

import numpy as np


def data_extractor_intermediate(directory, E_gs):
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
            #print("element: ", element)
            matrix.append(element) # each data row is put into a 2D matrix.
    #print(matrix, len(matrix))
    #print()
    #print("matrix[34]: ", matrix[34])
    #print()
    #print("matrix[34][6]: ", matrix[34][6])
    
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
    #print(Ex_column_data)
    #print()
    
    # Part III: We now adjust for the excited states by correcting for the ground state energy.
    
    #E_gs = -62.16550720
    new_excited_state = []
    for index in range(len(Ex_column_data)):
        new_excited_state.append(E_gs + Ex_column_data[index])
        
    new_excited_state.insert(0, E_gs) # Here I'm just putting the ground state with his buddies.
    #print(new_excited_state)
        

    return new_excited_state


def data_average_energy(initial, final):
    """
    We calculate the average energy between final and initial states.
    
    intial = initial state summary file.
    final = final state summary file.
    """
    # Part I: Extract data and put into a matrix.
    initial_array = [] # empty array to be filled with data.
    with open(initial, "r") as doc:
        for line in doc:
            #print(line)
            element = line.split() # this will put each row into a list.
            #print("element: ", element)
            initial_array.append(element) # each data row is put into a 2D matrix.

    # Part I: Extract data and put into a matrix.
    final_array = [] # empty array to be filled with data.
    with open(final, "r") as doc:
        for line in doc:
            #print(line)
            element = line.split() # this will put each row into a list.
            #print("element: ", element)
            final_array.append(element) # each data row is put into a 2D matrix.
    

    average_energy = 0.5 * (float(initial_array[5][5]) + float(final_array[5][5]))

    #print()
    #print("AVERAGE ENERGY: ", average_energy)
    #print()
    
    return average_energy



"""
Calculating new ex_energies.

ex_energy = E_k - <E_avg>
"""

def ex_energy(intermediate, E_gs, initial, final):
    ex_energy = []
    
    for i in range(0, 30):
        ex_energy.append(data_extractor_intermediate(intermediate, E_gs)[i] - data_average_energy(initial, final))
    
    return ex_energy
    

initial = r"C:\Users\dsedgh\Downloads\summary_O22_sd-shell_EM1.8_2.0_om1.0_magnus_O22_e4_E16_s500_hw15_A22.txt"
final = r"C:\Users\dsedgh\Downloads\summary_Ne22_sd-shell_EM1.8_2.0_om1.0_magnus_O22_e4_E16_s500_hw15_A22.txt"
path = r"C:\Users\dsedgh\Downloads\14th of february work\summary_F22_sd-shell_EM1.8_2.0_om1.0_magnus_O22_e4_E16_s500_hw15_A22.txt"


data_extractor_intermediate(path, -62.16550720)
data_average_energy(initial, final)

print("FINAL RESULT: ", ex_energy(path, -62.16550720, initial, final))

# I've tested with just the ground state energy given by kshell to compare my result
# with kshell and it works perfectly well.