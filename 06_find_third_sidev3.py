# find the length of the thrid side based on two knowns
import math


# calculator for the third side of the triangle
def third_calc(side_a, length_a, side_b, length_b):
    
    # Side A is hypotenuse
    if side_a == "hypotenuse":

        # second side is opposite, calculates third side
        if side_b == "opposite":
            side_c = "adjacent"
            side_c_length = math.sqrt(length_a**2 - length_b**2)
            return [side_c, side_c_length]

        # second side is adjacent, calculates third side
        elif side_b == "adjacent":
            side_c = "opposite"
            side_c_length = math.sqrt(length_a**2 - length_b**2)
            return [side_c, side_c_length]

    # side A is opposite
    elif side_a == "opposite":
        
        # second side is hypotenuse, calculates third side
        if side_b == "hypotenuse":
            side_c = "adjacent"
            side_c_length = math.sqrt(length_b**2 - length_a**2)
            return [side_c, side_c_length]

        # second side is adjacent, calculates third side
        elif side_b == "adjacent":
            side_c = "hypotenuse"
            side_c_length = math.sqrt(length_a**2 + length_b**2)
            return [side_c, side_c_length]

    # side A is adjacent
    elif side_a == "adjacent":
        
        # second side is hypotenuse, calculates third side
        if side_b == "hypotenuse":
            side_c = "opposite"
            side_c_length = math.sqrt(length_b**2 - length_a**2)
            return [side_c, side_c_length]

        # second side is opposite, calculates third side
        elif side_b == "opposite":
            side_c = "hypotenuse"
            side_c_length = math.sqrt(length_a**2 + length_b**2)
            return side_c and side_c_length

# test data for faster testing
options = [
    ["hypotenuse", 5, "adjacent", 4],
    ["hypotenuse", 5, "opposite", 3],
    ["opposite", 3, "adjacent", 4]
]

for item in options:
    side_a = item[0]
    length_a = item[1]
    side_b = item[2]
    length_b = item[3]

    side_c_length = third_calc(side_a, length_a, side_b, length_b)

    print()
    print("INPUT: ", item, "\nANSWER:", side_c_length)
    print()
