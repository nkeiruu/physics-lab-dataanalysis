import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
#from matplotlib import rc
from scipy.optimize import curve_fit
#rc('text', usetex=True)
plt.rcParams["font.family"] = "serif"
plt.style.use('fivethirtyeight')




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




def plotting(imported_data):
    plt.figure(figsize=(14,10))
    plt.plot(imported_data[0], imported_data[1], 'r')
    plt.errorbar(imported_data[0], imported_data[1], 'ko' ) 
    #plt.title("Lab 5", fontdict={'fontsize' : 30})
    plt.suptitle(" LAb 6 hydrogen")
    plt.xlabel("Voltage (Volts)")
    plt.ylabel("B^2r^2[]")
    plt.show()

def curve_fit_linear(imported_data):
    plt.figure(figsize=(10,8))
    #Change errorbars here
    plt.errorbar(imported_data[0], imported_data[1], yerr=0.0005, fmt ='.k', capsize=3, capthick= 1)
    #What your guesses are for the function parameters
    #InitialGuess = [0.3,(2*np.pi)/200]

    popt, pcov = curve_fit(linear, imported_data[0], imported_data[1], maxfev=1000)
    #Change x- axis range here
    xfit = np.arange(-0.5,0.5, 0.000001)

    dx = 9.0
    par = tuple(popt)
    plt.plot(imported_data[0], imported_data[1], 'ko')
    plt.plot(xfit, linear(xfit, *popt), 'r--', label = r'eqn: y = {0:.12f} + {1}x'.format(par[0], par[1])) #Labe fit eqn with 3 decimal places
    
    print(f'The values of slope and y-intercept are {par[0]} and {par[1]}')

    '''Take sqrt of variance of parameters a (slope) and b (y-intercept) only & put in tuple
     so that it can be printed'''
    par_errors= tuple(np.sqrt(np.diag(pcov)))
    print(f'The standard deviation of slope and y-intercept are {par_errors[0]:{1}.{3}} and\
    {par_errors[1]:{1}.{3}}')

    plt.title("Inverse of wavelength vs inverse of initial energy level", fontdict={'fontsize' : 15})
    plt.suptitle("Hydrogen Spectrum (Balmer Series)" ,fontdict={'fontsize' : 25})
    plt.xlabel(r'$\frac{1}{m^2}$',fontdict={'fontsize' : 20})
    plt.ylabel(r"$\frac{1}{\lambda}[\frac{1}{nm}]$" ,fontdict={'fontsize' : 20})
    plt.legend(fontsize = 'large')
    
    #To label individual points
    X= imported_data[0]
    Y = imported_data[1]
    annotations=["Blue","Aqua", "Red"]
    for i, label in enumerate(annotations):
        plt.annotate(label, (X[i],Y[i]), fontsize= 15)

    # Tweak spacing to prevent clipping of y and xlabel
    plt.subplots_adjust(left=0.15, bottom=0.2)

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
    return (b*x + a)

imported_data = parse_file('Order1.csv', header=False)
imported_data =sort_data(imported_data)
print(imported_data[0])
print(imported_data[1])

curve_fit_linear(imported_data)
#plotting(imported_data)