# import libraries
import numpy as np
import math

# Python3 program explaining
# degrees() function

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Radian values : \n", in_array)

degree_Values = np.degrees(in_array)
print ("\nDegree values : \n", degree_Values)

print()

# Python3 program explaining
# rad2deg() function

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Radian values : \n", in_array)

out_Values = np.rad2deg(in_array)
print ("\nDegree values : \n", out_Values)
