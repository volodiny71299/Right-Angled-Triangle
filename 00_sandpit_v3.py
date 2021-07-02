# making lists
# *** testing ***

hypotenuse = []
opposite = []
adjacent = []

sides_list = [hypotenuse, opposite, adjacent]

side_dict = {
    'Hypotenuse': hypotenuse,
    'Opposite': opposite,
    'Adjacent': adjacent
}

test_data = [
    [['Hypotenuse', 5], ['Opposite', 3], ['Adjacent', 4]]
]


count = 0

for side_information in test_data:
    for item in sides_list:
        item.append(0)

    side_known = test_data[count]
    count += 1

    for item in side_known:
        if len(item) > 0:
            to_find = (item[0])
            amount = (item[1])
            add_list = side_dict[to_find]
            add_list[-1] = amount

print(sides_list)
