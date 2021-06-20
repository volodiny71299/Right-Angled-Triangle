# fucntion that checks that the second input is not the same as the first input when the user is asked to enter the known and unknown side


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
        return "invalid choice"



def get_sides():
    
    valid_sides = [
            ["hyp", "hypotenuse", "hyp", "h"],
            ["opp", "opposite", "opp", "o"],
            ["adj", "adjacent", "adj", "a"]
        ]

    side_a = ""
    while side_a != "invalid input":
        
        side_a = input("Known side: ")
        side_a_valid = string_check(side_a, valid_sides)

        side_b = input("Unknown side: ")
        side_b_valid = string_check(side_b, valid_sides)

        if side_a_valid == side_b_valid:
            print("error, try again")

        elif side_a_valid != "invalid input":
            return side_a_valid

sides = get_sides()
print(sides)
