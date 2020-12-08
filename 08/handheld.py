def basic_executor(line):
    execution_complete = False
    if (line[:3] == "acc"):
        next_line_relative_index = 1
        if (line.split(" ")[1][0] == "+"):
            accumulator_delta = int(line.split(" ")[1][1:])
        elif (line.split(" ")[1][0] == "-"):
            accumulator_delta = int(line.split(" ")[1][1:]) * -1
        else:
            print("Unexpected sign on acc number!")
    
    elif (line[:3] == "jmp"):
        accumulator_delta = 0
        if (line.split(" ")[1][0] == "+"):
            next_line_relative_index = int(line.split(" ")[1][1:])
        elif (line.split(" ")[1][0] == "-"):
            next_line_relative_index = int(line.split(" ")[1][1:]) * -1
        else:
            print("Unexpected sign on jmp number!")
    
    elif (line[:3] == "nop"):
        next_line_relative_index = 1
        accumulator_delta = 0

    elif (line[:3] == "!!!"):
        next_line_relative_index = 0
        accumulator_delta = 0
        execution_complete = True
    
    else:
        print("Unexpected operation code!")
    return next_line_relative_index, accumulator_delta, execution_complete

input = open('./input.txt')
lines = input.readlines()
lines.append("!!! +123")  # Manually add a line at the end. If this gets executed, then the program made it to the end! (No infinite loops)
enumerated_lines = enumerate(lines)

encountered_lines = []  # Add the index of each line we execute, so we can check if we're repeating a line.
next_line = 0
accumulator = 0

while (next_line not in encountered_lines):
    encountered_lines.append(next_line)
    line_delta, accumulator_delta, success_flag = basic_executor(lines[next_line])
    next_line = next_line + line_delta
    accumulator = accumulator + accumulator_delta

print("Part 1 - before repeating any instructions, the accumulator value is: ", accumulator)

for i_index, i_value in enumerated_lines:
    # Do the replacement...
    if (i_value[:3] == "jmp"):
        lines_copy = lines.copy()
        lines_copy[i_index] = lines_copy[i_index].replace("jmp", "nop", 1)
    elif (i_value[:3] == "nop"):
        lines_copy = lines.copy()
        lines_copy[i_index] = lines_copy[i_index].replace("nop", "jmp", 1)
    
    # And then see if the replacement fixed the infinite loop issue.
    if (i_value[:3] == "acc" or i_value[:3] == "!!!"):  # Don't need to try it for scenarios where we changed nothing.
        pass
    else:
        encountered_lines = []
        next_line = 0
        accumulator = 0
        success_flag = False
        while (next_line not in encountered_lines):
            encountered_lines.append(next_line)
            line_delta, accumulator_delta, success_flag = basic_executor(lines_copy[next_line])
            next_line = next_line + line_delta
            accumulator = accumulator + accumulator_delta
        if (success_flag):
            print("Part 2 - after fixing the infinite loop instruction, the accumulator value is: ", accumulator)
            break