# work out angle length using inverse(ratio)

# https://stackoverflow.com/questions/46958547/finding-an-unknown-length-of-a-side-using-sohcahtoa-trigonometry


# checks for valid input from the user, keeps going until valid
def string_check(choice, options):

    for var_list in options:

        # if the unit is valid, return the first item
        if choice in var_list:

            # get the first item of sublist in deg_rad
            chosen = var_list[0]
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the unit is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


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


import math

# trig(angle=30, side=2, known='hyp', unknown='opp')
# This would want to find the length of a leg of a triangle
# that has a hypotenuse of 2, and an angle between the
# hypotenuse and another leg of 30 (degrees)
# https://stackoverflow.com/questions/46958547/finding-an-unknown-length-of-a-side-using-sohcahtoa-trigonometry

# sin(T) = opp / hyp
# cos(T) = adj / hyp
# tan(T) = opp / adj

def trig(angle, side, known, unknown):
    angle = math.radians(angle)
    # Unknown poss:
        # hyp
        # opp
        # adj
    
    if known == 'hyp':
        if unknown == 'opp':
            return side * math.sin(angle)
        elif unknown == 'adj':
            return side * math.cos(angle)

    elif known == 'opp':
        if unknown == 'hyp':
            return side / math.sin(angle)
        elif unknown == 'adj':
            return side / math.tan(angle)

    elif known == 'adj':
        if unknown == 'hyp':
            return side / math.cos(angle)
        elif unknown == 'opp':
            return side * math.tan(angle)



def inverse(side_a, side_b):
    