
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import minimize
import csv
#from Derived_Array_Data import new_array_formula

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
    counter = 0
    with open(file_name) as file:
        for line in file:
            if(header == True): #skips first line if function call is set to true
                header = False
                continue
            split_line = line.split(',')
            x_axis_data = np.append(x_axis_data, float(split_line[0]))
            y_axis_data = np.append(y_axis_data, float(split_line[1]))
            counter+=1
    print('Amount of data points:', counter)
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
    par_errors= tuple(np.sqrt(np.diag(pcov)))

    #The best fit parameters
    amp1 = par[0]
    cen1 = par[1]
    wid1 = par[2]
    amp2 = par[3]
    cen2 = par[4]
    wid2 = par[5]
    amp3 = par[6]
    cen3 = par[7]
    wid3 = par[8] 
    offset3 = par[9]
    amp4 = par[10]
    cen4 = par[11]
    wid4 = par[12] 
    offset4 = par[13]
    amp5 = par[14]
    cen5 = par[15]
    wid5 = par[16]
    amp6 = par[17]
    cen6 = par[18]
    wid6 = par[19]
    
    #The best fit errors
    amp1_er = par_errors[0]
    cen1_er = par_errors[1]
    wid1_er = par_errors[2]
    amp2_er = par_errors[3]
    cen2_er = par_errors[4]
    wid2_er = par_errors[5]
    amp3_er = par_errors[6]
    cen3_er = par_errors[7]
    wid3_er = par_errors[8] 
    offset3_er = par_errors[9]
    amp4_er = par_errors[10]
    cen4_er = par_errors[11]
    wid4_er = par_errors[12] 
    offset4_er = par_errors[13]
    amp5_er = par_errors[14]
    cen5_er = par_errors[15]
    wid5_er = par_errors[16]
    amp6_er = par_errors[17]
    cen6_er = par_errors[18]
    wid6_er = par_errors[19]

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
             r'\end{{align*}}'.format(par[1], par[4], par[7], par[11], par[15], par[18]))
            
       

    plt.text(500, 2670, eq1, color='k', fontsize=8,
        horizontalalignment="left", verticalalignment="top")


    #Change plot appearance here
    plt.title("Velocity Calibration: Enriched Fe Absorber", fontdict={'fontsize' : 22})
    #plt.suptitle("Enriched Iron")
    plt.xlabel("Channels")
    plt.ylabel("Counts",fontsize=14)
   
    
  #Adding 2nd plot
   #The x axis dta
    chnls = np.array([par[1], par[4], par[7], par[11], par[15], par[18]])
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
    axis2.plot(xfit2, linear(xfit2, *popt2), 'b', label = r'Linear fit y={0:.5f}x + {1:.1f}'.format(par2[0], par2[1]))

    #write fit parameters to csv file
    header = ['amp', 'amp error', 'center', 'center error', 'width', 'width error']    
    values = [
    [amp1,amp1_er,cen1, cen1_er,wid1,wid1_er],
    [amp2, amp2_er,cen2, cen2_er, wid2, wid2_er],
    [amp3, amp3_er, cen3, cen3_er, wid3,wid3_er],
    [amp4,amp4_er,cen4,cen4_er, wid4, wid4_er],
    [amp5,amp5_er, cen5, cen5_er, wid5, wid5_er],
    [amp6, amp6_er, cen6, cen6_er, wid6, wid6_er]

    ]                                                 

    with open(parameters_file_name_write, "w+", newline='') as file:
        writer =csv.writer(file)
        writer.writerow(header)
        writer.writerows(values)


    axis2.legend(loc="upper right")

    #chi squares statisitic calculator
    def chi_sqrd( measurements, fit_ftn, guess):
        chi2= lambda param: np.sum((measurements- fit_ftn(imported_data[0], param)**2/fit_ftn(imported_data[0],param)))
        result = minimize(chi2, guess, method='Nelder-Mead')
        chi2_min = result.fun
        print ("best fit is:", result.x, "with chi2:", chi2_min)


    chi_sqrd(imported_data[0],_6Lorentzian,InitialGuess)

    #saves as a pdf, exclude if want to see first
    #plt.savefig('velocitcalfinal2.pdf')

    plt.show()
    
    
    



def _6Lorentzian(x, param):
    #The best fit parameters
    amp1 = param[0]
    cen1 = param[1]
    wid1 = param[2]
    amp2 = param[3]
    cen2 = param[4]
    wid2 = param[5]
    amp3 = param[6]
    cen3 = param[7]
    wid3 = param[8] 
    offset3 = param[9]
    amp4 = param[10]
    cen4 = param[11]
    wid4 = param[12] 
    offset4 = param[13]
    amp5 = param[14]
    cen5 = param[15]
    wid5 = param[16]
    amp6 = param[17]
    cen6 = param[18]
    wid6 = param[19]
    
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
parameters_file_name_write = 'moss parameters.csv'
curve_fit_lorentzian(imported_data)
