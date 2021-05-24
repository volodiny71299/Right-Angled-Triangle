# https://kodify.net/python/math/round-decimals/
# rounding down numbers for number checker reference
# https://kodify.net/python/math/round-decimals/

import math


def round_decimals_down(number:float, decimals:int=2):

    # Returns a value rounded down to a specific number of decimal places.

    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


# Some numbers to round
valueA = 3.14159265359
valueB = 1845.7409947
valueC = -100.95
valueD = 9.5432
valueE = 34.49953

# Round values to a certain number of decimal places
roundA = round_decimals_down(valueA, 5)
roundB = round_decimals_down(valueB, 4)
roundC = round_decimals_down(valueC, 3)
roundD = round_decimals_down(valueD, 2)
roundE = round_decimals_down(valueE, 1)

# Display the results
print("Value:".ljust(15), "Rounded:")

print(str(valueA).ljust(15), roundA)
print(str(valueB).ljust(15), roundB)
print(str(valueC).ljust(15), roundC)
print(str(valueD).ljust(15), roundD)
print(str(valueE).ljust(15), roundE)
