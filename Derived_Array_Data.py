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
            raw_data_1 = np.append(raw_data_1, float(split_line[0]))
            raw_data_2 = np.append(raw_data_2, float(split_line[1]))
    return [raw_data_1, raw_data_2]

def new_array_formula(raw_data_1):
    new_data = np.array([])
    new_data = raw_data_1*2
    return(new_data)


file_name = 'PHY251Lab2ElectronCharge.csv'
print(new_array_formula)