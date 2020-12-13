input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()

earliest_availability = int(lines[0])
service_list = lines[1].split(",")

# Part 1 - Need to find the bus from service_list which will depart the soonest after my earliest_availability
# The buses marked "x" are 'probably' out of service... don't look at them for part 1.
# We want the first multiple of each bus# that is >= earliest_availability. i.e. for buses=[5,7], availability=71
# Bus 5: 5, 10, 15, 20, ..., 65, 70, **75**, 80, ...
# Bus 7: 7, 14, 21, ..., 63, 70, **77**, 84, ...
# We'd pick bus 5 because it would arrive at time 75. 75 > 71, and 75 < 77.

in_service_list = list(int(x) for x in service_list if x != "x")
earliest_valid_departures = {}
for bus in in_service_list:
    departure = 0
    while departure < earliest_availability:
        departure = departure + bus
    earliest_valid_departures[bus] = departure

chosen_bus = min(earliest_valid_departures, key=earliest_valid_departures.get)
wait_time = earliest_valid_departures[chosen_bus] - earliest_availability
print("Part 1 - ID of chosen bus (", chosen_bus, ") multiplied by wait time (", wait_time, "): ", chosen_bus * wait_time)

# Part 2 - Need to find the timestamp where each of the buses in the input leave one minue apart from each other
# Now the 'x' spaces DO matter - they are minutes in the sequence with no constraints on which bus leaves / doesn't leave
# So for [5, x, 6, 9, 17, x, x, 25]
# We need to find timestamp T where bus5 leaves at T, then bus6 leaves at T+2 (skipped 1 because of x), bus9 leaves at T+3, ...
# We want T%5=0; (T+2)%6=0; (T+3)%9=0; (T+4)%17=0; and (T+7)%25=0
# NOTE : ALL of the buses in the schedule are prime... 

small_list = ['67','7','59','61']

# timestamp = 67
# while ((timestamp + 1) % 7 != 0):
#     timestamp += 67
# print(timestamp)

# timestamp = 335
# while ((timestamp + 2) % 59 != 0):
#     timestamp += (67 * 7)
# print(timestamp)

# timestamp = 6901
# while ((timestamp + 3) % 61 != 0):
#     timestamp += (67 * 7 * 59)
# print(timestamp)

# ========================================================
def find_first_sequence(service_list):
    valid_buses = []
    for i_index, i_value in enumerate(service_list):
        if (i_value != "x"):
            valid_buses.append((int(i_value), i_index))  # For small_list, it'd be: [(67,0),(7,1),(59,2),(61,3)]

    jump = int(service_list[0])  # This is the num to ADD each iteration of the while loop. Each iter of forLoop, * it by current bus#
    timestamp = int(service_list[0])  # This is the starting point for each round of forLoop. Gets set to the result of the while loop.
    for i_index, i_value in enumerate(valid_buses[:-1]):
        next_value = valid_buses[i_index+1][0]
        next_offset = valid_buses[i_index+1][1]
        while ((timestamp + next_offset) % next_value !=0):
            timestamp += jump
        jump = jump * next_value

    return timestamp

print("part 2 - Earliest timestamp that gives a valid sequence: ", find_first_sequence(service_list))