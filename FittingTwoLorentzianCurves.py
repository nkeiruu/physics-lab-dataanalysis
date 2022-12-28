import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import minimize
import csv
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble= r'\usepackage{amsmath}')
plt.rcParams.update({'font.size': 22})
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

#Calculate new array
def new_array_formula(raw_data):
    new_data = np.array([])
    new_data = 0.03201*raw_data-23.7 #Input formula here
    #print("-raw",raw_data)
    #print("new",new_data)
    return(new_data)

def curve_fit_lorentzian(imported_data):

    #change this according to text width in latex if putting picture here
    #plt.gcf().set_size_inches(w=7.058, h=5.4)

    #use this if not putting into latex
    plt.figure(figsize=(10,8))

    plt.plot(computed_data, imported_data[1], 'ko', markersize=3)

    #Set guessesfor the function parameters
    #InitialGuess = [2500,0.7,0.2 ,1000,-2.6,0.2, 950,-0.5, 0.3,200, 950,0.5, 0.2, 200, 1000,3,0.3, 1000,6,0.2]
    InitialGuess = [ 9.9e+02 , -5.1 , 2.01e-01  ,9.935e+02,
    -2.59  ,2.01e-01  ,6.46e+02 ,-0.56,
    0.3,  230 ,650  ,1.04,
   0.3, 209,  8.5e+02 , 3.1,
   2.01e-01 , 9.20306886e+02  ,5.6 , 2.01e-01, 370]
    #rest = [,1000,-2.6,0.2, 950,-0.5, 0.3,200, 950,0.5, 0.2, 200, 1000,3,0.3, 1000,6,0.2]

    #Curve fit for Lorentzian
    popt, pcov = curve_fit(_6Lorentzian_parms, computed_data, imported_data[1], InitialGuess, maxfev=10000)
    xfit = np.arange(480,950, 0.001)
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(computed_data,_6Lorentzian_parms(computed_data, *popt), 'r',\
    label = 'Lorentzian Fit '.format(par[2]))
    par_errors= tuple(np.sqrt(np.diag(pcov)))
    
    
    """plt.plot(computed_data,_6Lorentzian_parms(computed_data,1.13283321e+03, -5.00049795e+00,  2.18814448e-01 , 1.04934716e+03,
 -2.80428485e+00,  2.54305062e-01 , 9.61387448e+02 ,-5.76440796e-01,
  2.53615072e-01, -3.73414042e+02 , 7.32325968e+02 , 1.05241454e+00,
  1.88575787e-01,  1.21001810e+02 , 9.35964225e+02 , 3.32183801e+00,
  3.05638316e-01,  9.86075936e+02 , 5.67761450e+00,  2.91625417e-01,
  7.95583988e+02
    ))"""


    # print("width, width error, center, center error", par[2], par_errors[2], par[1], par_errors[1])
    #print("par", par)
    #label= r'fit: $A= %1.2f e^{%1.3f t}$' % tuple(popt)
    #print(par[1], par[3], par[5], par[7])
  

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


    #Adding labels to graph
    """plt.text(6, 21000, r'Velocity shift: {0:.3f} mm/s'.format(par[1]), color='k', fontsize=12,
        horizontalalignment="right", verticalalignment="top")"""

    
    """eq1 = (  r'\begin{{align*}}'
             r'c_1 & = {0:.1f}\\'
             r'c_2 &= {1:.1f}\\'
             r'c_3 & = {2:.1f}\\'
             r'c_4 & = {3:.1f}\\'
             r'c_5 & = {4:.1f}\\'
             r'c_6 & = {5:.1f}\\'
             r'\end{{align*}}'.format(par[1], par[4], par[7], par[12], par[15], par[18]))
            
                     
    plt.text(6.5, 2600, eq1, color='k', fontsize=8,
        horizontalalignment="left", verticalalignment="top")"""

        #chi squares statisitic calculator
    def chi_sqrd( measurements, fit_ftn, guess):
        #print('output of fit function:', fit_ftn(computed_data, guess))
        chi2= lambda param: np.sum((measurements-fit_ftn(computed_data, param))**2/fit_ftn(computed_data,param))
        result = minimize(chi2, guess, method='Nelder-Mead')
        chi2_min = result.fun
        print ("best fit is:", result.x, "with chi2:", chi2_min)
       

    chi_sqrd(imported_data[1],_6Lorentzian_parmlist,InitialGuess)




    #Change plot appearance here
    plt.title("Zeeman Effect: Enriched FeAbsorber", fontdict={'fontsize' : 26})
    #plt.suptitle("Enriched Iron")
    plt.xlabel("Velocity Shift (mm/s)",fontsize=24)
    plt.ylabel("Counts",fontsize=24)
    plt.legend(loc="upper left")
    plt.savefig('zeeman_final2.pdf')
    plt.show()
    
    """Adding 2nd plot
      #The x axis dta
      chnls = np.array([par[1], par[4], par[7], par[10], par[15], par[18]])
      vlcty = np.array([-5.103,-2.859,-0.615,1.065,3.309,5.553])
   
   # twin object for two different y-axis on the sample plot
    axis2 = plt.twinx()

    # make a plot with different y-axis using second axis object
    axis2.plot(computed_data,  _Lorentzian(computed_data,2.735e3,7.4e-1,2.59e-1),"bo", markersize = 5)
    axis2.set_ylabel("sith chi square",color="blue",fontsize=14)
   
    #saves as a pdf, exclude if want to see first
    #plt.savefig('velocitcal3.pdf')"""


  #InitialGuess = [1000,-5,0.2 ,1000,-2.6,0.2, 950,-0.5, 0.3,200, 950,0.5, 0.2, 200, 1000,3,0.3, 1000,6,0.2]


