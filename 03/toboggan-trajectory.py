# Part 1
# Input is a topography map. Dots are open spaces, hashes are trees. The map repeats infitely to the right. 
# If my sled only can go in a straight line (SLOPE is RIGHT 3, DOWN 1), how many trees will I encounter?

input = open('./input.txt')
lines = input.readlines()

# Part 1 - Want to pass to a function: the map (lines), slope (eg [3,1]), and my current spot (starting at [0,0])
#          Want to receive back: new coordinates (first one would be [3,1]) and if the space contents is a tree (1) or empty (0)
def sled_mover(map_array, slope, pre_move_coordinates):
    rightmost_row = len(map_array[0]) - 1  # If the new x-pos is over this number, loop back around
    if (pre_move_coordinates[0] + slope[0] > rightmost_row):
        post_move_coordinates = [
        ((pre_move_coordinates[0] + slope[0]) % rightmost_row) - 1,
        pre_move_coordinates[1] + slope[1]
        ]
    else:
        post_move_coordinates = [
        (pre_move_coordinates[0] + slope[0]),
        pre_move_coordinates[1] + slope[1]
        ]
    if (map_array[post_move_coordinates[1]][post_move_coordinates[0]] == "#"):
        contents = 1
    elif (map_array[post_move_coordinates[1]][post_move_coordinates[0]] == "."):
        contents = 0
    else:
        print("Unrecognized character error!")
    return post_move_coordinates, contents


map = []
for i in lines:
    single_line = []
    for j in i:
        if (j != '\n'):
            single_line.append(j)
    map.append(single_line)

# top_row = 0
bottom_row = len(map) - 1  # When your returned coordinates have bottom_row in the x-coord spot, stop moving

start_coordinates = [0,0]
number_of_trees = 0
while (start_coordinates[1] < bottom_row):
    start_coordinates, contents = sled_mover(map, [3,1], start_coordinates)
    number_of_trees += contents

print("Part 1 - Number of trees encountered: ", number_of_trees)

hit_trees_array = []  # For each of the 5 slopes below, append the resultant # of hit trees to this list
for varying_slope in [[1,1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    start_coordinates = [0,0]
    number_of_trees = 0
    while (start_coordinates[1] < bottom_row):
        start_coordinates, contents = sled_mover(map, varying_slope, start_coordinates)
        number_of_trees += contents
    hit_trees_array.append(number_of_trees)

print("Part 2 - Product of all trees encountered: ", hit_trees_array[0]*hit_trees_array[1]*hit_trees_array[2]*hit_trees_array[3]*hit_trees_array[4])