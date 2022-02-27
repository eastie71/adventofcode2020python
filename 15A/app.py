"""
Day 15: Rambunctious Recitation
"""
test_numbers1 = [0,3,6]
test_numbers2 = [3,1,2]

puzzle_numbers = [13, 16, 0, 12, 15, 1]

def get_result_for_number_game_for_turn(numbers, max_turn_number):
    seen_numbers = {}
    current_turn_number = 1
    current_spoken_number = 0

    # Start with the initial number list - assume each number is unique
    for number in numbers:
        seen_numbers[number] = {"previous": current_turn_number, "last": -1}
        current_turn_number += 1
        #last_spoken_number = number
    
    #print(f"For turn: {current_turn_number}, number = {last_spoken_number}, seen = {seen_numbers}")

    for current_turn_number in range(current_turn_number, max_turn_number):
        if current_spoken_number not in seen_numbers:
            seen_numbers[current_spoken_number] = {"previous": current_turn_number, "last": -1}
            current_spoken_number = 0
        elif seen_numbers[current_spoken_number]["last"] == -1:  
            seen_numbers[current_spoken_number]["last"] = current_turn_number
            current_spoken_number = seen_numbers[current_spoken_number]["last"] - seen_numbers[current_spoken_number]["previous"]
        else:
            seen_numbers[current_spoken_number]["previous"] = seen_numbers[current_spoken_number]["last"]
            seen_numbers[current_spoken_number]["last"] = current_turn_number
            current_spoken_number = seen_numbers[current_spoken_number]["last"] - seen_numbers[current_spoken_number]["previous"]
        #print(f"For turn: {current_turn_number}, number = {last_spoken_number}, seen = {seen_numbers}")
    
    return current_spoken_number

print(f"2020 Question 15A: 2020th value from game is = {get_result_for_number_game_for_turn(test_numbers2, 2020)}")