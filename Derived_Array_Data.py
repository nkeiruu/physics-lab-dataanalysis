import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import rc
from scipy.optimize import curve_fit
#rc('text', usetex=True)
plt.rcParams["font.family"] = "serif"


def parse_file(file_name, header=True):
    raw_data_1 = np.array([])
    raw_data_2 = np.array([])
    with open(file_name) as file:
        for line in file:
            if(header == True):
                header = False
                continue
            split_line = line.split(',')
            #print(split_line)
            raw_data_1 = np.append(raw_data_1, float(split_line[0]))
            raw_data_2 = np.append(raw_data_2, float(split_line[1]))
    return [raw_data_1, raw_data_2]#raw_data_2 can also be returned

#calculate the square of all array elements
def new_array_formula(raw_data):
    new_data = np.array([])
    data = np.array([])
    data = raw_data[0]
    new_data = np.log(raw_data[1])  #Input formula here
   
    return(data,new_data)

def write_to_file(new_data, file_name_write):
    output = "" #A place to put the data 
    print(new_data)
    with open(file_name_write, "w+") as file:
        #iterates through number of rows
        for i in range(0,len(new_data[0])):
            #iterates through number of members
            for j in range(0,len(new_data)):
                output += str(new_data[j][i])  #Convert data to string and put in holder
                if j != len(new_data)-1:
                    output+= ','
                else:
                    output+= '\n'
        file.write(output)
    file.close()
    print(f'The computed data has been written to {file_name_write}')

file_name = 'Decay-137-Ba.csv'
file_name_write = 'calculated Decay-137-Ba.csv'
#Calling parse file function to load the data and store in raw_data
raw_data = parse_file(file_name, header = False)

#Call new array formula
computed_data = new_array_formula(raw_data)

#print(computed_data)

write_to_file(computed_data, file_name_write)

