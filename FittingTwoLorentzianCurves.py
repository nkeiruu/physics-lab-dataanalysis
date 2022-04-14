import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble= r'\usepackage{amsmath}')

#makes the plot look nicer in latex
"""mpl.use('pgf')
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})"""

# Parses csv file and stores them in 2 arrays
def parse_file(file_name, header=False):
    x_axis_data = np.array([])
    y_axis_data = np.array([])
    with open(file_name) as file:
        for line in file:
            if(header == True): #skips first line if function call is set to true
                header = False
                continue
            split_line = line.split(',')
            x_axis_data = np.append(x_axis_data, float(split_line[0]))
            y_axis_data = np.append(y_axis_data, float(split_line[1]))
    return [x_axis_data, y_axis_data]



def curve_fit_lorentzian(imported_data):

    #change this according to text width in latex if putting picture here
    #plt.gcf().set_size_inches(w=7.058, h=5.4)

    #use this if not putting into latex
    plt.figure(figsize=(10,8))

    plt.plot(imported_data[0], imported_data[1], 'ko', markersize=4)
    #Set guessesfor the function parameters
    InitialGuess = [1000,590,20 ,1000,650,20, 950,720, 20,200, 950,780, 20, 200, 1000,830,20, 1000,930,20]

    #Curve fit for 1st Lorentzian
    popt, pcov = curve_fit(_6Lorentzian, imported_data[0], imported_data[1], InitialGuess, maxfev=10000)
    xfit = np.arange(480,950, 0.001)
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(xfit,_6Lorentzian(xfit, *popt), 'r',\
    label = r'Lorentzian Fit c1 = {0}'.format(par[1]))
    #print('y,z ', popt)
    #label= r'fit: $A= %1.2f e^{%1.3f t}$' % tuple(popt)
    #print(par[1], par[3], par[5], par[7])

   

    plt.text(1500, 2700, 'Lorentian Center Parameters', color='k', fontsize=12,
        horizontalalignment="right", verticalalignment="top")

    #Add label to graph
    eq1 = (  r'\begin{{align*}}'
             r'c_1 & = {0:.1f}\\'
             r'c_2 &= {1:.1f}\\'
             r'c_3 & = {2:.1f}\\'
             r'c_4 & = {3:.1f}\\'
             r'c_5 & = {4:.1f}\\'
             r'c_6 & = {5:.1f}\\'
             r'\end{{align*}}'.format(par[1], par[4], par[7], par[10], par[13], par[16]))
            
                     
    plt.text(1000, 2600, eq1, color='k', fontsize=8,
        horizontalalignment="right", verticalalignment="top")


    

    #Change plot appearance here
    plt.title("Velocity Calibration", fontdict={'fontsize' : 25})
    plt.suptitle("Enriched Iron")
    plt.xlabel("Channels")
    plt.ylabel("Counts")
    plt.legend(loc="upper left")
    plt.show()
    

    #saves as a pdf, exclude if want to see first
    #plt.savefig('velocitcal2.pdf')




def _6Lorentzian(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3,offset3, amp4,cen4,wid4,offset4,amp5,cen5,wid5,amp6,cen6,wid6):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (-amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
            (-amp3*wid3**2/((x-cen3)**2+wid3**2)-offset3) +\
            (-amp4*wid4**2/((x-cen4)**2+wid4**2)-offset4) +\
            (-amp5*wid5**2/((x-cen5)**2+wid5**2)) +\
                (-amp6*wid6**2/((x-cen6)**2+wid6**2))

"""def _Lorentzian(x, amp1, cen1, wid1):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)+21569) """

imported_data = parse_file('data\Moss velocity calibration.csv', header=False)


#plotting(imported_data, imported_data2)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_lorentzian(imported_data)
