#A Simple Plotting Tool
#3/3/2022
import numpy as np
import matplotlib.pyplot as plt

def simple_plot(x_start, x_end, f_x,x_label,y_label):
    
    #List of x values
    xlist = np.array(np.arange(x_start,x_end,0.1))
    
    # input Fuction
    f_x= 1/(np.exp(1/xlist )-1)
    
    
    #Plotting
    plt.figure(figsize=(10,8))
    plt.plot(xlist, f_x, marker = "o")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

    if __name__ == "__main__":
        import sys
        print(f"Enter x axis start, x axis end, numpy function expression (use xlist as x), x axis label, y axis label")
        simple_plot(float(sys.argv[1]), float(sys.argv[2]),sys.argv[3],sys.argv[4], sys.argv[5]  )