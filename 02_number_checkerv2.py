# number checker (version 2 with imporved 2nd angle calculator)
# check for valid numbers in a certain range of values
# allow float
# rounds the input of of the the angle down so that when they enter 89.999... the 2nd angle doesn't = 0

# import libraries
import math


# got this rounding down code from https://kodify.net/python/math/round-decimals/
# making sure that the input of the user doesn't break the 
# program when they enter something really close to 90
def round_decimals_down(number:float, decimals:int=2):
    
    # Returns a value rounded down to a specific number of decimal places.
    
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


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
get_angle = num_check("What is the value of the angle ", "Enter a value between 0 and 89.999\n", 0, 90, float)

# get the length of a side (used the float('inf') to represent an infinite integer, doesn't have a max restriction)
get_length = num_check("What is the length of one side ", "Enter a value greater than 0\n", 0, float('inf'), float)

# calculate the second angle (can be used for overall data for end results)

get_angle = round_decimals_down(get_angle, 3)

angle_two = 90 - get_angle

# prints results of input
print("Angle one: {:.3f}".format(get_angle))
print("Angle two: {:.3f}".format(angle_two))
