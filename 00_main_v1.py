# main code with added functions
# importing libraries
import numpy


# original code from - https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
# element of each sublist in a list of lists
def Extract(lst):
    return [item[0] for item in lst]


# function goes here
def string_check(choice, options):

    for var_list in options:

        # if the unit is valid, return the first item
        if choice in var_list:

            # get the first item of sublist in valid_lengths
            chosen = var_list[0]
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the length is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# number checker with custom error message with
# minimum and max value and number type choice
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


# Function to get length units
def valid_length():
    
    # set up a list of valid options for the length values
    # helps with formating overall resutls
    valid_length = [
        ["mm", "millimetres", "millimeters"],
        ["cm", "centimetres", "centimeters"],
        ["m", "metres", "meters"],
        ["km", "kilometres", "kilometers"]
        ]

    # default unit if user chooses to not choose anything
    length_auto = "units"

    # start of while loop
    length_unit = ""
    while length_unit != "invalid choice":
        
        # get the users unit for the length
        length_unit = input("Choose your measuring unit or type 'xxx' to keep it default (units)\n").lower()

        # if user chooses to type in 'xxx' chooses 'units' as default measuring unit
        if length_unit == "xxx":
            return length_auto

        # checks that the item is in valid_length list
        length_choice = string_check(length_unit, valid_length)

        # if the choice is good returns the chosen item
        if length_choice != "xxx" and length_choice != "invalid choice":
            return length_choice

        # if not in list, prints an error to try again
        else:
            print("Error, please try again\n")


# list of valid options of what can be calculated
valid_calculation = [
    ["angle", "an"],
    ["area", "ar"],
    ["hypotenuse", "h"],
    ["perimeter", "perimetre", "p"],
    ["short side", "leg", "ss"]
]

# yes and no function for
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

calculation = 0

while calculation != "xxx":
    # ask user what they are calculating
    calculation = input("What to calculate? ").lower()

    # if the exit code is entered, stops the loop
    if calculation == "xxx":
        break

    # checks that the input for what is needed to be calculated is correct
    calculation_choice = string_check(calculation, valid_calculation)

    # if the input is correct return a message saying what you chose
    if calculation_choice != "xxx" and calculation_choice != "invalid choice":
        # check calculation option is valid
        print("You want to calculate '{}'".format(calculation_choice))
        print()
        break

    # print error message and separate first item of sublist and put it into error message
    else:
        # code to separate messages -
        # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
        print("Error, please try again\n"
              "Valid options are -", ', '.join(Extract(valid_calculation)), "\n")


# getting mesuring untis
get_units = valid_length()


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
print("Side length: {:.3f} {}".format(get_length, get_units))
