# ask user what they are trying to calculate (right angled triangle)

valid_calculations = [
    ["angle", "an"],
    ["short side", "ss"],
    ["hypotenuse", "h"],
    ["area", "ar"],
    ["perimeter", "p"]
]

calculation_ok = ""
calculation = ""

for item in range(0,3):

    # ask user for what they are trying to calculate
    what_to_calculate = input("What do you want to calculate? ".lower())

    for var_list in valid_calculations:

        # if the calculation is in list
        if what_to_calculate in var_list:

            # get full name of what is needed to be calculated
            calculation = var_list[0].title()
            calculation_ok = "yes"
            break

        # # if the chosen calculation is not valid ask again
        else:
            calculation_ok = "no"

    # print option again
    if calculation_ok == "yes":
        print("You want to calculate '{}'".format(calculation))

    else:
        print("Invalid choice")
