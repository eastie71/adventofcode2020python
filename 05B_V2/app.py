"""
Day 5: Binary Boarding
"""
def get_row_num(seat):
    # convert to binary string eg. FBFBBFF -> 0101100
    translation = seat.maketrans("FB","01")
    binary_row_num = seat.translate(translation)
    # convert the binary string to a decimal to get the row number eg. 0101100 -> 44
    return int(binary_row_num,2)

def get_col_num(seat):
    # convert to binary string eg. RRL -> 110
    translation = seat.maketrans("LR", "01")
    binary_col_num = seat.translate(translation)
    # convert binary string to decimal to get col number eg. 110 -> 6
    return int(binary_col_num,2)

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