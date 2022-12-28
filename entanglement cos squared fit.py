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
    return (x_axis_data, y_axis_data)



def curve_fit_lorentzian(imported_data):
    plt.figure(figsize=(10,8))
    plt.plot(imported_data[0], imported_data[1], 'ro')
    #Set guessesfor the function parameters
    InitialGuess = [1200,2]

    #Curve fit 
    popt, pcov = curve_fit(cos_sqrd, imported_data[0], imported_data[1], InitialGuess, maxfev=10000)
    xfit = np.arange(0, 370, 0.1)
    par = tuple(popt) #This is  the optimal parameters
    plt.plot(xfit, cos_sqrd(xfit, *popt), 'b', label = r'$\frac{N_0}{2} \cos^2\left(\frac{\pi}{180}\right) \theta +135^{0}$')

    print('frequency in radians, ',par[1])
    freq_degrees = par[1] *(180/np.pi)
    print('frequency in degrees, ',freq_degrees)


    

    #Change plot appearance here
    plt.title(r"$\alpha$ = $135^0$, $N_0$ ={0:.3f}".format(par[0]), fontdict={'fontsize' : 15})
    #plt.suptitle("Isomer Shift")
    plt.xlabel(r"$\beta$ (degrees)")
    plt.ylabel("Coincidences")
    plt.legend(loc="upper left")
    plt.savefig('alpha135.pdf')
    plt.show()




"""def _6Lorentzian(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3,amp4,cen4,wid4,amp5,cen5,wid5,amp6,cen6,wid6):
    return (-amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (-amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
            (-amp3*wid3**2/((x-cen3)**2+wid3**2)-190) +\
            (-amp4*wid4**2/((x-cen4)**2+wid4**2)-190) +\
            (-amp5*wid5**2/((x-cen5)**2+wid5**2)) +\
                (-amp6*wid6**2/((x-cen6)**2+wid6**2))"""

def cos_sqrd(x, No, frq):
    return ((No/2)*(np.cos(frq*(x*2*np.pi/360 + (3*np.pi/4))))**2 ) 

imported_data = parse_file('a=135.csv', header=False)


#plotting(imported_data, imported_data2)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_lorentzian(imported_data)
