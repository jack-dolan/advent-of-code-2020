
def find_summed_pair(sum_number, input):
    summed_pair = [0, 0]
    for i, number in enumerate(input):
        if (number > sum_number):
            continue
        complementary_number = sum_number - number
        if complementary_number in input[i+1:]:  # Only need to check beyond the index you're at. 
                                                 # Reduces wasted cycles AND elimnates summing of the same number
            summed_pair = [number, complementary_number]
            return summed_pair
    else:
        return 0  # Return a single zero if no pair is found (only relevant for use in find_summed_triplet)

def find_contiguous_summed_set(sum_number, full_set):
    summed_set = []
    for i_index, i_value in enumerate(full_set):
        overflow = False
        success = False
        lookahead = 2
        while (overflow == False and success == False):
            summed_set = full_set[i_index:(i_index+lookahead)]
            sumof_summed_set = sum(summed_set)
            if (sumof_summed_set == sum_number):
                success = True
            elif (sumof_summed_set > sum_number):
                overflow = True
            else:
                lookahead += 1
        if (success):
            break
    return summed_set


def check_xmas1_validity(focused_number, preceding_numbers):
    xmas_valid = False
    summed_pair = find_summed_pair(focused_number, preceding_numbers)
    if (summed_pair != 0):  # Zero means summed pair wasn't found
        if (summed_pair[0] != summed_pair[1]):  # XMAS encoding doesn't allow both numbers to be the same
            xmas_valid = True
    return xmas_valid

input = open('./input.txt')
lines = input.readlines()

preamble_length = 25
number_of_relevant_numbers = len(lines) - preamble_length

invalid_number = 0
for i in range(preamble_length, len(lines)):  # For each of the relevant numbers (ie starting at lines[25], if preamble is 25)
    preceding_group = list(map(int, lines[i-preamble_length:i]))
    number_validity = check_xmas1_validity(int(lines[i]), preceding_group)
    if (not number_validity):
        invalid_number = int(lines[i])
        print("Part 1 - The first number in the sequence that doesn't follow XMAS encoding is: ", invalid_number)
        break

lines_ints = list(map(int, lines))
contiguous_summed_set = find_contiguous_summed_set(invalid_number, lines_ints)
print("Part 2 - The encryption weakness is: ", min(contiguous_summed_set) + max(contiguous_summed_set))