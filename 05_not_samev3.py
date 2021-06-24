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


# Asks user for the known side (hyp, adj, opp)
def get_known():

    valid_sides = [
            ["hyp", "hypotenuse", "hyp", "h"],
            ["opp", "opposite", "opp", "o"],
            ["adj", "adjacent", "adj", "a"]
        ]

    side_a = ""
    while side_a != "invalid choice":
        side_a = input("Side A: ")
        side_a_valid = string_check(side_a, valid_sides)

        if side_a_valid == "invalid choice":
            print("Error, please try again")

        elif side_a_valid != "invalid choice":
            return side_a_valid


# Function which asks the user what the unknown side is (doesn't let the known side be repeated)
def second_side(known):
    
    valid_sides = [
            ["hyp", "hypotenuse", "hyp", "h"],
            ["opp", "opposite", "opp", "o"],
            ["adj", "adjacent", "adj", "a"],
            ["unknown", "unk", "u"]
        ]

    unknown = ""
    while unknown != "invalid choice":
        unknown = input("Side B: ")
        unknown_valid = string_check(unknown, valid_sides)

        if unknown_valid == known:
            print("Please choose a different side")

        elif unknown_valid != "invalid choice":
            return unknown_valid

        else:
            print("Error, please try again")

side_a = get_known()

side_b = second_side(side_a)

print("Side A:", side_a)
print("Side B:", side_b)

if side_b == "Unknown":
    angle = int(input("Angle: "))

else:
    print("Inverse working out...")
