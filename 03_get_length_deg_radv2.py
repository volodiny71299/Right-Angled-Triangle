# ask the user what units they want in their calculations

def Extract(lst):
    return [item[0] for item in lst]


# string checker
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
        length_unit = input("Choose your measuring unit or keep blank for the default option (units)\n").lower()

        # if user chooses to type in 'xxx' chooses 'units' as default measuring unit
        if length_unit == "":
            return length_auto

        # checks that the item is in valid_length list
        length_choice = string_check(length_unit, valid_length)

        # if the 
        if length_choice != "" and length_choice != "invalid choice":
            return length_choice

        # if not in list, prints an error to try again
        else:
            print("Please choose from -", ', '.join(Extract(valid_length)), "\n")


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


# getting length untis
# get_length_unit = valid_length()

# getting angle units
get_angle_unit = deg_rad()

# print out chosen results
# print("300 {}\n43 {}".format(get_length_unit, get_angle_unit))
print("You chose to use {}".format(get_angle_unit))
