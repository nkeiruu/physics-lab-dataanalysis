import numpy as np

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