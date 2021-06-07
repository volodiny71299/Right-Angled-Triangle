# get degree or radians
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


# turning first item of each sublist into a list
def Extract(lst):
    return [item[0] for item in lst]


# checks for valid input from the user, keeps going until valid
def string_check(choice, options):

    for var_list in options:

        # if the unit is valid, return the first item
        if choice in var_list:

            # get the first item of sublist in deg_rad
            chosen = var_list[0]
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the unit is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# get deg/rad for your measurements
def deg_rad():
    
    deg_rad_list = [
        ["degrees", "degree", "deg", "d"],
        ["radians", "radian", "rad", "r"]
    ]

    angle_input = ""
    while angle_input != "invalid choice":

        angle_input = input("Degree or radians? ").lower()

        chosen_angle = string_check(angle_input, deg_rad_list)
        
        if chosen_angle != "invalid choice":
            return chosen_angle

        else:
            print("Please choose between -", ' and '.join(Extract(deg_rad_list)), "\n")

# getting mesuring untis
get_deg_rad = deg_rad()

# prints out the unit that the user chose
print("You chose to use {} for your angle measurements".format(get_deg_rad))

if get_deg_rad == "degrees":
    angle_value = int(input("How much "))
    rad_value = np.radians(angle_value)
    print(rad_value)

else:
    angle_value = (input("How much "))
    deg_value = np.deg2rad(angle_value)
    print(deg_value)
