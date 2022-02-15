import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
#from matplotlib import rc
from scipy.optimize import curve_fit
#rc('text', usetex=True)
plt.rcParams["font.family"] = "serif"
plt.style.use('classic')




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
    plt.suptitle(" Scattering ")
    plt.xlabel("Voltage (Volts)")
    plt.ylabel("B^2r^2[]")
    plt.show()

def curve_fit_linear(imported_data):
    plt.figure(figsize=(10,8))
    #Change ERRORBARS here
    plt.errorbar(imported_data[0], imported_data[1], yerr=0.0, fmt ='.k', capsize=3, capthick= 1)
    #What your guesses are for the function parameters
    #InitialGuess = [0.3,(2*np.pi)/200]



    #This is where actual fitting takes place i.e the finding of optimal parameters
    popt, pcov = curve_fit(linear, imported_data[0], imported_data[1], maxfev=1000)


    #Change x- axis range here
    xfit = np.arange(0,len(imported_data[0]), 1)

    dx = 9.0
    par = tuple(popt) #This is standard deviation of the optimal parameters
    plt.plot(imported_data[0], imported_data[1], 'ko')
    plt.plot(xfit, linear(xfit, *popt), 'r--', label = r'eqn: y = {0:.12f} + {1}x'.format(par[0], par[1])) #Labe fit eqn with 3 decimal places
    
    print(f'The values of slope and y-intercept are {par[1]} and {par[0]}')

    '''Take sqrt of variance of parameters a (slope) and b (y-intercept) only & put in tuple
     so that it can be printed'''
    par_errors= tuple(np.sqrt(np.diag(pcov)))

    with open(errors_file_name_write, "w+") as file:
        file.write(f'The values of slope and y-intercept are {par[1]} and {par[0]}')
        file.write(f'The standard deviation of slope and y-intercept are {par_errors[1]:{1}.{3}} and {par_errors[0]:{1}.{3}}')
        file.close

    print(f'The standard deviation of slope and y-intercept are {par_errors[1]:{1}.{3}} and\
    {par_errors[0]:{1}.{3}}')
    print(f'The fit parameters and their errors have been written to {errors_file_name_write}')

    #plt.title(r"Large Cylinder Scattering ", fontdict={'fontsize' : 15})
    plt.suptitle(r"Radiation Background Count per 10s interval " ,fontdict={'fontsize' : 25})
    plt.xlabel(r'Number of time intervals',fontdict={'fontsize' : 20})
    plt.ylabel(r"Number of counts" ,fontdict={'fontsize' : 20})
    plt.legend(fontsize = 'large')
    
    #To label individual points
   # X= imported_data[0]
    #Y = imported_data[1]
    #annotations=["Blue","Aqua", "Red"]
    #for i, label in enumerate(annotations):
     #   plt.annotate(label, (X[i],Y[i]), fontsize= 15)

    # Tweak spacing to prevent clipping of y and xlabel
    #plt.subplots_adjust(left=0.15, bottom=0.2)

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

errors_file_name_write = 'decay error.txt'

imported_data = parse_file('calculated Decay-137-Ba.csv', header=False)
imported_data =sort_data(imported_data)
print(imported_data[0])
print(imported_data[1])


curve_fit_linear(imported_data)
#plotting(imported_data)