import matplotlib.pyplot as plt
import numpy as np
#Parsing CSV file
#Reads info line by line each column seperated by column

#frequencies = np.array([400, 600, 1000, 1200, 1400])

def parse_file(file_name, header= True): #header ensures python disregards header
    x_Axis_data = np.array([]) #Hold info from CSV
    y_Axis_data = np.array([])
#opens environment
    with open(file_name) as file:
        for line in file:
            if header == True:
                header = False  #Ensure loop only runs once
                continue # Skips everything below during first iteration of for loop
            #splits array by comma seperated, stores split line into array
            split_line =line.split(',') 

            #Appends data to array
            x_Axis_data = np.append(x_Axis_data,float(split_line[0]))
            y_Axis_data = np.append(y_Axis_data,float(split_line[1]))
            #print(float(split_line[3])) #changes to int array so I can manipulate
            #print(float(split_line[4]))
    #This is a tuple two arrays        
    return(x_Axis_data, y_Axis_data)

def plotting(imported_data1, imported_data2, imported_data3,
        linear_regression1, linear_regression2, linear_regression3):
    #Set size of your canvas in inches (I know, this is weird)
    plt.figure(figsize=(8,6))
    #Plot your first graph
    plt.plot(imported_data1[0], imported_data1[1], 'ro')
    plt.plot(imported_data2[0], imported_data2[1], 'ko')
    plt.plot(imported_data3[0], imported_data3[1], 'bo')

    
    plt.plot(linear_regression1[0], linear_regression1[1], 'r', label= "Trial 1")
    plt.plot(linear_regression2[0], linear_regression2[1], 'k', label= "Trial 2")
    plt.plot(linear_regression3[0], linear_regression3[1], 'b', label= "Trial 3")
    
    plt.legend(loc="upper left")

    
    #Graph title and labels
    plt.title("Number of Fringes Passed,m, as a Function of Distance Moved by Movable Mirror", fontdict={'fontsize' : 9})
   # plt.suptitle("Number of Fringes Passed,m, as a Function of Distance Moved by Movable Mirror")
    plt.xlabel("Fringe Number")
    plt.ylabel("Distance [m]")
    plt.errorbar(imported_data1[0], imported_data1[1], xerr=0.5, yerr=0.5e-6, fmt ='.r', capsize=5, capthick= 1)
    plt.errorbar(imported_data2[0], imported_data2[1], xerr=0.5, yerr=0.5e-6, fmt ='.k', capsize=5, capthick= 1)
    plt.errorbar(imported_data3[0], imported_data3[1], xerr=0.5, yerr=0.5e-6,fmt ='.b', capsize=5, capthick= 1)
    plt.show()

#sorting Functiom
def sort_data(imported_data):
    #implementation of insertion sort
    #check insertion sort in action here: https://visualgo.net/en/sorting
    
    i = 1 #starting from the element at index 1
    while(i < len(imported_data[0])): #loop while i is less than the size of the array
        j = i #for each iteration, set j to be equal to i
        while(j > 0): #loop until j is equal to zero
            if(imported_data[0][j] < imported_data[0][j-1]): #if the current value at index j is less than current value at index j - 1
                #then swap the data, make sure that the relationship between elements of x axis is preserved with elements of y axis
                #sorting x-axis data
                temp = imported_data[0][j]
                imported_data[0][j] = imported_data[0][j-1]
                imported_data[0][j-1] = temp
                #sorting y-axis data
                temp = imported_data[1][j]
                imported_data[1][j] = imported_data[1][j-1]
                imported_data[1][j-1] = temp
            j -= 1 #decrease j by 1
        i += 1 #increase i by 1
    return imported_data #return the sorted data

def linear_regression(imported_data): 
    n = len(imported_data[0]) #number of elements in x axis (same as y axis)
    add_x = sum(imported_data[0])   #add all x axis elements
    add_y = sum(imported_data[1])   #add all y axis elements
    add_x_sqr = sum([i**2 for i in imported_data[0]]) #add all y axis elements squared
    add_xy = sum([imported_data[0][i] * imported_data[1][i] for i in range(0, n)]) #add the product of each corresponding pair from x and y
    y_intercept = (add_y * add_x_sqr - add_x * add_xy) / (n * add_x_sqr - add_x**2) #compute the y intercept of the linear regression
    slope = (n * add_xy - add_x * add_y) / (n * add_x_sqr - add_x**2) #compute slope of linear regression 
    slopevals = np.array([])
    slopevals = np.append(slopevals, slope)#array of slope vals
    print(slopevals)

    #print("Slope:",slope)
    #range_val = int(max(imported_data[0]) - min(imported_data[0])) #compute range of the x axis values
    lin_reg_x = [i for i in range(3, 35)] #create list of elements from 0 to range, determines how far regression goes
    lin_reg_y = [slope * i + y_intercept for i in lin_reg_x] #replace x value in equation to find the y in linear regression
    return [lin_reg_x, lin_reg_y] #return both lists

    


#This is where tuple is stores    
imported_data1 = parse_file(r'C:\Users\Nkeiru\Google Drive\Stony Brook University\Spring 2021\Modern Physics PHY 251\LAB\Lab 1\PHY252_Lab1_T1.csv')
imported_data2 = parse_file(r'C:\Users\Nkeiru\Google Drive\Stony Brook University\Spring 2021\Modern Physics PHY 251\LAB\Lab 1\PHY252_Lab1_T2.csv')
imported_data3 = parse_file(r'C:\Users\Nkeiru\Google Drive\Stony Brook University\Spring 2021\Modern Physics PHY 251\LAB\Lab 1\PHY252_Lab1_T3.csv')



#imported_data = sort_data(imported_data)




linear_regression1 = linear_regression(imported_data1)
linear_regression2 = linear_regression(imported_data2)
linear_regression3 = linear_regression(imported_data3)

plotting(imported_data1, imported_data2, imported_data3, 
    linear_regression1, linear_regression2, linear_regression3)




#prints what is in my current directory
#print(os.listdir())