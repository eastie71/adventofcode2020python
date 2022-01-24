"""
Day 9: Encoding Error
"""
#with open("test.txt", "r") as file:
with open("Q9input.txt", "r") as file:
    data = file.readlines()
    numbers = [int(number_str.strip()) for number_str in data]

#print(numbers)

def get_first_failed_number(numbers, preamble_length):
    start_pos = 0
    end_pos = preamble_length
    while (end_pos < len(numbers)):
        found = False
        current_number = numbers[end_pos]
        for i in range(start_pos, end_pos):
            for j in range(i+1, end_pos):
                if numbers[i] + numbers[j] == current_number:
                    found = True
                    break
            if found:
                break
        if not found: # then the number failed (is invalid)
            return current_number
        end_pos += 1
        start_pos += 1
    print("Could not find an invalid number!")
    return None

def get_encryption_weakness_number(numbers, failed_number):
    start_pos = 0
    current_total = 0
    while start_pos < len(numbers):
        current_total = numbers[start_pos]
        end_pos = start_pos + 1
        while current_total < failed_number:
            current_total += numbers[end_pos]
            if current_total == failed_number:
                # we got it
                lowest = -1
                highest = -1
                for i in range(start_pos, end_pos):
                    if numbers[i] < lowest or lowest == -1:
                        lowest = numbers[i]
                    if numbers[i] > highest:
                        highest = numbers[i]
                print(f"Lowest = {lowest}, Highest = {highest}")
                return lowest + highest
            end_pos += 1
        start_pos += 1
    print("Failed to find the encryption weakness!")
    return None

failed_number = get_first_failed_number(numbers, 25)
print(f"2020 Question 9A: Encryption Weakness Number from XMAS numbers list = {get_encryption_weakness_number(numbers, failed_number)}")