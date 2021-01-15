import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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



def curve_fit_lorentzian(imported_data, imported_data2):
    plt.figure(figsize=(10,8))
    plt.plot(imported_data[0], imported_data[1], 'ro')
    plt.plot(imported_data2[0], imported_data2[1], 'ko')
    #What your guesses are for the function parameters
   # InitialGuess = [1,3/20000, 1/2000,0.000000650]

    popt, pcov = curve_fit(lorentzian_func, imported_data[0], imported_data[1], maxfev=1000)
    xfit = np.arange(-2.5, 2.5, 0.001)
    plt.plot(xfit, lorentzian_func(xfit, *popt), 'r', label='Single Slit Pattern')
    print('y,z ', popt)

    popt2, pcov2 = curve_fit(lorentzian_func2, imported_data2[0], imported_data2[1], maxfev=1000)
    xfit2 = np.arange(-2.5, 2.5, 0.001)
    plt.plot(xfit, lorentzian_func2(xfit2, *popt2), 'k', label='Double Slit Pattern')
    print('y2,z2 ', popt2)

    plt.title("Lab 8: Diffraction", fontdict={'fontsize' : 30})
    plt.suptitle("Nkeiru Ubadike")
    plt.xlabel("Radians")
    plt.ylabel("Intensity (I/I max, volts)")
    plt.legend(loc="upper left")
    plt.show()




def lorentzian_func(x,I,d,w):
    return (I*((np.sin((np.pi*d*np.sin(x))/w))**2)/((np.pi*d*np.sin(x))/w)**2)

def lorentzian_func2(x,I,d,l,w):
    return (I*(np.sinc(np.pi*d*np.sin(x)/(w))**2)*((np.sin(2*np.pi*l*np.sin(x))/(w))**2)/((np.sin(np.pi*l*np.sin(x)/(w)))**2))

imported_data = parse_file('Lab8NormalizedSingleSlit.csv', header=False)
imported_data2 = parse_file('NormalizedDoubleSlit.csv', header=False)

#plotting(imported_data, imported_data2)

#print(imported_data[0])
#print(imported_data[1])

curve_fit_lorentzian(imported_data, imported_data2)