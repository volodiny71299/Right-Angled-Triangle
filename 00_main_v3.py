# main code v2
# Sources for codes ->
# Extract function - https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
# List with no brackets (print) - https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# trigonometry - # https://stackoverflow.com/questions/46958547/finding-an-unknown-length-of-a-side-using-sohcahtoa-trigonometry

# import libraries
import math

# Functions list


# extracts the items in the list as a single item
def Extract(lst):
    return [item[0] for item in lst]


# string checker (checks for item in list upon users input)
def string_check(choice, options):

    for var_list in options:

        # if the calculation is in one of the lists, return the full item
        if choice in var_list:

            # get full name of snack and put it in title case so it looks nice when outputted
            chosen = var_list[0]
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the calculation is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid input"


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


# function which calculates the side length based on the users input
def trig_norm(angle, side_name, side_length, unknown):
    angle = math.radians(angle)
    # Unknown poss:
        # hyp
        # opp
        # adj
    
    # calculates the side length when the known side of the triangle is hypotenuse
    if side_name == 'hypotenuse':

        # calculates the length when opposite is unknown
        if unknown == 'opposite':
            return side_length * math.sin(angle)

        # calculates the length when adjacent is unknown
        elif unknown == 'adjacent':
            return side_length * math.cos(angle)
    
    # calculates the side length when the known side of the triangle is opposite
    elif side_name == 'opposite':

        # calculates the length when hypotenuse is unknown
        if unknown == 'hypotenuse':
            return side_length / math.sin(angle)

        # calculates the length when adjacent is unknown
        elif unknown == 'adjacent':
            return side_length / math.tan(angle)

    # calculates the side length when the known side of the triangle is adjacent
    elif side_name == 'adjacent':

        # calculates the length when hypotenuse is unknown
        if unknown == 'hypotenuse':
            return side_length / math.cos(angle)
            
        # calculates the length when opposite is unknown
        elif unknown == 'opposite':
            return side_length * math.tan(angle)


# function which calculates angle if has two knwon sides
def trig_inverse(side_a, side_b, length_a, length_b):

    # finds ratio using opp and adj and uses that with inverse tan to find the angle
    # main side is opposite (then calculates angle based on the second chosen side with ratio)
    
    # when first side is opposite
    if side_a == 'opposite':

        # when the second side is adjacent
        if side_b == 'adjacent':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.atan(ratio)
            angle = math.degrees(angle)
            return angle

        # when the second side is hypotenuse
        elif side_b == 'hypotenuse':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle

    # main side is adjacent (then calculates angle based
    # on the second chosen side with ratio)
    elif side_a == 'adjacent':

        # when the second side is opposite
        if side_b == 'opposite':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle

        # when the second side is hypotenuse
        elif side_b == 'hypotenuse':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle


    # main side is hypotenuse (then calculates angle based on the second chosen side with ratio)
    elif side_a == 'hypotenuse':

        # when the second side is opposite
        if side_b == 'opposite':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle
        
        # when the second side is adjacent
        elif side_b == 'adjacent':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle


# Asks user for the known side (hyp, adj, opp)
def get_side(question):

    valid_sides = [
            ["hypotenuse", "hyp", "h"],
            ["opposite", "opp", "o"],
            ["adjacent", "adj", "a"]
        ]

    side_a = ""
    while side_a != "invalid input":
        side_a = input(question).lower()
        side_a_valid = string_check(side_a, valid_sides)

        if side_a_valid == "invalid input":
            print("Error, please try again\nValid options are -", ', '.join(Extract(valid_sides)), "\n")

        elif side_a_valid != "invalid input":
            return side_a_valid


# gets the user to type in the second side,
def second_side(question, known):

    valid_sides = [
        ["hypotenuse", "hyp", "h"],
        ["opposite", "opp", "o"],
        ["adjacent", "adj", "a"],
        ["unknown", "unk", "u"]
    ]

    unknown = ""
    while unknown != "invalid input":

        default = "unknown"

        unknown = input(question)
        unknown_valid = string_check(unknown, valid_sides)

        if unknown_valid == known:
            print("Cannot be same as Side A ({})".format(side_a))

        elif unknown_valid != "invalid input":
            return unknown_valid

        elif unknown == "":
            return default

        else:
            print("Error, please try again")


# *** main routine ***

# method -->
# 1) Ask for known values
side_a = get_side("Name of side A: ")
length_a = num_check("Length of {}: ".format(side_a), "Error, make sure your input is a number above 0\n", 0, float('inf'), float)

# Ask for side b
side_b = second_side("\nName of side B?\n-Keep blank if the length is unknown- ", side_a)



# if second side is unknown, ask user what side it is, so it can calculate it
if side_b == "unknown":
    
    print()

    # get angle value for the trig function to work out length of b
    angle_value = num_check("Angle: ", "Please enter a valid angle value", 0, float('inf'), float)

    # list that hold valid options for side b
    valid_side = [
            ["hypotenuse", "hyp", "h"],
            ["opposite", "opp", "o"],
            ["adjacent", "adj", "a"]
        ]

    # start of loop to get side b
    side_b = ""
    while side_b != "invalid input":

        print()

        # asks for side b in the loop
        side_b = input("(corresponding to your angle position)\nWhat is the unknown side: ").lower()
        side_b_unknown = string_check(side_b, valid_side)

        # makes sure side b is not same as side a
        if side_b_unknown == side_a:
            print("Cannot be the same as A ({})".format(side_a))

        # if side b is a valid option, return it
        elif side_b_unknown != "invalid input":
            print("Unknown side: {}".format(side_b_unknown))
            break

        # if side b input has invalid input, prints error
        else:
            print("Please enter")

    print()

    # get the length of side_b 
    length_b = trig_norm(angle_value, side_a, length_a, side_b_unknown)
    
    print()

    # prints the length of side b
    print("Length of unknown: {:.3f}".format(length_b))


# if length of side b is known, get the length of b and calculate the angle
else:

    # if Side A is hypotenuse, add maximum value to the length (cannot exceed length of side A)
    if side_a == "hypotenuse":
        length_b = num_check("Length of {}: ".format(side_b), "Make sure your input is a number between 0 and {}".format(length_a), 0, length_a, float)

    # if side A isn't hypotenuse, don't limit the maximum value
    else:
        length_b = num_check("Length of {}: ".format(side_b), "Error, make sure your input is a number above 0", 0, float('inf'), float)

    angle = trig_inverse(side_a, side_b, length_a, length_b)

    print("Value of desired angle: {:.3f}°".format(angle))

print()
print()

value_list = []
name_list = []
