import pandas

name_lengths = 'one', 'two', 'three', 'four'

hypotenuse = []
opposite = []
adjacent = []

sides_list = [hypotenuse, opposite, adjacent]

triangle_side_dict = {
    'Triangle': name_lengths,
    'Hypotenuse': hypotenuse,
    'Opposite': opposite,
    'Adjacent': adjacent,
}

test_data = [
    [['Hypotenuse', 5], ['Opposite', 3], ['Adjacent', 4]],
    [['Hypotenuse', 10], ['Opposite', 6], ['Adjacent', 8]],
    [['Hypotenuse', 50], ['Opposite', 30], ['Adjacent', 40]],
    [['Hypotenuse', 2.5], ['Opposite', 1.5], ['Adjacent', 2]]
]

count = 0

for all_sides in test_data:

    for item in sides_list:
        item.append(0)

    known_sides = test_data[count]
    count += 1

    for item in known_sides:
        if len(item) > 0:
            to_find = (item[0])
            amount = (item[1])
            add_list = triangle_side_dict[to_find]
            add_list[-1] = amount

print()
print("Side lengths: ", sides_list)
print("Hypotenuse lengths: ", sides_list[0])
print("Opposite lengths: ", sides_list[1])
print("Adjacent lengths: ", sides_list[2])
print()

traingle_frame = pandas.DataFrame(triangle_side_dict)
traingle_frame = traingle_frame.set_index('Triangle')
print(traingle_frame)
