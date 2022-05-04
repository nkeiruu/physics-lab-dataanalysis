import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from Derived_Array_Data import new_array_formula

#makes the plot look nicer in latex
#mpl.use('pgf')
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,

    
    
})
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc({'pgf.preamble': r'\usepackage{amsmath}'})




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
    plt.gcf().set_size_inches(w=9.2, h=7.5)

    #use this if not putting into latex
    #plt.figure(figsize=(10,8))

    plt.plot(imported_data[0], imported_data[1], 'ko', markersize=4)
    #Set guessesfor the function parameters
    InitialGuess = [1000,590,20 ,1000,650,20, 950,720, 20,200, 950,780, 20, 200, 1000,830,20, 1000,930,20]

    #Curve fit for Lorentzian
    popt, pcov = curve_fit(_6Lorentzian, imported_data[0], imported_data[1], InitialGuess, maxfev=10000)
    xfit = np.arange(480,950, 0.001)
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(xfit,_6Lorentzian(xfit, *popt), 'r',\
    label = 'Lorentzian Fit ')
    plt.legend(loc="upper left")
    #print('y,z ', popt)
    #label= r'fit: $A= %1.2f e^{%1.3f t}$' % tuple(popt)
    #print(par[1], par[3], par[5], par[7])

    

    #Adding labels to graph
    plt.text(570, 2700, 'Lorentian Center Best Fits', color='k', fontsize=8,
        horizontalalignment="right", verticalalignment="top")

    
    eq1 = (  r'\begin{{align*}}'
             r'c_1 & = {0:.1f}\\'
             r'c_2 &= {1:.1f}\\'
             r'c_3 & = {2:.1f}\\'
             r'c_4 & = {3:.1f}\\'
             r'c_5 & = {4:.1f}\\'
             r'c_6 & = {5:.1f}\\'
             r'\end{{align*}}'.format(par[1], par[4], par[7], par[10], par[15], par[18]))
            
       

    plt.text(500, 2670, eq1, color='k', fontsize=8,
        horizontalalignment="left", verticalalignment="top")


    #Change plot appearance here
    plt.title("Velocity Calibration: Enriched Fe Absorber", fontdict={'fontsize' : 22})
    #plt.suptitle("Enriched Iron")
    plt.xlabel("Channels")
    plt.ylabel("Counts",fontsize=14)
   
    
  """ #Adding 2nd plot
   #The x axis dta
    chnls = np.array([par[1], par[4], par[7], par[10], par[15], par[18]])
    vlcty = np.array([-5.103,-2.859,-0.615,1.065,3.309,5.553])
   
   # twin object for two different y-axis on the sample plot
    axis2 = plt.twinx()

    # make a plot with different y-axis using second axis object
    axis2.plot(chnls, vlcty,"bo", markersize = 5)
    axis2.set_ylabel("Absorption Line Positions (mm/s)",color="blue",fontsize=14)

    #curve fit for line
    xfit2 = np.arange(583,950, 0.001)
    popt2, pcov2 = curve_fit(linear, chnls,vlcty, maxfev=1000)
    dx = 9.0
    par2 = tuple(popt2) 
    axis2.plot(xfit2, linear(xfit2, *popt2), 'b', label = r'Linear fit y={0:.3f}x + {1:.1f}'.format(par2[0], par2[1]))
    
    axis2.legend(loc="upper right")"""
    #saves as a pdf, exclude if want to see first
    plt.savefig('velocitcalfinal.pdf')

    plt.show()
    
    
    



def _6Lorentzian(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3,offset3, amp4,cen4,wid4,offset4,amp5,cen5,wid5,amp6,cen6,wid6):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (-amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
            (-amp3*wid3**2/((x-cen3)**2+wid3**2)-offset3) +\
            (-amp4*wid4**2/((x-cen4)**2+wid4**2)-offset4) +\
            (-amp5*wid5**2/((x-cen5)**2+wid5**2)) +\
                (-amp6*wid6**2/((x-cen6)**2+wid6**2))

"""def _Lorentzian(x, amp1, cen1, wid1):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)+21569) """
    
def linear(x,a,b):
    return (a*x + b)


imported_data = parse_file('data\Moss velocity calibration.csv', header=False)


#plotting(imported_data, imported_data2)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_lorentzian(imported_data)
