# Part 1
# Input is a txt file of lots of individual numbers
# Two of them add to 2020
# We need to find those two numbers, then multiply them. The product will be this puzzle's answer

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

# Part 2
# Input is a txt file of lots of individual numbers
# Three of them add to 2020
# We need to find those three numbers, then multiply them. The product will be this puzzle's answer
def find_summed_triplet(sum_number, input):
    summed_triplet = [0, 0, 0]
    for i, number in enumerate(input):
        if (number > sum_number):
            continue
        complementary_number = sum_number - number
        remaining_pair = find_summed_pair(complementary_number, input)
        if (remaining_pair != 0):
            summed_triplet = [remaining_pair[0], remaining_pair[1], number]
            return summed_triplet



input = open('./input.txt')
lines = list(map(int, input.readlines())) 

answer_pair = find_summed_pair(2020, lines)
print("Part 1 Answer Pair: ", answer_pair)
print("Part 1 Answer Key: ", answer_pair[0] * answer_pair[1])

# NOTE: find_summed_triplet currently does not check for using the same number multiple times.
#       So it could return [100, 100, 1820] where the first two values are the SAME 100
answer_triplet = find_summed_triplet(2020, lines)
print("Part 2 Answer Triplet: ", answer_triplet)
print("Part 2 Answer Key: ", answer_triplet[0] * answer_triplet[1] * answer_triplet[2])