import pandas


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


# triangle_num = 'one', 'two', 'three', 'four'

hypotenuse = []
opposite = []
adjacent = []

sides_list = [hypotenuse, opposite, adjacent]

triangle_side_dict = {
    # 'Triangle': triangle_num,
    'Hypotenuse': hypotenuse,
    'Opposite': opposite,
    'Adjacent': adjacent,
}

test_data = [
    [['Hypotenuse', 4.76021], ['Opposite', 2.4186], ['Adjacent', 4.1]],
    [['Hypotenuse', 3.71137], ['Opposite', 3.14], ['Adjacent', 1.97855]],
    [['Hypotenuse', 14.15097], ['Opposite', 12], ['Adjacent', 7.5]],
    [['Hypotenuse', 10.19804], ['Opposite', 2], ['Adjacent', 10]]
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


triangle_frame = pandas.DataFrame(triangle_side_dict)

round_to = num_check("How many decimal places? ", "Please enter a number between 1 and 5\n", 0, 6, int)

triangle_frame = triangle_frame.round(round_to)

print(triangle_frame)
