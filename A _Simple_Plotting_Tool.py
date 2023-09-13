#A Simple Plotting Tool
#3/3/2022
import numpy as np
import matplotlib.pyplot as plt


#List of x values
xlist = np.array(np.arange(0.5,4,0.1))

# input Fuction
f_x= 1/(np.exp(1/xlist )-1)


#Plotting
plt.figure(figsize=(10,8))
plt.plot(xlist, f_x, marker = "o")
plt.xlabel("KT/hw")
plt.ylabel("<n>")
plt.show()