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


# function which calculates angle if has two knwon sides
def inverse(side_a, side_b, length_a, length_b):

    # finds ratio using opp and adj and uses that with inverse tan to find the angle
    if side_a == 'opp':
        if side_b == 'adj':
            ratio = length_a/length_b
            angle = math.atan(ratio)
            angle = math.degrees(angle)
            return angle

        elif  side_b == 'hyp':
            ratio = length_a/length_b
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle


    elif side_a == 'adj':
        if side_b == 'opp':
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle

        elif side_b == 'hyp':
            ratio = length_a/length_b
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle

    
    elif side_a == 'hyp':
        if side_b == 'opp':
            ratio = length_b/length_a
            angle = math.asin(ratio)
            angle = math.degrees(angle)
            return angle
        
        elif side_b == 'adj':
            ratio = length_b/length_a
            angle = math.acos(ratio)
            angle = math.degrees(angle)
            return angle


side_a = input("Side A: ")
length_a = int(input("Length of A: "))

side_b = input("Side B: ")
length_b = int(input("Length of B: "))


answer = inverse(side_a, side_b, length_a, length_b)
print(answer)
