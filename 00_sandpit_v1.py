# list containing all questions (aka test data)
summary_list = []

hypotenuse = []
opposite = []
adjacent = []
sides_list = [hypotenuse, opposite, adjacent]

# loop (for each problem...)
for item in range(0, 3):

    row = []

    temp_hyp = ['Hypotenuse']
    temp_opp = ['Opposite']
    temp_adj = ['Adjacent']

    which_side = input("Which side? ")

    if which_side == "hyp":
        hyp = input("Hypotenuse: ")
        
    elif which_side == "opp":
        opp = input("Opposite: ")
        temp_opp.append(opp)
    else:
        adj = input("Adjacent: ")
        temp_opp.append(opp)


    row = [temp_hyp, temp_opp, temp_adj]

    summary_list.append(row)


print()
print(summary_list)