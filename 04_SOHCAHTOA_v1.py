# sohcahtoa function for trigonometry
# https://stackoverflow.com/questions/46958547/finding-an-unknown-length-of-a-side-using-sohcahtoa-trigonometry

# importing libraries
import math


def trigonometry(angle, side_length, side_respective_to_angle, unknown):
    sohcahtoa = [
        ['opposite', 'hypotenuse', 'adjacent'],
        [None, math.sin, math.tan],
        [math.sin, None, math.cos],
        [math.tan, math.cos, None]
    ]

    index1 = sohcahtoa[0].index(side_respective_to_angle)
    index2 = sohcahtoa[0].index(unknown)
    function = sohcahtoa[index1 + 1][index2]
    return (side_length / function(math.radians(angle))
        if side_respective_to_angle == 'opposite' or (side_respective_to_angle == 'adjacent' and unknown == 'hypotenuse')
        else function(math.radians(angle) * side_length))

angle = 30
side_length = 8
side_respective_to_angle = 9
unknown = ""
answer = trigonometry(30, 2, 'hypotenuse', 'opposite')

print(answer)