"""def _6Lorentzian(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3,offset3, amp4,cen4,wid4,offset4,amp5,cen5,wid5,amp6,cen6,wid6):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (-amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
            (-amp3*wid3**2/((x-cen3)**2+wid3**2)-offset3) +\
            (-amp4*wid4**2/((x-cen4)**2+wid4**2)-offset4) +\
            (-amp5*wid5**2/((x-cen5)**2+wid5**2)) +\
                (-amp6*wid6**2/((x-cen6)**2+wid6**2))"""

def _6Lorentzian_parms(x,     
                 amp1,
                 cen1,
                 wid1,
                 amp2,
                 cen2,
                 wid2,
                 amp3,
                 cen3,
                 wid3, 
                 offset3,
                 amp4,
                 cen4,
                 wid4, 
                 offset4,
                 amp5,
                 cen5,
                 wid5,
                 amp6,
                 cen6,
                 wid6,
                 off):
    
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)+off) +\
           (-amp2*wid2**2/((x-cen2)**2+wid2**2)+off) +\
           (-amp3*wid3**2/((x-cen3)**2+wid3**2)-offset3) +\
           (-amp4*wid4**2/((x-cen4)**2+wid4**2)-offset4) +\
           (-amp5*wid5**2/((x-cen5)**2+wid5**2)+off) +\
           (-amp6*wid6**2/((x-cen6)**2+wid6**2)+off)


def _6Lorentzian_parmlist(x, parms):
    amp1 = parms[0]
    cen1 = parms[1]
    wid1 = parms[2]
    amp2 = parms[3]
    cen2 = parms[4]
    wid2 = parms[5]
    amp3 = parms[6]
    cen3 = parms[7]
    wid3 = parms[8] 
    offset3 = parms[9]
    amp4 = parms[10]
    cen4 = parms[11]
    wid4 = parms[12] 
    offset4 = parms[13]
    amp5 = parms[14]
    cen5 = parms[15]
    wid5 = parms[16]
    amp6 = parms[17]
    cen6 = parms[18]
    wid6 = parms[19]
    off = parms[20]

    result =  (-amp1*wid1**2/((x-cen1)**2+wid1**2)+off) +\
              (-amp2*wid2**2/((x-cen2)**2+wid2**2)+off) +\
              (-amp3*wid3**2/((x-cen3)**2+wid3**2)-offset3) +\
              (-amp4*wid4**2/((x-cen4)**2+wid4**2)-offset4) +\
              (-amp5*wid5**2/((x-cen5)**2+wid5**2)+off) +\
              (-amp6*wid6**2/((x-cen6)**2+wid6**2)+off)

    return result

imported_data = parse_file('Moss_velocity_calibration.csv', header=False)
computed_data = new_array_formula(imported_data[0])
parameters_file_name_write = 'moss parameters.csv'

#plotting(imported_data, imported_data2)



curve_fit_lorentzian(imported_data)

