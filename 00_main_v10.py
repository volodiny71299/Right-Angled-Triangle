# main code v6
# Put the whole code in a loop until exit code is given
# Sources for codes ->
# Extract function - https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
# List with no brackets (print) - https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# trigonometry - # https://stackoverflow.com/questions/46958547/finding-an-unknown-length-of-a-side-using-sohcahtoa-trigonometry

# import libraries
import math
import pandas

# np.random.seed(25)

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
            angle = math.atan(ratio)
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
            ["hypotenuse", "hyp", "h", "c"],
            ["opposite", "opp", "o", "b"],
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
        ["adjacent", "adj", "a"]
    ]

    unknown = ""
    while unknown != "invalid input":

        default = "unknown"

        unknown = input(question)
        unknown_valid = string_check(unknown, valid_sides)

        if unknown_valid == known:
            print("Cannot be same as the first side({})".format(side_a))

        elif unknown_valid != "invalid input":
            return unknown_valid

        else:
            print("Error, please try again")


# calculator for the third side of the triangle
def third_calc(side_a, length_a, side_b, length_b):
    
    # Side A is hypotenuse
    if side_a == "hypotenuse":

        # second side is opposite, calculates third side
        if side_b == "opposite":
            side_c = "adjacent"
            side_c_length = math.sqrt(length_a**2 - length_b**2)
            return [side_c, side_c_length]

        # second side is adjacent, calculates third side
        elif side_b == "adjacent":
            side_c = "opposite"
            side_c_length = math.sqrt(length_a**2 - length_b**2)
            return [side_c, side_c_length]

    # side A is opposite
    elif side_a == "opposite":
        
        # second side is hypotenuse, calculates third side
        if side_b == "hypotenuse":
            side_c = "adjacent"
            side_c_length = math.sqrt(length_b**2 - length_a**2)
            return [side_c, side_c_length]

        # second side is adjacent, calculates third side
        elif side_b == "adjacent":
            side_c = "hypotenuse"
            side_c_length = math.sqrt(length_a**2 + length_b**2)
            return [side_c, side_c_length]

    # side A is adjacent
    elif side_a == "adjacent":
        
        # second side is hypotenuse, calculates third side
        if side_b == "hypotenuse":
            side_c = "opposite"
            side_c_length = math.sqrt(length_b**2 - length_a**2)
            return [side_c, side_c_length]

        # second side is opposite, calculates third side
        elif side_b == "opposite":
            side_c = "hypotenuse"
            side_c_length = math.sqrt(length_a**2 + length_b**2)
            return [side_c, side_c_length]


# appends side name+length to a list
def append_input(side, length):
    
    if side == 'hypotenuse':
        hypotenuse.append(length)

    elif side == 'opposite':
        opposite.append(length)

    else:
        adjacent.append(length)


# *** Dictionaries and lists ***

# triangle_num = 'one', 'two', 'three', 'four'

# set up dictionary for the three sides
hypotenuse = []
opposite = []
adjacent = []

# dictionaries for the two angles
angle_one = []
angle_opposite = []

# triangle sides dictionary
triangle_side_dict = {
    'hypotenuse': hypotenuse,
    'opposite': opposite,
    'adjacent': adjacent,
}

# triangle angle dictionary
triangle_angle_dict = {
    'angle': angle_one,
    'opposite angle': angle_opposite
}

# *** main routine ***

# getting instructions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

instructions_list = ""

instructions = "*** WELCOME ***\n" \
               "This program helps the user work out values of a right angled triangle!\n" \
               "You will be asked to enter information about the triangle in order for the program to calculate values of the triangle.\n" \
               "1) Enter a known side value\n" \
               "2) Enter the length of that known value\n" \
               "3) You will be asked if you know the second side value\n" \
               "\t- If yes, you will be asked to enter the name and the value of the side\n" \
               "\t- If no, you will be asked to enter an angle value (between 0 and 90)\n" \
               "4) You will be asked to loop the program or print the results\n" \
               "Good luck!\n"

while instructions != "invalid input":

    instructions = input("Do you want to see the instructions? [Yes/No] ").lower()

    print_instructions = string_check(instructions, yes_no)
    if print_instructions == "yes":
        print(instructions_list)
        break

    elif print_instructions == "no":
        print("You chose to not print instructions :)\n")
        break

    else:
        print("Error, please try again\nValid options are -", ', '.join(Extract(yes_no)), "\n")


