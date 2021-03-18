import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import rc
from scipy.optimize import curve_fit
#rc('text', usetex=True)
plt.rcParams["font.family"] = "serif"


def parse_file(file_name, header=True):
    x_axis_data = np.array([])
    y_axis_data = np.array([])
    with open(file_name) as file:
        for line in file:
            if(header == True):
                header = False
                continue
            split_line = line.split(',')
            x_axis_data = np.append(x_axis_data, float(split_line[0]))
            y_axis_data = np.append(y_axis_data, float(split_line[1]))
    return [x_axis_data, y_axis_data]

def plotting(imported_data):
    plt.figure(figsize=(14,10))
    plt.plot(imported_data[0], imported_data[1], 'r')
    plt.errorbar(imported_data[0], imported_data[1], 'ko' ) 
    #plt.title("Lab 5", fontdict={'fontsize' : 30})
    plt.suptitle("Lab 2: Determination of Electron Charge")
    plt.xlabel("Number of Electron Charge Units, e")
    plt.ylabel("Total Charge, Q [C]")
    plt.show()

def curve_fit_linear(imported_data):
    plt.figure(figsize=(10,8))
    #Change errorbars here
    plt.errorbar(imported_data[1], imported_data[0], yerr=0.005, fmt ='.k', capsize=3, capthick= 1)
    #What your guesses are for the function parameters
    #InitialGuess = [0.3,(2*np.pi)/200]

    popt, pcov = curve_fit(linear, imported_data[1], imported_data[0], maxfev=1000)
    #Change x- axis range here
    xfit = np.arange(0.0, 11.0, 1.5)

    dx = 9.0
    par = tuple(popt)
    plt.plot(xfit, linear(xfit, *popt), 'r--', label = r'eqn: y = {0:.5f}x + {1}'.format(par[0], par[1])) #Labe fit eqn with 3 decimal places
    
    print(f'The values of slope and y-intercept are {par[0]} and {par[1]}')

    '''Take sqrt of variance of parameters a (slope) and b (y-intercept) only & put in tuple
     so that it can be printed'''
    par_errors= tuple(np.sqrt(np.diag(pcov)))
    print(f'The standard deviation of slope and y-intercept are {par_errors[0]:{1}.{3}} and\
    {par_errors[1]:{1}.{3}}')

    plt.title("Number of electron charge unit, e, vs total charge", fontdict={'fontsize' : 15})
    #plt.suptitle("Number of electron charge unit, e, vs total charge")
    plt.xlabel("Number of Electron Charge Units, e")
    plt.ylabel(r'Total Charge, Q  $(x 10^{-17})  [C]$')
    plt.legend()
    plt.show()


def sort_data(imported_data):
    #implementation of insertion sort
    #check insertion sort in action here: https://visualgo.net/en/sorting
    i = 1
    while(i < len(imported_data[0])):
        j = i
        while(j > len(imported_data[0])):
            if(imported_data[0][j] < imported_data[0][j-1]):
                #sorting x-axis data
                temp = imported_data[0][j]
                imported_data[0][j] = imported_data[0][j-1]
                imported_data[0][j-1] = temp
                #sorting y-axis data
                temp = imported_data[1][j]
                imported_data[1][j] = imported_data[1][j-1]
                imported_data[1][j-1] = temp
            j -= 1
        i += 1
    return imported_data

def linear(x,a,b):
    return ((a*x)+ b)

imported_data = parse_file('PHY 251 Lab 2 Electron Charge.csv', header=False)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_linear(imported_data)
#plotting(imported_data)