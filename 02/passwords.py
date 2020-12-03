import re

# Part 1
# Input is a list of strings which represent password policies, and passwords that SHOULD follow them
# Format example: 1-3 a: abcde
# Means the letter A must be used 1-3 times in the password. The example PW is compliant here.
# Need to find quantity of passwords that ARE valid in the list.


def parse_policy_and_password(line):
    minimum_occurences = int(re.match(r"^[^-]*", line).group())
    maximum_occurences = int(re.search(r".*?-(.*?) .*", line).group(1))
    required_letter = re.search(r".*? (.*?):.*", line).group(1)
    password = re.search(r"[^ ]+$", line).group()
    return required_letter, minimum_occurences, maximum_occurences, password


input = open('./input.txt')
lines = input.readlines()
correct_password_count = 0
for i in lines:
    required_letter, minimum_occurences, maximum_occurences, password = parse_policy_and_password(i)
    if (password.count(required_letter) >= minimum_occurences and password.count(required_letter) <= maximum_occurences):
        correct_password_count += 1
print("Part 1 - Total number of valid passwords: ", correct_password_count)

correct_password_count = 0
for i in lines:
    required_letter, index_1, index_2, password = parse_policy_and_password(i)
    if(bool(password[index_1-1] == required_letter) ^ bool(password[index_2-1] == required_letter)):
        correct_password_count += 1
print("Part 2 - Total number of valid passwords: ", correct_password_count)


