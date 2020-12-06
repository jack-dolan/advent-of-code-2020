def binary_space_location(boarding_pass):
    # Returns this boarding pass' row (0-127) and column (0-7), and the seat ID (multiply the row by 8, then add the column)

    row_range = [0, 127]  # [minPossibleValue, maxPossibleValue]
    col_range = [0, 7]

    # Determine the row
    for i in range(0, 6):
        if (boarding_pass[i] == "B"):
            row_range = [row_range[0] + ((row_range[1]-row_range[0]+1)/2), row_range[1]]
        else:
            row_range = [row_range[0], row_range[1] - ((row_range[1]-row_range[0]+1)/2)]
    if (boarding_pass[6] == "B"):
        row = row_range[1]
    else:
        row = int(row_range[0])
    
    # Determine the column
    for i in range(7, 9):
        if (boarding_pass[i] == "R"):
            col_range = [col_range[0] + ((col_range[1]-col_range[0]+1)/2), col_range[1]]
        else:
            col_range = [col_range[0], col_range[1] - ((col_range[1]-col_range[0]+1)/2)]
    if (boarding_pass[9] == "R"):
        column = col_range[1]
    else:
        column = int(col_range[0])

    seat_id = int((row * 8)  + column)
    return row, column, seat_id

input = open('./input.txt')
lines = input.readlines()

highest_seat_id = 0
all_filled_seats = []  # list of all seats with corresponding passes (list contains the seat ids)
for i in lines:
    row, column, seat_id = binary_space_location(i)
    if (seat_id > highest_seat_id):
        highest_seat_id = seat_id
    all_filled_seats.append(seat_id)

print("Part 1 - Highest seat ID: ", highest_seat_id)

passengerless_seats = []
for i in range(0,128):
    for j in range (0,8):
        if (int((i * 8)  + j) not in all_filled_seats):
            passengerless_seats.append(int((i * 8)  + j))

# Some of the seats at front and end of plane don't exist.
# My seat is the one in passengerless_seats that isn't durrounded by its neigbors
my_seat = []
for i in passengerless_seats:
    if ((i-1) not in passengerless_seats and (i+1) not in passengerless_seats):
        my_seat.append(i)
print("Part 2 - My seat ID: ", my_seat)