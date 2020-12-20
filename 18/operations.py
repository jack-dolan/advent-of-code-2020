import re

input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()
lines = list(map(lambda s: s.strip(), lines))

def solve_paren_less_expression(expression):
    result = int(expression[0])
    operation = ""
    for i in expression[1:]:
        if (i == "+"):
            operation = "+"
        elif (i == "*"):
            operation = "*"
        else:
            if (operation == "+"):
                result += int(i)
            else:
                result *= int(i)
    return result

def perform_all_addition(expression):
    if ("+" not in expression):
        return expression
    else:
        plus_index_list = []
        for i_index, i_value in enumerate(expression):
            if (i_value == "+"):
                plus_index_list.append(i_index)
        result_list = expression
        for plus_index in reversed(plus_index_list):
            replacement_sum = int(result_list[plus_index-1]) + int(result_list[plus_index+1])
            result_list = result_list[:plus_index-1] + [str(replacement_sum)] + result_list[plus_index+2:]
        return result_list

def decompose(expression, mode):  # Returns the expression, with the pieces in parentheses solved, in list format
    if ("(" not in expression and ")" not in expression):
        if (mode == 1):
            return(solve_paren_less_expression(expression.split(" ")))
        elif (mode == 2):
            # first compute all additions separately, then evaluate the whole thing once it's all multiplcation
            multiplication_only_expression = perform_all_addition(expression.split(" "))
            return(solve_paren_less_expression(multiplication_only_expression))
    else:
        this_level_pairs = []  # Will contain index pairs of all the this-level paren pieces.
        open_paren_index = 0
        closed_tracker = 0
        for i_index, i_value in enumerate(expression):
            if (i_value == "("):
                if (closed_tracker == 0):  # You encounter an openParen, and it's a new this-level container
                    closed_tracker = 1
                    open_paren_index = i_index
                else:  # You encounter an openParen, but it's within a this-level container that you're already tracking
                    closed_tracker += 1
            elif (i_value == ")"):
                closed_tracker -= 1
                if (closed_tracker == 0):  # You encounter a closeParen, and it closes the currently tracked this-level container
                    this_level_pairs.append([open_paren_index, i_index])
                    
        new_expression = expression
        for index_pair in reversed(this_level_pairs):
            replacement_content = decompose(expression[index_pair[0]+1:index_pair[1]], mode)
            new_expression = new_expression[:index_pair[0]] + str(replacement_content) + new_expression[index_pair[1]+1:]
        return decompose(new_expression, mode)

part_1_sum = 0
for i in lines:
    part_1_sum += decompose(i, 1)

print("Part 1 - Sum of all decomposed expressions: ", part_1_sum)

part_2_sum = 0
for i in lines:
    part_2_sum += decompose(i, 2)
    # print(decompose(i, 2))

print("Part 2 - Sum of all decomposed expressions: ", part_2_sum)