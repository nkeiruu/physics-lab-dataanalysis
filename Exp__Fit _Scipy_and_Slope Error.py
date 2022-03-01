import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#makes the plot look nicer in latex
mpl.use('pgf')
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})




from numpy.core.fromnumeric import sort
#from matplotlib import rc
from scipy.optimize import curve_fit
#rc('text', usetex=True)
plt.rcParams["font.family"] = "serif"
plt.style.use('seaborn-whitegrid')




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
    plt.xlabel("Time()")
    plt.ylabel("Voltage()")
    plt.show()

def curve_fit_linear(imported_data):

    #change this according to text width in latex if putting picture here
    plt.gcf().set_size_inches(w=7.058, h=5.4)

    #use this if not putting into latex
    #plt.figure(figsize=(10,8))
   
    #What your guesses are for the function parameters
    #InitialGuess = [0.3,(2*np.pi)/200]



    #This is where actual fitting takes place i.e the finding of optimal parameters
    popt, pcov = curve_fit(exp_Fit, imported_data[0], imported_data[1], maxfev=1000)


    #Change x- axis range here
    xfit = np.linspace(4.4,86,num=2000)

    dx = 9.0
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(imported_data[0], imported_data[1], 'ko')
    plt.plot(xfit, exp_Fit(xfit, *popt), 'r--', label = r'fit eqn: $V$ = {0:.3f}*$exp(-{1:.4f}t)$ '.format(par[0], par[1])) #Labe fit eqn with 3 decimal places
    
    
     #Change ERRORBARS here
    plt.errorbar(imported_data[0], imported_data[1], yerr=0.04, fmt ='.b')
    
    print(f'The values of amplitude and t2 are {par[0]} and {par[1]}')
    print(popt)

    '''Take sqrt of variance of parameters a (slope) and b (y-intercept) only & put in tuple
     so that it can be printed'''
    par_errors= tuple(np.sqrt(np.diag(pcov)))

    with open(errors_file_name_write, "w+") as file:
        file.write(f'The values of amp and t2 are {par[0]} and {par[1]}')
        file.write(f'The standard deviation of amp and t2 are {par_errors[0]:{1}.{3}} and {par_errors[1]:{1}.{3}}')
        file.close

    print(f'The standard deviation of amp and t2 are {par_errors[0]:{1}.{3}} and\
    {par_errors[1]:{1}.{3}}')
    print(f'The fit parameters and their errors have been written to {errors_file_name_write}')

    

    plt.title(r'Determination of Spin Echo Decay Time, ${T_2}^{,}$, in Glycerin', fontdict={'fontsize' : 20})
    #plt.suptitle(r'Determination of Spin Echo Decay Time, ${T_2}^{,}$, in Oil' ,fontdict={'fontsize' : 25})
    plt.xlabel(r'Time(ms)',fontdict={'fontsize' : 25})
    plt.ylabel(r"Voltage(V)" ,fontdict={'fontsize' : 25})
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

    #saves as a pdf, exclude if want to see first
    plt.savefig('glycerin t2 prime.pdf')


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

def exp_Fit(x,a,b):
    return (a*np.exp(-x*b))


imported_data = parse_file('glycerin t2 pulse train method minus 0.9 offset.csv', header=False)

imported_data =sort_data(imported_data)

errors_file_name_write = 'glycerin t2 prime.txt'


print(imported_data[0])
print(imported_data[1])


curve_fit_linear(imported_data)
#plotting(imported_data)