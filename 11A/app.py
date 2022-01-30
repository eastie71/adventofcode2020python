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
    from_row = 0 if row == 0 else row - 1
    to_row = row if row >= len(current_seat_map)-1 else row + 1
    from_col = 0 if col == 0 else col - 1
    to_col = col if col >= len(current_seat_map[0])-1 else col + 1

    row_num = from_row
    col_num = from_col
    while row_num <= to_row:
        col_num = from_col
        while col_num <= to_col:
            if row_num != row or col_num != col:
                if current_seat_map[row_num][col_num] == '#':
                    count += 1
            col_num += 1
        row_num += 1
    
    # print(f"For Seat ({row},{col}), occupied count = {count}")
    return count

def count_occupied_seats(seat_map):
    seat_count = 0
    for seat_row in seat_map:
        for col_num in range(0, len(seat_row)):
            if seat_row[col_num] == '#':
                seat_count += 1
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
                    # "." is the floor - just map this over
                    case ".":
                        new_seat_map[row_num] += seat
                    case "#":
                        # For an occupied seat (#) - check if more than 4 adjacent seats are occupied, then empty it
                        if get_adjacent_occupied_count(row_num,col_num) >= 4:
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
print(f"2020 Question 11A: Total Occupied Seats = {get_total_occupied_seats(seating_map)}, in {map_iteration_count} iterations")