carry_on = ""
while carry_on == "":

    print("-Right angled triangle diagram (not to scale)-")
    print("  A")
    print("  |\ ")
    print("  | \ ")
    print("  |  \ ")
    print("b |   \ c")
    print("  |    \ ")
    print("  |     \ ")
    print("  |______\ ")
    print(" C   a    B")

    # Ask for known values of for the first side
    side_a = get_side("Known side (hypotenuse, opposite, adjacent): ")

    # get length of the first known side
    length_a = num_check("Length of {}: ".format(side_a), "Error, make sure your input is a number above 0\n", 0, float('inf'), float)

    # appending the first side + length
    append_input(side_a, length_a)

    # ask user if they know the second side
    know_side_b = input("Is another side known? [Yes/No] ")
    know_side_b = string_check(know_side_b, yes_no)

    # if second side is unknown, ask user what side it is, so it can calculate it
    if know_side_b == "no":
        
        print()

        # get angle value for the trig function to work out length of b
        angle_value = num_check("Angle value: ", "Please enter a valid angle value", 0, float('inf'), float)

        angle_value_two = 90 - angle_value

        angle_one.append(angle_value)
        angle_opposite.append(angle_value_two)

        # Hard coded side names for easier calculations based on the first chosen side by the user
        if side_a == "hypotenuse":
            side_b = "opposite"

        elif side_a == "opposite":
            side_b = "adjacent"

        elif side_a == "adjacent":
            side_b = "hypotenuse"

        # get the length of side_b
        length_b = trig_norm(angle_value, side_a, length_a, side_b)

        # append input of Side+Length B
        append_input(side_b, length_b)

        # Calculate name and length of side C
        third_side = third_calc(side_a, length_a, side_b, length_b)
        side_c = third_side[0]
        length_c = third_side[1]

        # append the length of side c to the wanted list
        append_input(side_c, length_c)
        
        carry_on = input("\nPress <ENTER> to continue or anything else to print the results\n")

    # if length of side b is known, get the length of b and calculate the angle
    else:

        # Ask for the second side
        side_b = second_side("Name of second side (hypotenuse, opposite, adjacent): ", side_a)

        # if Side A is hypotenuse, add maximum value to the length (cannot exceed length of side A)
        if side_a == "hypotenuse":
            length_b = num_check("Length of {}: ".format(side_b), "Make sure your input is a number between 0 and {}".format(length_a), 0, length_a, float)

        if side_b == "hypotenuse":
            length_b = num_check("Length of {}: ".format(side_b), "{} cannot be shorter than {} ({})".format(side_b, side_a, length_a), length_a, float('inf'), float)

        # if side A isn't hypotenuse, don't limit the maximum value
        else:
            length_b = num_check("Length of {}: ".format(side_b), "Error, make sure your input is a number above 0", 0, float('inf'), float)

        angle_value = trig_inverse(side_a, side_b, length_a, length_b)
        
        angle_value_two = 90 - angle_value

        angle_one.append(angle_value)
        angle_opposite.append(angle_value_two)

        # append side b name and length
        append_input(side_b, length_b)

        # calculate the name and length of side C
        third_side = third_calc(side_a, length_a, side_b, length_b)
        side_c = third_side[0]
        length_c = third_side[1]

        # append the length of C to the wanted list
        append_input(side_c, length_c)

        carry_on = input("\nPress <ENTER> to use the calculator again\nOR anything else to print the results\n")

print()
triangle_side_frame = pandas.DataFrame(triangle_side_dict)
triangle_angle_frame = pandas.DataFrame(triangle_angle_dict)

round_to = num_check("How many decimal places? ", "Please enter a number between 0 and 5\n", -1, 6, int)

# rounding the whole data frame to users choice
triangle_side_frame = triangle_side_frame.round(round_to)
triangle_angle_frame = triangle_angle_frame.round(round_to)


print()
print("\t*** Triangle Lengths ***")
print(triangle_side_frame)

print()

print("\t*** Triangle Angles (degrees) ***")
print(triangle_angle_frame)
print()
