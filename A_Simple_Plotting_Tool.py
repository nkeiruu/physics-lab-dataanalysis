#A Simple Plotting Tool
#3/3/2022
'''Rewritten Sep 17 2023 to be reusable function and a script, 5 arguments needed to run as script
x_start: graph lower bound (float)
x_end: graph upper bound (float)
f_x: function expression, quotation marks must be added around expession
xlabel, ylabel: respective graph labels (string)
'''
import numpy as np
import matplotlib.pyplot as plt

def simple_plot(x_start, x_end, f_x,x_label,y_label):
    
    #List of x values
    x = np.array(np.arange(x_start,x_end,0.1))
    
    # input Fuction
    #f_x= 1/(np.exp(1/x )-1)

    #Evaluates the expreeion and returns result
    ret_f_x= eval(f_x)
          
    
    
    #Plotting
    plt.figure(figsize=(10,8))
    plt.plot(x, ret_f_x, marker = "o")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

if __name__ == "__main__":
    import sys
    #print(sys.argv)
    simple_plot(float(sys.argv[1]), float(sys.argv[2]),sys.argv[3],sys.argv[4], sys.argv[5])