input = open('./input.txt')  # Solution!
# input = open('./input_sample.txt')  # 8
# input = open('./input_sample_small.txt')  # 4
# input = open('./input_sample_large.txt')  # 19208

lines = input.readlines()
lines_ints = list(map(int, lines))
lines_ints.sort()

device_adapter_rating = lines_ints[-1] + 3

all_available_adapters = lines_ints.copy()
all_available_adapters.append(0)  # Add an "adapter" for the zero-rating outlet
all_available_adapters.append(device_adapter_rating)# Add an "adapter" for the device (largest adapter plus 3)
all_available_adapters.sort()

def joltage_difference_counts(ordered_output_list):
    difference_counts = {
        1: 0,
        2: 0,
        3: 0
    }
    for i_index, i_value in enumerate(ordered_output_list):
        if (i_index == len(ordered_output_list) - 1):
            difference_counts[3] += 1
        elif (i_index == 0):
            joltage_difference = ordered_output_list[i_index + 1] - i_value
            difference_counts[joltage_difference] += 1
            difference_counts[i_value] += 1  # Also account for the difference from ZERO (charging outlet) if first value
        else:
            joltage_difference = ordered_output_list[i_index + 1] - i_value
            difference_counts[joltage_difference] += 1
    return(difference_counts)

def caching(func):
    tried = {}
    def helper(x):
        if x not in tried:
            tried[x] = func(x)
        return tried[x]
    return helper

@caching  # TURN BACK ON
def get_all_valid_arrangements(goal_joltage):
    sum_of_valid_arrangements = 0

    if (goal_joltage == 0):  # Means that you've worked all the way down to the outlet's voltage. VALID ARRANGEMENT
        sum_of_valid_arrangements = 1
        return sum_of_valid_arrangements
    
    # For each VALID adapter in all_available_adapters (step down from goal_joltage by 1, 2, or 3)
    for adapter in list(x for x in list(goal_joltage - y for y in range(1,4)) if x in all_available_adapters):
        sum_of_valid_arrangements += get_all_valid_arrangements(adapter)

    return sum_of_valid_arrangements


part1_counts = joltage_difference_counts(lines_ints)
print("Part 1 - The joltage difference product is: ", part1_counts[1] * part1_counts[3])
print("Part 2 - The total # of valid arrangements is: ", get_all_valid_arrangements(device_adapter_rating))
