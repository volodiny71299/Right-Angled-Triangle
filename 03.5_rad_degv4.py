# https://www.geeksforgeeks.org/numpy-radians-deg2rad-python/

# Python3 program explaining
# degrees() function

import numpy as np
import math

in_array = np.arange(10.) * 90
print ("Degree values : \n", in_array)

radian_Values = np.radians(in_array)
print ("\nRadian values : \n", radian_Values)


# number checker, has a custom question, error message and high and low values to 
# make sure user doesn't enter negative values for length/angle
def num_check(question, error, low, high, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low < response < high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
get_angle = num_check("\nWhat is the value of the angle ", "Enter a value between 0 and 90\n", 0, 90, float)

get_angle_radian = np.radians(get_angle)
print("\nRadian value:\n", get_angle_radian)
