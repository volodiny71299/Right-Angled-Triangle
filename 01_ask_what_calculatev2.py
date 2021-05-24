

# function goes here
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
        return "invalid choice"


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

    if calculation == "xxx":
        break

    calculation_choice = string_check(calculation, valid_calculation)

    if calculation_choice != "xxx" and calculation_choice != "invalid choice":
<<<<<<< Updated upstream
        # check calculation option is valid
        print("You want to calculate '{}'".format(calculation_choice))
        print()
=======
        print("Calculation: {}".format(calculation_choice))

    else:
        pass
>>>>>>> Stashed changes

    else:
        print("Error, please try again")
