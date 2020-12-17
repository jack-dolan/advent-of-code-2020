import re

input = open('./input.txt')
# input = open('./input_small.txt')
# input = open('./input_small_2.txt')
paragraphs = input.read().split("\n\n")

known_fields = paragraphs[0].split("\n")
field_ranges = {}
for i in known_fields:
    # Everything up to first colon is field_name. Use it as the key in field_ranges
    field_name = re.search('^(.*):', i).group(1)
    # Everything from colon space to next space is the first range
    range1 = list(map(lambda s: int(s), re.search(': (.*) or', i).group(1).split("-")))
    # Everything from or space to the end of the line is the second range
    range2 = list(map(lambda s: int(s), re.search('or (.*)$', i).group(1).split("-")))    
    field_ranges[field_name] = [range1, range2]
my_ticket = (paragraphs[1].split("\n")[1]).split(",")
nearby_tickets = paragraphs[2].split("\n")[1:]

# ==========================================================================================

def get_invalid_numbers(ticket, allowed_ranges):
    invalid_numbers = []
    for number in ticket.split(","):
        number = int(number)
        for allowed_range in allowed_ranges:
            if (number in range(allowed_range[0], allowed_range[1]+1)):
                break
        else:
            invalid_numbers.append(number)
    return invalid_numbers

def combine_ranges(range_dictionary):
    all_original_ranges = []
    for key in range_dictionary.keys():
        all_original_ranges.append(range_dictionary[key][0])
        all_original_ranges.append(range_dictionary[key][1])
    all_original_ranges_sorted = sorted(all_original_ranges, key=lambda x: x[0])
    is_list_merged = False
    while not is_list_merged:
        for i_index, i_value in enumerate(all_original_ranges_sorted[:-1]):
            range1 = i_value
            range2 = all_original_ranges_sorted[i_index+1]
            if (range1[1] >= range2[0]):
                new_merged_range = [range1[0], range2[1]]
                # vv replace the original 2 ranges with the new range vv
                all_original_ranges_sorted = all_original_ranges_sorted[:i_index] + [new_merged_range] + all_original_ranges_sorted[i_index+2:]
                break
        else:
            is_list_merged = True
            
    return all_original_ranges_sorted

# ==========================================================================================

combined_ranges = combine_ranges(field_ranges)
invalid_numbers = []
tickets_to_purge = []
for index, ticket in enumerate(nearby_tickets):
    new_invalid_numbers = get_invalid_numbers(ticket, combined_ranges)
    invalid_numbers += new_invalid_numbers
    if new_invalid_numbers != []:
        tickets_to_purge.append(index)
print("Part 1 - Sum of all invalid numbers found is: ", sum(invalid_numbers))

# Purge all invalid tickets after Part 1 is complete
tickets_to_purge = sorted(tickets_to_purge, reverse=True)
for index in tickets_to_purge:
    del nearby_tickets[index]

nearby_tickets = list(map(lambda s: s.split(","), nearby_tickets))
valid_fields = []
for i in range(0, len(my_ticket)):
    values_in_ith_column = list(map(lambda s: int(s[i]), nearby_tickets))
    fields_that_work = []
    for key in field_ranges:
        range1 = field_ranges[key][0]
        range2 = field_ranges[key][1]
        for tried_number in values_in_ith_column:
            if (tried_number not in range(range1[0], range1[1]+1) and tried_number not in range(range2[0], range2[1]+1)):
                break
        else:
            fields_that_work.append(key)
    valid_fields.append([i, fields_that_work])

final_fields = []
delete_able_valid_fields = valid_fields.copy()
while len(final_fields) < len(valid_fields):
    indexes_to_delete = []
    fieldnames_to_delete = []
    for i_index, i_value in enumerate(delete_able_valid_fields):
        if (len(i_value[1]) == 1):
            final_fields.append(i_value)
            fieldnames_to_delete.append(i_value[1][0])
            indexes_to_delete.append(i_index)
    for index in sorted(indexes_to_delete, reverse=True):
        del delete_able_valid_fields[index]
    # delete all occurences of the field(s) that just got added from the stuff that remains
    for fieldname in fieldnames_to_delete:
        for i_index, i_value in enumerate(delete_able_valid_fields):
            if (fieldname in i_value[1]):
                delete_able_valid_fields[i_index][1].remove(fieldname)

field_names = {}
for i in final_fields:
    key = i[1][0]
    value = i[0]
    field_names[key] = value
departure_indexes = []
for key in field_names.keys():
    if ("departure" in key):
        departure_indexes.append(field_names[key])

q2_result = 1
for i in departure_indexes:
    q2_result *= int(my_ticket[i])
print("Part 2 - Multiplied 'departure' values are: ", q2_result)