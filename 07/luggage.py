def bag_support_checker(examined_bag_type, desired_bag_type, bag_library):
    supported_bags = []  # List of all bag types supported by this bag (examined_bag_type)
                         # If empty, dead end (no other bags).
    if (bag_library[examined_bag_type] == []):  # This bag holds nothing. Definitely doesn't hold the desired bag
        support = False
    elif (desired_bag_type in map(lambda x: x[0], bag_library[examined_bag_type])): # Desired bag is IN this bag. Definitely holds the desired bag
        support = True
    
    else:  # Desired bag isn't in this bag, but it might be in this bag's bags. Use recursion to find out...
        support = False
        for bag_type in map(lambda x: x[0], bag_library[examined_bag_type]):
            if bag_support_checker(bag_type, desired_bag_type, bag_library):
                support = True

    return support  # bools - support True if bag supports desired_bag_type


def bag_capacity_checker(examined_bag_type, bag_library):
    if (bag_library[examined_bag_type] == []):  # This bag holds nothing.
        capacity = 0
    else:  # this bag contains something...
        # Capacity is: 
        # sum of all quantities from bag_library[examined_bag_type]
        # +
        # sum of all (quantity from bag_library[examined_bag_type] * bag_capacity_checker(this bag))
        capacity = sum(map(lambda x: x[1], bag_library[examined_bag_type])) + sum(map(lambda x: x[1] * bag_capacity_checker(x[0], bag_library), bag_library[examined_bag_type]))
    return capacity


input = open('./input.txt')
lines = input.readlines()

bag_catalog = {}
# Dictionary containing all bag types (e.g. "shiny gold"), and the bag types / quantity they can hold
# Format is:
# {
#   "shiny gold": [["neon yellow", 1], ["dull blue", 2]]
#   "neon yellow": [["warm red", 5]]
#   "dull blue": []
# }

for i in lines:
    words = i.split(" ")
    base_bag = words[0] + " " + words[1]
    if (words[-3:] == ["no", "other", "bags."]):  # Bag is a dead end... no more bags contained within it
        bag_catalog[base_bag] = []
    else:  # Sentence will be of the format: "base1 base2 bags contain X Xword1 Xword2 bags, Y Yword1 Yword2 bags."
        value_list = []  # Will take the form of [["neon yellow", 1], ["dull blue", 2]]
        for j in range(0, int((len(words)-4)/4)):
            # x_list = []  # will take the form of ["warm red", 5]
            X = int(words[4 * (j + 1)])
            xWord1 = words[4 * (j + 1) + 1]
            xWord2 = words[4 * (j + 1) + 2]
            # value_list.append(x_list)
            value_list.append([xWord1 + " " + xWord2, X])
        bag_catalog[base_bag] = value_list

# print(bag_support_checker("dotted indigo", "shiny gold", bag_catalog)) # Directly has it
# print(bag_support_checker("faded salmon", "shiny gold", bag_catalog)) # Holds no bags
# print(bag_support_checker("muted tomato", "shiny gold", bag_catalog)) # Holds indirectly by 1 level
# print(bag_support_checker("bright red", "shiny gold", bag_catalog)) # Holds indirectly by 2 levels

can_hold_goldie_count = 0
for i in bag_catalog:
    if bag_support_checker(i, "shiny gold", bag_catalog):
        can_hold_goldie_count += 1

print("Part 1 - Number of bags that can support a shiny gold bag: ", can_hold_goldie_count)
print("Part 2 - A single shiny gold bag contains ", bag_capacity_checker("shiny gold", bag_catalog), " bags.")