# Python program explaining
# cos() function

import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)

cos_Values = np.cos(in_array)
print ("\nCosine values : \n", cos_Values)


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
get_angle = num_check("What is the value of the angle ", "Enter a value between 0 and 90\n", 0, 90, float)

get_angle_cosine = np.cos(get_angle)
print ("\nCosine value : \n", get_angle_cosine)