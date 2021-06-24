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
            chosen = var_list[0].title()
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
    if side_name == 'hyp':

        # calculates the length when opposite is unknown
        if unknown == 'opp':
            return side_length * math.sin(angle)

        # calculates the length when adjacent is unknown
        elif unknown == 'adj':
            return side_length * math.cos(angle)
    
    # calculates the side length when the known side of the triangle is opposite
    elif side_name == 'opp':

        # calculates the length when hypotenuse is unknown
        if unknown == 'hyp':
            return side_length / math.sin(angle)

        # calculates the length when adjacent is unknown
        elif unknown == 'adj':
            return side_length / math.tan(angle)

    # calculates the side length when the known side of the triangle is adjacent
    elif side_name == 'adj':

        # calculates the length when hypotenuse is unknown
        if unknown == 'hyp':
            return side_length / math.cos(angle)
            
        # calculates the length when opposite is unknown
        elif unknown == 'opp':
            return side_length * math.tan(angle)


# function which calculates angle if has two knwon sides
def trig_inverse(side_a, side_b, length_a, length_b):

    # finds ratio using opp and adj and uses that with inverse tan to find the angle
    # main side is opposite (then calculates angle based on the second chosen side with ratio)
    
    # when first side is opposite
    if side_a == 'opp':

        # when the second side is adjacent
        if side_b == 'adj':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.atan(ratio)
            angle = math.degrees(angle)
            return angle

        # when the second side is hypotenuse
        elif side_b == 'hyp':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle

    # main side is adjacent (then calculates angle based
    # on the second chosen side with ratio)
    elif side_a == 'adj':

        # when the second side is opposite
        if side_b == 'opp':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle

        # when the second side is hypotenuse
        elif side_b == 'hyp':
            # calculates the ratio based on the two known side lengths
            ratio = length_a/length_b
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle


    # main side is hypotenuse (then calculates angle based on the second chosen side with ratio)
    elif side_a == 'hyp':

        # when the second side is opposite
        if side_b == 'opp':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle
        
        # when the second side is adjacent
        elif side_b == 'adj':
            # calculates the ratio based on the two known side lengths
            ratio = length_b/length_a
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle


# Asks user for the known side (hyp, adj, opp)
def get_known():

    valid_sides = [
            ["hyp", "hypotenuse", "hyp", "h"],
            ["opp", "opposite", "opp", "o"],
            ["adj", "adjacent", "adj", "a"]
        ]

    side_a = ""
    while side_a != "invalid input":
        side_a = input("Side A: ")
        side_a_valid = string_check(side_a, valid_sides)

        if side_a_valid == "invalid input":
            print("Error, please try again")

        elif side_a_valid != "invalid input":
            return side_a_valid


# gets the user to type in the second side,
def second_side(known):
    valid_sides = [
        ["hyp", "hypotenuse", "hyp", "h"],
        ["opp", "opposite", "opp", "o"],
        ["adj", "adjacent", "adj", "a"],
        ["unknown", "unk", "u"]
    ]

    unknown = ""
    while unknown != "invalid choice":

        default = "unknown"

        unknown = input(" -Side B-\nIf unknown, keep blank\nB: ")
        unknown_valid = string_check(unknown, valid_sides)

        if unknown_valid == known:
            print("Please choose a different side")

        elif unknown_valid != "invalid input":
            return unknown_valid

        elif unknown_valid == "":
            return default

        else:
            print("Error, please try again")


# *** main routine ***

# method -->
# 1) Ask for known values
side_a = get_known()
length_a = num_check("Length A: ", "Error", 0, float('inf'), float)


side_b = second_side(side_a)

print("A: {} {}".format(side_a, length_a))
print("B: {}".format(side_b))

# if side_b == "Unknown":
