summary_list = []

for item in range(0, 3):
    question = input("type question: ")
    answer =  input("type answer: ")
    comment = input ("type comment: ")

    summary_statement = "{} | {} | {}".format(question, answer, comment)
    summary_list.append(summary_statement)


print()
print("*** Summary ****")
for item in summary_list:
    print(item)