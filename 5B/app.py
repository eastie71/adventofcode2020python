"""
Day 5: Binary Boarding
"""
def get_row_num(seat):
    min_row = 0
    max_row = 127
    for index in range(0,len(seat)-1):
        element = seat[index]
        diff = max_row - min_row
        match element:
            case "F":
                max_row -= round(diff/2)
            case "B":
                min_row += round(diff/2)
    if seat[6] == "F":
        return min_row
    else: # if seat[6] == "B"
        return max_row

def get_col_num(seat):
    min_col = 0
    max_col = 7
    for index in range(0,len(seat)-1):
        element = seat[index]
        diff = max_col - min_col
        match element:
            case "L":
                max_col -= round(diff/2)
            case "R":
                min_col += round(diff/2)
    if seat[2] == "L":
        return min_col
    else: # if seat[2] == "R"
        return max_col

def allocate_seats(seats, allocated_seats):
    for seat in seats:
        row_slice = slice(7)
        col_slice = slice(7,11)
        allocated_seats[get_row_num(seat[row_slice])][get_col_num(seat[col_slice])] = True

def find_unallocated_seat_id(allocated_seats):
    # Cannot be row 0 or 127
    for row in range(1,127):
        for col in range(8):
            if not allocated_seats[row][col]:
                return row * 8 + col

#with open("test.txt", "r") as file:
with open("Q5input.txt", "r") as file:
    seats = file.readlines()

allocated_seats = [[False for x in range(8)] for y in range(128)]
allocate_seats(seats,allocated_seats)
#print(f"Seat Id is: {get_seat_id(seats[0])}")
print(f"2020 Question 5B: My Seat ID = {find_unallocated_seat_id(allocated_seats)}")