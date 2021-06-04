# Python code to demonstrate the working of cos()
	
# importing "math" for mathematical operations
import math
	
a = math.pi / 6
	
# returning the value of cosine of pi / 6
print ("The value of cosine of pi / 6 is : ", end ="")
print (math.cos(a))

# Python program showing
# Graphical representation of
# cos() function
import math
import numpy as np
# import matplotlib.pyplot as plt

in_array = np.linspace(-(2 * np.pi), 2 * np.pi, 20)

out_array = []

for i in range(len(in_array)):
	out_array.append(math.cos(in_array[i]))
	i += 1


print("in_array : ", in_array)
print("\nout_array : ", out_array)

# red for numpy.sin()
# plt.plot(in_array, out_array, color = 'red', marker = "o")
# plt.title("math.cos()")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
