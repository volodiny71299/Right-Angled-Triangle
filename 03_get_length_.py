# ask the user what units they want in their calculations


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
        length_unit = input("Choose your measuring unit or type 'xxx' to keep it default (units)\n").lower()

        # if user chooses to type in 'xxx' chooses 'units' as default measuring unit
        if length_unit == "xxx":
            return length_auto

        # checks that the item is in valid_length list
        length_choice = string_check(length_unit, valid_length)

        # if the 
        if length_choice != "xxx" and length_choice != "invalid choice":
            return length_choice

        # if not in list, prints an error to try again
        else:
            print("Error, please try again\n")

# getting mesuring untis
get_units = valid_length()

# prints out the unit that the user chose
print("You chose to use {} for your measurements".format(get_units))
