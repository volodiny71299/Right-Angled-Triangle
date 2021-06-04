# number checker v5
# Gets values for each length
# check for valid numbers in a certain range of values
# allow float

# importing libraries
import numpy


def Extract(lst):
    return [item[0] for item in lst]

# string check for allowed items
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
        return "invalid choice"


# checks numbers
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

def get_values():
        
    available_sides = [
        ["the opposite side", "opposite", "o"],
        ["the adjacent side", "adjacent", "a"],
        ["hypotenuse", "h"]
        ]
    
    # gets one angle
    get_angle = num_check("What is the value of the angle ", "Please enter a valid number\nGreater than 1 or less than 89\n", 1, 89, float)

    what_value = ""
    while what_value != "invalid choice":

        # get the length of a side (used the float('inf') to represent an infinite integer, doesn't have a max restriction)
        what_value = input("What is a known length - hypotenyse, opposite/adjacent to the angle ").lower()
        
        choice_value = string_check(what_value, available_sides)
        
        if choice_value != "invalid choice":
            get_length = num_check("What is the length of {} ".format(choice_value), "Enter a value greater than 0\n", 0, float('inf'), float)

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

                # checks that the input for what is needed to be calculated is correct
                calculation_choice = string_check(calculation, valid_calculation)

                if calculation_choice == choice_value:
                    print("You already know this side")

                # if the input is correct return a message saying what you chose
                if calculation_choice != choice_value and calculation_choice != "invalid choice":
                    # check calculation option is valid
                    print("You want to calculate '{}'".format(calculation_choice))
                    print()
                    continue

                # print error message and separate first item of sublist and put it into error message
                else:
                    # code to separate messages -
                    # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
                    print("Please try again\n"
                        "Valid options are -", ', '.join(Extract(valid_calculation)), "\n")

            

            # returns the input in this function
            return get_angle, choice_value, get_length

        else:
            print("Error, please try again\n")


values = get_values()
print(values)
