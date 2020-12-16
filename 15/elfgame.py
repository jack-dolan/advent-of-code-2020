input = open('./input.txt')
lines = input.read()

starting_numbers = lines.split(",")
starting_numbers = list(map(lambda s: int(s), starting_numbers))

def get_next_spoken_number(list_of_spoken_numbers):
    most_recently_spoken_number = list_of_spoken_numbers[-1]
    if (list_of_spoken_numbers.count(most_recently_spoken_number) == 1):
        return 0
    else:
        for i_index, i_value in enumerate(reversed(list_of_spoken_numbers[:-1])):
            if i_value == most_recently_spoken_number:
                return i_index + 1

goal_iteration = 2020  # We want to know the 2020th number in the spoken sequence.
spoken_numbers = starting_numbers.copy()
for i in range(0,goal_iteration - len(starting_numbers)):
    next_spoken_number = get_next_spoken_number(spoken_numbers)
    spoken_numbers.append(next_spoken_number)
print("Part 1 - The 2020th spoken number in the sequence will be: ", spoken_numbers[-1])

# =========================================================

def play_game(timestamp_dict, last_spoken_number, current_timestamp):
    if (last_spoken_number in timestamp_dict.keys()):  # The word has been spoken before
        next_spoken_number = i - timestamp_dict[last_spoken_number]
        timestamp_dict[last_spoken_number] = i
    else:  # word has not been spoken before
        next_spoken_number = 0
        timestamp_dict[last_spoken_number] = i
    return next_spoken_number, timestamp_dict

goal_iteration = 30000000
timestamps = {}
for i_index, i_value in enumerate(starting_numbers[:-1]):
    timestamps[i_value] = i_index  # "4: [0, True]"  means that the number 4 was last spoken at time 0 and it's the only time
most_recently_spoken_number = starting_numbers[-1]

for i in range(len(starting_numbers)-1, goal_iteration-1):
    most_recently_spoken_number, timestamps = play_game(timestamps, most_recently_spoken_number, i)
    # if (i % 1000 == 0):  # Use for tracking progress by 1,000 increments
    #     print(i)

print("Part 2 - The 30000000th spoken number in the sequence will be: ", most_recently_spoken_number)