

# original code from - https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
# element of each sublist in a list of lists
def Extract(lst):
    return [item[0] for item in lst]


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
    ["angle", "an", "ang"],
    ["hypotenuse", "h"],
    ["the opposite side", "opposite", "o"],
    ["the adjacent side", "adjacent", "ad"],
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

    # print error message and separate first item of sublist and put it into error message
    else:
        # code to separate messages -
        # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
        print("Error, please try again\n"
              "Valid options are -", ', '.join(Extract(valid_calculation)), "\n")
