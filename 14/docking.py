import re

input = open('./input.txt')
# input = open('./input_small.txt')
lines = input.readlines()
lines = list(map(lambda s: s.strip(), lines))

def int_to_binary(input_int):
    output_binary = '{0:036b}'.format(input_int)
    return output_binary

def binary_to_int(input_binary):
    output_int = int(input_binary, 2)
    return output_int

def apply_mask_to_binary(mask, input_binary):
    masked_binary = input_binary
    for i_index, i_value in enumerate(mask):
        if (i_value != "X"):
            masked_binary = masked_binary[:i_index] + i_value + masked_binary[i_index+1:]
    return masked_binary

def apply_mask_to_binary_v2(mask, input_binary):
    masked_binary = input_binary
    for i_index, i_value in enumerate(mask):
        if (i_value != "0"):
            masked_binary = masked_binary[:i_index] + i_value + masked_binary[i_index+1:]
    return masked_binary

def get_memory_address_list(mask, memory_address_binary):
    memory_address_list = []
    masked_memory_address_with_floaters = apply_mask_to_binary_v2(mask, memory_address_binary)
    # At this point, the address has been turned to binary AND masked, but still has X's in it
    floater_count = masked_memory_address_with_floaters.count("X")
    floater_locations = list(x for x in enumerate(masked_memory_address_with_floaters) if x[1] == "X") # [(30, 'X'), (35, 'X')]
    for i in range(0, 2**floater_count):
        binary = bin(i)[2:].zfill(floater_count)
        new_address = masked_memory_address_with_floaters
        for j_index, j_value in enumerate(floater_locations):
            new_address = new_address[:j_value[0]] + binary[j_index] + new_address[j_value[0]+1:]
        memory_address_list.append(binary_to_int(new_address))
    return memory_address_list  # List of INTEGER addresses, one for each possibility resulting from floaters

memory = {}
mask = ""
for i in lines:
    if (i[:4] == "mask"):
        mask = i[7:]
    elif (i[:3] == "mem"):
        memory_address = int(re.search('\[(.*)\]', i).group(1))
        unmasked_memory_value_int = int(re.search('= (.*)$', i).group(1))
        masked_memory_value_int = binary_to_int(apply_mask_to_binary(mask, int_to_binary(unmasked_memory_value_int)))
        memory[memory_address] = masked_memory_value_int

sum = 0
for key in memory:
    sum += memory[key]
print("Part 1 - Sum of all memory values after the last line: ", sum)

# =========================================

memory = {}
mask = ""
for i in lines:
    if (i[:4] == "mask"):
        mask = i[7:]
    elif (i[:3] == "mem"):
        memory_address = int(re.search('\[(.*)\]', i).group(1))
        unmasked_memory_value_int = int(re.search('= (.*)$', i).group(1))
        memory_address_binary = int_to_binary(memory_address)
        memory_address_list = get_memory_address_list(mask, memory_address_binary)
        for address in memory_address_list:
            memory[address] = unmasked_memory_value_int

sum = 0
for key in memory:
    sum += memory[key]
print("Part 2 - Sum of all memory values after the last line: ", sum)
