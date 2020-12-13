import math

input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()
lines = map(lambda s: s.strip(), lines)

def navigate_one_line(starting_position, starting_direction, instruction):
    instr_action = instruction[0]
    instr_number = int(instruction[1:])

    if (instr_action == "N"):
        ending_position = [starting_position[0], starting_position[1] + instr_number]
        ending_direction = starting_direction
    elif (instr_action == "E"):
        ending_position = [starting_position[0] + instr_number, starting_position[1]]
        ending_direction = starting_direction
    elif (instr_action == "S"):
        ending_position = [starting_position[0], starting_position[1] - instr_number]
        ending_direction = starting_direction
    elif (instr_action == "W"):
        ending_position = [starting_position[0] - instr_number, starting_position[1]]
        ending_direction = starting_direction
    elif (instr_action == "L"):
        ending_position = starting_position
        ending_direction = (starting_direction - instr_number) % 360
    elif (instr_action == "R"):
        ending_position = starting_position
        ending_direction = (starting_direction + instr_number) % 360
    elif (instr_action == "F"):
        if (starting_direction == 0):
            ending_position = [starting_position[0], starting_position[1] + instr_number]
        elif (starting_direction == 90):
            ending_position = [starting_position[0] + instr_number, starting_position[1]]
        elif (starting_direction == 180):
            ending_position = [starting_position[0], starting_position[1] - instr_number]
        elif (starting_direction == 270):
            ending_position = [starting_position[0] - instr_number, starting_position[1]]
        ending_direction = starting_direction

    return ending_position, ending_direction


def navigate_waypoint_one_line(starting_boat_position, starting_waypoint_position, instruction):
    instr_action = instruction[0]
    instr_number = int(instruction[1:])

    if (instr_action == "N"):
        ending_boat_position = starting_boat_position
        ending_waypoint_position = [starting_waypoint_position[0], starting_waypoint_position[1] + instr_number]
    elif (instr_action == "E"):
        ending_boat_position = starting_boat_position
        ending_waypoint_position = [starting_waypoint_position[0] + instr_number, starting_waypoint_position[1]]
    elif (instr_action == "S"):
        ending_boat_position = starting_boat_position
        ending_waypoint_position = [starting_waypoint_position[0], starting_waypoint_position[1] - instr_number]
    elif (instr_action == "W"):
        ending_boat_position = starting_boat_position
        ending_waypoint_position = [starting_waypoint_position[0] - instr_number, starting_waypoint_position[1]]
    elif (instr_action == "L"):
        ending_boat_position = starting_boat_position
        degrees = math.radians(instr_number % 360)
        x1 = starting_waypoint_position[0]*math.cos(degrees) - starting_waypoint_position[1]*math.sin(degrees)
        y1 = starting_waypoint_position[0]*math.sin(degrees) + starting_waypoint_position[1]*math.cos(degrees)
        ending_waypoint_position = [x1, y1]
    elif (instr_action == "R"):
        ending_boat_position = starting_boat_position
        degrees = math.radians(-1 * (instr_number % 360))
        x1 = starting_waypoint_position[0]*math.cos(degrees) - starting_waypoint_position[1]*math.sin(degrees)
        y1 = starting_waypoint_position[0]*math.sin(degrees) + starting_waypoint_position[1]*math.cos(degrees)
        ending_waypoint_position = [x1, y1]
    elif (instr_action == "F"):
        ending_boat_position = starting_boat_position
        for i in range(0, instr_number):
            ending_boat_position[0] += starting_waypoint_position[0]
            ending_boat_position[1] += starting_waypoint_position[1]
        ending_waypoint_position = starting_waypoint_position

    return ending_boat_position, ending_waypoint_position


starting_position = [0,0]
starting_direction = 90  # 0:North, 90:East, 180:South, 270:West
boat_position = [0,0]
waypoint_position = [10, 1]
for instruction in lines:
    starting_position, starting_direction = navigate_one_line(starting_position, starting_direction, instruction)
    boat_position, waypoint_position = navigate_waypoint_one_line(boat_position, waypoint_position, instruction)

print("Part 1 - Manhattan distance from starting position was: ", abs(starting_position[0]) + abs(starting_position[1]))

print("Part 2 - Manhattan distance from starting position was: ", int(abs(boat_position[0]) + abs(boat_position[1])))
