import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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
    plt.figure(figsize=(10,8))
    plt.plot(imported_data[0], imported_data[1], 'ro')
    #Set guessesfor the function parameters
    InitialGuess = [2500,764,25]

    #Curve fit for 1st Lorentzian
    popt, pcov = curve_fit(_cos_sqrd, imported_data[0], imported_data[1], maxfev=10000)
    xfit = np.arange(706, 813, 0.001)
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(xfit,_cos_sqrd576y(xfit, *popt), 'b', label = r'fit eqn: $L$ = -$frac{{0:.3f}*{2:.4f}^2}{(x-{1:.4f})^2 + {2:.4f}^2}+21569$ '.format(par[0], par[1],par[2]))
    #print('y,z ', popt)


    

    #Change plot appearance here
    plt.title("Stainless Steel Absorber", fontdict={'fontsize' : 30})
    plt.suptitle("Isomer Shift")
    plt.xlabel("Channels")
    plt.ylabel("Counts")
    plt.legend(loc="upper left")
    plt.show()




"""def _6Lorentzian(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3,amp4,cen4,wid4,amp5,cen5,wid5,amp6,cen6,wid6):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (-amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
            (-amp3*wid3**2/((x-cen3)**2+wid3**2)-190) +\
            (-amp4*wid4**2/((x-cen4)**2+wid4**2)-190) +\
            (-amp5*wid5**2/((x-cen5)**2+wid5**2)) +\
                (-amp6*wid6**2/((x-cen6)**2+wid6**2))"""

def cos_sqrd(x, No, b, a):
    return ((No/2)*(np.cos(b + a))^2) 

imported_data = parse_file('Isomer shift data to fit.csv', header=False)


#plotting(imported_data, imported_data2)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_lorentzian(imported_data)
