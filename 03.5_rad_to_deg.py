# testing to convert degrees into rad
# import libraries
import numpy as np




# number checker with custom error messages and max and min limits
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

angle_value = num_check("What is the length of a known angle? ", "Please try again", 1, 89, float)

rad_angle_value = np.radians(angle_value)

print("{:.3f} Degrees\nor\n{} Radians".format(angle_value, rad_angle_value))
