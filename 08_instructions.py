# getting instructions
# version one


def Extract(lst):
    return [item[0] for item in lst]


# string checker (checks for valid input from a list)
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



yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

instructions_list = "\n***WELCOME***\nThis program helps the user work out values of a right angled triangle!\nYou will be asked to enter known information about the triangle in order for the program to calculate unknown values of triangles.\nAll the program needs is ->\n1) Side name [Hypotenuse, Adjacent, Opposite] (corresponding to the angle) and its length PLUS the known angle\n2) Two different sied names [Hypotenuse, Adjacent, Opposite] and their lengths (adjacent/opposite cannot be longer than hypotenuse)\n"

instructions = ""
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

print("Program continues...")
