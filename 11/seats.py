input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()
map_width = len(lines[0]) - 1  # Subtract the \n
map_height = len(lines)

seat_map = {}
for i_index, i_value in enumerate(lines):  # for each row (Y coord)
    for j_index, j_value in enumerate(i_value.replace('\n', '')):  # for each column (X coord) in this row
        seat_map[(j_index, i_index)] = j_value
# print(seat_map)

def step_forward_one_round(starting_map):  # DIRECT ADJACENCY SEATING (1)
    new_map = {}
    for x in range(0, map_width):
        for y in range(0, map_height):
            coordinates = (x,y)
            new_map[coordinates] = "."

            # Get the surrounding spots
            occupied_adjacent_seats = 0
            for neighbor in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]:
                neighbor_coordinates = (x+neighbor[0],y+neighbor[1])
                if (neighbor_coordinates in starting_map.keys()):
                    if (starting_map[neighbor_coordinates] == "#"):
                        occupied_adjacent_seats += 1
            
            if (starting_map[coordinates] == "L"):
                if (occupied_adjacent_seats == 0):
                    new_map[coordinates] = "#"
                else:
                    new_map[coordinates] = "L"
            elif (starting_map[coordinates] == "#"):
                if (occupied_adjacent_seats >= 4):
                    new_map[coordinates] = "L"
                else:
                    new_map[coordinates] = "#"
    return new_map


def step_forward_one_round_los(starting_map):  # LINE OF SIGHT SEATING (2)
    new_map = {}
    for x in range(0, map_width):
        for y in range(0, map_height):
            coordinates = (x,y)
            new_map[coordinates] = "."

            # Get the surrounding spots
            occupied_adjacent_seats = 0
            for neighbor in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]:
                thing_found = "."
                neighbor_coordinates = (x,y)
                while (thing_found == "."):
                    neighbor_coordinates = (neighbor_coordinates[0]+neighbor[0],neighbor_coordinates[1]+neighbor[1])
                    if (neighbor_coordinates in starting_map.keys()):
                        thing_found = starting_map[neighbor_coordinates]
                    else:
                        break
                if (thing_found == "#"):
                        occupied_adjacent_seats += 1
            
            if (starting_map[coordinates] == "L"):
                if (occupied_adjacent_seats == 0):
                    new_map[coordinates] = "#"
                else:
                    new_map[coordinates] = "L"
            elif (starting_map[coordinates] == "#"):
                if (occupied_adjacent_seats >= 5):
                    new_map[coordinates] = "L"
                else:
                    new_map[coordinates] = "#"
    return new_map


def stabilize(starting_map, seating_strategy):
    new_map = {}
    while (new_map != starting_map):
        if (new_map != {}):
            starting_map = new_map
        if (seating_strategy == 1):
            new_map = step_forward_one_round(starting_map)
        elif (seating_strategy == 2):
            new_map = step_forward_one_round_los(starting_map)
    return new_map

stabilized_map = stabilize(seat_map, 1)
occupied_count = 0
for x in range(0, map_width):
    for y in range(0, map_height):
        coordinates = (x,y)
        if (stabilized_map[coordinates] == "#"):
            occupied_count += 1

print("Part 1 - Number of occupied seats: ", occupied_count)

stabilized_map = stabilize(seat_map, 2)
occupied_count = 0
for x in range(0, map_width):
    for y in range(0, map_height):
        coordinates = (x,y)
        if (stabilized_map[coordinates] == "#"):
            occupied_count += 1

print("Part 2 - Number of occupied seats: ", occupied_count)