"""
Day 11: Seating System
"""
current_seat_map = []
map_iteration_count = 0

#with open("test.txt", "r") as file:
with open("Q11input.txt", "r") as file:
    data = file.readlines()
    seating_map = [line.strip() for line in data]

def get_adjacent_occupied_count(row,col):
    global current_seat_map
    count = 0
    from_row = row
    from_col = col

    # Check NORTH
    to_row = 0
    to_col = col
    row_num = from_row
    col_num = from_col
    while row_num >= to_row:
        if row_num != row:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num -= 1
    
    # Check NORTH EAST
    to_row = 0
    to_col = len(current_seat_map[0])
    row_num = from_row
    col_num = from_col
    while row_num >= to_row and col_num < to_col:
        if row_num != row or col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num -= 1
        col_num += 1

    # Check EAST
    to_row = row
    to_col = len(current_seat_map[0])
    row_num = from_row
    col_num = from_col
    while col_num < to_col:
        if col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        col_num += 1

    # Check SOUTH EAST
    to_row = len(current_seat_map)
    to_col = len(current_seat_map[0])
    row_num = from_row
    col_num = from_col
    while row_num < to_row and col_num < to_col:
        if row_num != row or col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num += 1
        col_num += 1

    # Check SOUTH
    to_row = len(current_seat_map)
    to_col = col
    row_num = from_row
    col_num = from_col
    while row_num < to_row:
        if row_num != row:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num += 1

    # Check SOUTH WEST
    to_row = len(current_seat_map)
    to_col = 0
    row_num = from_row
    col_num = from_col
    while row_num < to_row and col_num >= to_col:
        if row_num != row or col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num += 1
        col_num -= 1

    # Check WEST
    to_row = row
    to_col = 0
    row_num = from_row
    col_num = from_col
    while col_num >= to_col:
        if col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        col_num -= 1

    # Check NORTH EAST
    to_row = 0
    to_col = 0
    row_num = from_row
    col_num = from_col
    while row_num >= to_row and col_num >= to_col:
        if row_num != row or col_num != col:
            if current_seat_map[row_num][col_num] == '#':
                count += 1
                break
            elif current_seat_map[row_num][col_num] == 'L':
                break
        row_num -= 1
        col_num -= 1

    # print(f"For Seat ({row},{col}), occupied count = {count}")
    return count

def count_occupied_seats(seat_map):
    seat_count = 0
    for seat_row in seat_map:
        seat_count += seat_row.count("#")
    return seat_count

def get_total_occupied_seats(seat_map):
    new_seat_map = []
    current_seat_count = -1

    global current_seat_map 
    global map_iteration_count
    current_seat_map = seat_map
    row_width = len(current_seat_map[0])

    while True:
        new_seat_map = []
        for row_num in range(0, len(current_seat_map)):
            new_seat_map.append("")
            for col_num in range(0, row_width):
                seat = current_seat_map[row_num][col_num]

                match seat:
                    # "." is the floor - just skip this over
                    case ".":
                        new_seat_map[row_num] += seat
                    case "#":
                        # For an occupied seat (#) - check if more than 5 adjacent seats are occupied, then empty it
                        if get_adjacent_occupied_count(row_num,col_num) >= 5:
                            new_seat_map[row_num] += 'L'
                        else:
                            new_seat_map[row_num] += seat
                    case "L":
                        # For an unoccupied seat (L) - check if NO adjacent seats are occupied - then occupy it
                        if get_adjacent_occupied_count(row_num,col_num) == 0:
                            new_seat_map[row_num] += '#'
                        else:
                            new_seat_map[row_num] += seat
                    case _:
                        print("Unexpected Seat Type found - Exiting with -1")
                        return -1
        
        new_seat_count = count_occupied_seats(new_seat_map)
        # If the seat count hasn't changed then occupied seats have stabilized and wont change anymore - so we have out answer!
        if new_seat_count == current_seat_count:
            break

        map_iteration_count += 1
        current_seat_count = new_seat_count
        current_seat_map = new_seat_map
        # print(current_seat_map)
    
    return current_seat_count

# print(seating_map)
print(f"2020 Question 11B: Total Occupied Seats = {get_total_occupied_seats(seating_map)}, in {map_iteration_count} iterations")