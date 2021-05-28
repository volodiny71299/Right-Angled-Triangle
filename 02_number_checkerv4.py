# number checker
# check for valid numbers in a certain range of values
# allow float

# importing libraries
import numpy


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
get_angle = num_check("What is the value of the angle ", "Please enter a valid number\nGreater than 1 or less than 89\n", 1, 89, float)

# get the length of a side (used the float('inf') to represent an infinite integer, doesn't have a max restriction)
get_length = num_check("What is the length of one side ", "Enter a value greater than 0\n", 0, float('inf'), float)

# calculate the second angle (can be used for overall data for end results)
get_angle = numpy.round(get_angle)
angle_two = 90 - get_angle

print()

# prints results of input
print("Angle one: {:.3f}".format(get_angle))
print("Angle two: {:.3f}".format(angle_two))
print("Side length: {:.3f}".format(get_length))
