import math


# rounding up and down, one function

def round_up_down(number:float, decimals:int=2):

    if number < 0.001:
        return math.floor(number)

    elif number > 89.999:
        return math.ceil(number)
    
    factor = 10 ** decimals
    return math.floor(number * factor) / factor


# number checker with high and low and custom error message
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


get_value = num_check("Number: ", "Please enter a valid number\n", 0, 90, float)
print()

print("= {}".format(get_value))
print()
get_value = round_up_down(get_value, 3)

print("= {}".format(get_value))
print()
