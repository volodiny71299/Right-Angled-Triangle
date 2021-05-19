# number checkers (checks number is valid)
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


get_value = num_check("Length of side A in cm - ", "Please enter a number greater than 0", float)

print("Side A: {:.2f}cm".format(get_value))
