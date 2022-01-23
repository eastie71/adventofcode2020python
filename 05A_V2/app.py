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

def get_seat_id(seat):
    row_slice = slice(7)
    row_num = get_row_num(seat[row_slice])
    #print(f"row num = {row_num}")
    col_slice = slice(7,11)
    col_num = get_col_num(seat[col_slice])
    #print(f"col num = {col_num}")

    return row_num * 8 + col_num

def get_highest_seat_id(seats):
    highest_seat_id = 0
    for seat in seats:
        seat_id = get_seat_id(seat)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id

#with open("test.txt", "r") as file:
with open("Q5input.txt", "r") as file:
    seats = file.readlines()

#print(f"Seat Id is: {get_seat_id(seats[0])}")
print(f"2020 Question 5A: Highest Seat ID = {get_highest_seat_id(seats)}")