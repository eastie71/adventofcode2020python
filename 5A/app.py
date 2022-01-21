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