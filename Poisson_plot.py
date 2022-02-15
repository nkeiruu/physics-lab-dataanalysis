import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
from numpy import random
import seaborn as sns
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




def plotting():
    plt.figure(figsize=(14,10))
   
    #plt.errorbar(imported_data[0], imported_data[1], 'ko' )
    xfit = np.arange(17)
    #Mean
    b=3
    #poisson
    y1 =[(b**xfit[i])*np.exp(-b)/np.math.factorial(xfit[i]) for i in range(0, len(xfit))]
    
    plt.suptitle(r"Probability of N counts " ,fontdict={'fontsize' : 25})
    plt.xlabel(r'Number of counts',fontdict={'fontsize' : 20})
    plt.ylabel(r"Probability" ,fontdict={'fontsize' : 20})
    plt.plot(xfit,y1 , 'ko')
    
    sns.distplot(random.poisson(lam=3, size=16), hist=False, label=r'$\langle N \rangle ^{N} e^{-\langle N \rangle}/\langle N \rangle! where \langle N \rangle = 3$')
    plt.legend()
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


def poisson(x,b):
  
    return((b**x)*np.exp(-b)/np.math.factorial(x))
    

imported_data = parse_file('GM_background.csv', header=False)
#imported_data =sort_data(imported_data)
#print(imported_data[0])
#print(imported_data[1])
plotting()

