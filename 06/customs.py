

input = open('./input.txt')
read_file = input.read()
group_answers = read_file.split("\n\n")  # Each entry in the set of answer(s) from one group

for index, value in enumerate(group_answers):
    individual_answers = value.split("\n")  # Each entry is the answer set for an individual in that group
    group_answers[index] = individual_answers

sum_of_any_yes_per_group = 0
for i in group_answers:
    group_answers_concatenated = ''.join(i)
    unique_group_answers = set(group_answers_concatenated)
    sum_of_any_yes_per_group += len(unique_group_answers)

print("Part 1 - Sum of 'yes' answers at a group level: ", sum_of_any_yes_per_group)

sum_of_all_yes_per_group = 0
for i in group_answers:
    if (len(i) == 1):
        sum_of_all_yes_per_group += len(i[0])
    else:
        groups_unanimous_letters = 0
        for letter in i[0]:
            # Check if each letter of the first person's answers are in ALL other groupmember's answers
            if(all(letter in answers for answers in i)):
                groups_unanimous_letters += 1
        sum_of_all_yes_per_group += groups_unanimous_letters

print("Part 2 - Sum of UNANIMOUS 'yes' answers at a group level: ", sum_of_all_yes_per_group)