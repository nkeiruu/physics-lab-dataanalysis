import matplotlib.pyplot as plt
import numpy as np
from Parse_file_function import parse_file



'''
find relevant points.
In this case points corresponding to where graph starts leveling off
'''
def relevant_point_y_axis(graph_data):
    relevant_point_y = []
    #Find index of minimum x value of 2D array
    x_point_index =  np.where(graph_data[0] == min(graph_data[0]))[0]
    print(graph_data[0][x_point_index])
    #Find the actual values of minimum x point and its corresponding y
    relevant_point_y = [ graph_data[0][x_point_index][0], graph_data[1][x_point_index][0]]
    #finds a near by point(not necessarily adjacent) of relevant point so can plot line
    relevant_point_y2 = [ graph_data[0][x_point_index+ 4][0], graph_data[1][x_point_index+ 4][0]]
    print(relevant_point_y2)
    return(relevant_point_y, relevant_point_y2)



def relevant_point_x_axis(graph_data):
    prev_point = 0.0
    relevant_point_x = []
    delta = 1e-7 

    for point in graph_data[1]:
        if(abs(point-prev_point)> delta): #point where graph levels off (where stops changing much)
            prev_point = point
            continue
        else:
            index = np.where(graph_data[1] == point)[0] #finds index at prescribed point
            print ('index:', index)
            relevant_point_x = [graph_data[0][index][0], point ]  #Find the actual values of minimum x point and its corresponding y
              #finds a near by point(not necessarily adjacent) of relevant point so can plot line
            relevant_point_x2 = [graph_data[0][index+ 4][0], graph_data[1][index+ 4][0]] 
            break
    return(relevant_point_x, relevant_point_x2)



def derivative_at_point(xy_coord1, xycoord2):
    slope = (xycoord2[1] - xy_coord1[1])/(xycoord2[0]- xy_coord1[0])
    print('Top', xycoord2[1] - xy_coord1[1])
    print('bottom', xycoord2[0]- xy_coord1[0])

    print(f'The derivative at point{xy_coord1} and {xycoord2}is ',slope)
    return(slope)

def intersection_pt(slope1, xycoord1, slope2, xycoord2):
    #Equation for x intersection point using Cramer rule
    x_pt = (1*(slope2*xycoord2[0]-xycoord2[1])-(slope1*xycoord1[0]-xycoord1[1]))/(-1*slope1-(-1*slope2))
    return(x_pt)

def plotting(slope1, xycoord1, slope2, xycoord2):
    plt.figure(figsize=(8,6))
    x = np.linspace(0,3,1000)

    plt.title("Current vs Voltage: 577 nm", fontdict={'fontsize' : 30})
    plt.xlabel("Retarding Voltage(volts)")
    plt.ylabel("Anode Current(amps)")
    #plot data points
    plt.plot(imported_data1[0], imported_data1[1], 'ko')

    #plot 'tangent lines'
    plt.plot(x, x*slope1 -slope1*xycoord1[0] + xycoord1[1], 'r')
    plt.plot(x, x*slope2 -slope2*xycoord2[0] + xycoord2[1], 'g')
    plt.show()

    
        
imported_data1 = parse_file('577nm.csv')
points_closest_y_axis = relevant_point_y_axis(imported_data1)
point_closest_x_axis = relevant_point_x_axis(imported_data1)

#slope of the 2 lines
slope_higher2 = derivative_at_point(point_closest_x_axis[0], point_closest_x_axis[1])
slope_lower1 = derivative_at_point(points_closest_y_axis[0], points_closest_y_axis[1])

stopping_V_0 =intersection_pt(slope_lower1, points_closest_y_axis[0], 
slope_higher2, point_closest_x_axis[0])

plotting(slope_lower1, points_closest_y_axis[0], slope_higher2, point_closest_x_axis[0])

print (f' The point closest to y axis is: ', points_closest_y_axis)
print (f' The point closest to x axis is: ', point_closest_x_axis)

print (f' The slope of tangent line closest y axis: ', slope_lower1)
print (f' The slope of tangent line closest x axis: ', slope_higher2)
print (f' The intersection point (stopping potential): ', stopping_V_0)
