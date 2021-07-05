# appending sides function
# appends input based on what it is


def append_input(side, length):
    
    if side == 'hypotenuse':
        hypotenuse.append(side)
        hypotenuse.append(length)

    elif side == 'opposite':
        opposite.append(side)
        opposite.append(length)

    elif side == 'adjacent':
        adjacent.append(side)
        adjacent.append(length)
    

hypotenuse = []
adjacent = []
opposite = []

for item in range(0, 3):

    side = input("Side: ")
    length = input("Length: ")

    append_input(side, length)

print(hypotenuse)
print(opposite)
print(adjacent)

all_sides = [hypotenuse, adjacent, opposite]

print(all_sides)
