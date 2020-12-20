import re

# input = open('./input.txt')
input = open('./input_small.txt')
lines = input.read().split("\n\n")

rules = lines[0].split("\n")
rules = list(map(lambda s: s.strip(), rules))
messages = lines[1].split("\n")
messages = list(map(lambda s: s.strip(), messages))

rule_dict = {}
for rule in rules:
    rule_number = int(re.search('([0-9]*):', rule).group(1))
    rule_text = re.search(': (.*)$', rule).group(1)
    rule_dict[rule_number] = rule_text


def rule_zero_decomposition(rule_dictionary):
    char_list = []
    next_rule = rule_dictionary[0]
    finished = False
    while not finished:
        if ('"' in next_rule):
            print("xxx")
        elif('|' in next_rule):
            print("yyy")
    return char_list


def check_rule_zero_compliance(message, rule_dictionary):
    
    return True

print(rule_zero_decomposition(rule_dict))
# print(check_rule_zero_compliance("ababbb", rule_dict))
# print(check_rule_zero_compliance("bababa", rule_dict))
