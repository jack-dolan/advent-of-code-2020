
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

def get_all_valid_arrangements(available_adapter_list, starting_output_joltage, goal_input_joltage):
    sum_of_valid_arrangements = 0
    for adapter in available_adapter_list:
        if (adapter > starting_output_joltage + 3 or adapter < starting_output_joltage):
            # print("Dead end - ", starting_output_joltage, " -> ", adapter, " doesn't work.")
            sum_of_valid_arrangements += 0
        else:
            if(adapter + 3 >= goal_input_joltage):
                sum_of_valid_arrangements += 1
                # print("Success - ", starting_output_joltage, " -> ", adapter, " works!")
            list_less_adapter = available_adapter_list[:]
            list_less_adapter.remove(adapter)
            if (len(list_less_adapter) > 0):
                sum_of_valid_arrangements += get_all_valid_arrangements(list_less_adapter, adapter, goal_input_joltage)
    return sum_of_valid_arrangements



input = open('./input.txt')  # Solution!
# input = open('./input_sample.txt')  # 8
# input = open('./input_sample_small.txt')  # 4
# input = open('./input_sample_large.txt')  # 19208
lines = input.readlines()
lines_ints = list(map(int, lines))
lines_ints.sort()

device_adapter_rating = lines_ints[-1] + 3

part1_counts = joltage_difference_counts(lines_ints)
print("Part 1 - The joltage difference product is: ", part1_counts[1] * part1_counts[3])
print("Part 2 - The total # of valid arrangements is: ", get_all_valid_arrangements(lines_ints, 0, device_adapter_rating))