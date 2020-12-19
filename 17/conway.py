from collections import OrderedDict
import itertools
import copy

three_d_neighbors = [p for p in itertools.product([-1,0,1], repeat=3)]
three_d_neighbors.remove((0,0,0))

four_d_neighbors = [p for p in itertools.product([-1,0,1], repeat=4)]
four_d_neighbors.remove((0,0,0,0))

input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()
lines = list(map(lambda s: s.strip(), lines))

layers = OrderedDict()  # Layers starts as just the provided single slice of the pocket dimension.
layers[0] = OrderedDict()
for row_index, row_value in enumerate(lines):
    layers[0][row_index] = OrderedDict()
    for col_index, col_value in enumerate(row_value):
        layers[0][row_index][col_index] = col_value

def print_pocket_dimension(pocket_dimension_dict):
    for layer_key in pocket_dimension_dict.keys():
        print("Layer z = ", layer_key)
        for row_key in pocket_dimension_dict[layer_key].keys():
            row_list_to_print = []
            for col_key in pocket_dimension_dict[layer_key][row_key].keys():
                row_list_to_print.append(pocket_dimension_dict[layer_key][row_key][col_key])
            print(*row_list_to_print, sep=' ')

def add_shell_layer(pocket_dimension_dict):  # Returns the same dict, with one layer (on all 6 sides of the cube) of "." added
    padded_pocket_dimension_dict = copy.deepcopy(pocket_dimension_dict)
    # Add another dot to the ends of each row
    min_column = min(padded_pocket_dimension_dict[0][0].keys())
    max_column = max(padded_pocket_dimension_dict[0][0].keys())
    for layer_key in padded_pocket_dimension_dict.keys():
        for row_key in padded_pocket_dimension_dict[layer_key].keys():
            padded_pocket_dimension_dict[layer_key][row_key][min_column-1] = "."
            padded_pocket_dimension_dict[layer_key][row_key].move_to_end(min_column - 1, last=False)
            padded_pocket_dimension_dict[layer_key][row_key][max_column+1] = "."
            padded_pocket_dimension_dict[layer_key][row_key].move_to_end(max_column + 1)
    # Add another row of dots to the ends of each layer
    min_row = min(padded_pocket_dimension_dict[0].keys())
    max_row = max(padded_pocket_dimension_dict[0].keys())
    for layer_key in padded_pocket_dimension_dict.keys():
        padded_pocket_dimension_dict[layer_key][min_row-1] = OrderedDict()
        padded_pocket_dimension_dict[layer_key].move_to_end(min_row - 1, last=False)
        padded_pocket_dimension_dict[layer_key][max_row+1] = OrderedDict()
        padded_pocket_dimension_dict[layer_key].move_to_end(max_row + 1)
    for layer_key in padded_pocket_dimension_dict.keys():
        for row_key in [min_row-1, max_row+1]:
            for i in range(min_column-1, max_column+2):
                padded_pocket_dimension_dict[layer_key][row_key][i] = "."
    # Add another layer of dots to the ends of the pocket_dimension_dict    
    min_layer = min(padded_pocket_dimension_dict.keys())
    max_layer = max(padded_pocket_dimension_dict.keys())
    padded_pocket_dimension_dict[min_layer - 1] = OrderedDict()
    padded_pocket_dimension_dict.move_to_end(min_layer - 1, last=False)
    padded_pocket_dimension_dict[max_layer + 1] = OrderedDict()
    padded_pocket_dimension_dict.move_to_end(min_layer + 1)
    for layer_key in [min_layer-1, max_layer+1]:
        for row_key in range(min_row-1, max_row+2):
            padded_pocket_dimension_dict[layer_key][row_key]=OrderedDict()
            for col_key in range(min_column-1, max_column+2):
                padded_pocket_dimension_dict[layer_key][row_key][col_key] = "."
    return padded_pocket_dimension_dict

def find_active_neighbors(coordinate_tuple, unpadded_pocket_dimension_dict):  # Coords are (x,y,z)
    active_neighbor_list = []
    for neighbor in three_d_neighbors:
        neighbor_coordinates = (coordinate_tuple[0]+neighbor[0],coordinate_tuple[1]+neighbor[1],coordinate_tuple[2]+neighbor[2])
        x = neighbor_coordinates[0]
        y = neighbor_coordinates[1]
        z = neighbor_coordinates[2]
        if (z in unpadded_pocket_dimension_dict.keys()):
            if (y in unpadded_pocket_dimension_dict[z].keys()):
                if (x in unpadded_pocket_dimension_dict[z][y].keys()):
                    if (unpadded_pocket_dimension_dict[z][y][x] == "#"):
                        active_neighbor_list.append((x, y, z))
    return active_neighbor_list

# --------------------------- PART 1 -----------------------------------------------------------------------------------------------
# for range (1,7)
# for each cube in the whole thing (UNPADDED)
#   check it's neighbors. You'll get active-neighbor-list in return. Change it active/inactive based on count of active neighbor
mutable_padded_dict = copy.deepcopy(layers)
# print_pocket_dimension(mutable_padded_dict)
for i in range(1,7):
    mutable_padded_dict = add_shell_layer(mutable_padded_dict)
    temp_mutable_padded_dict = copy.deepcopy(mutable_padded_dict)
    for layer_key in mutable_padded_dict.keys():
        for row_key in mutable_padded_dict[layer_key].keys():
            for col_key in mutable_padded_dict[layer_key][row_key].keys():
                neighbor_list = find_active_neighbors((col_key, row_key, layer_key), mutable_padded_dict)
                if (mutable_padded_dict[layer_key][row_key][col_key]=="#"):
                    if(not(len(neighbor_list)==2 or len(neighbor_list)==3)):
                        temp_mutable_padded_dict[layer_key][row_key][col_key]="."
                else:
                    if (len(neighbor_list)==3):
                        temp_mutable_padded_dict[layer_key][row_key][col_key]="#"
    mutable_padded_dict = temp_mutable_padded_dict

# print_pocket_dimension(mutable_padded_dict)

part1_active_count = 0
for layer_key in mutable_padded_dict.keys():
        for row_key in mutable_padded_dict[layer_key].keys():
            for col_key in mutable_padded_dict[layer_key][row_key].keys():
                if (mutable_padded_dict[layer_key][row_key][col_key]=="#"):
                    part1_active_count += 1
print("Part 1 - Number of active cubes left after six 3-D simulation rounds: ",part1_active_count)

# --------------------------- PART 1 -----------------------------------------------------------------------------------------------
#
# --------------------------- PART 2 -----------------------------------------------------------------------------------------------

# --------------------------- PART 2 -----------------------------------------------------------------------------------------------
