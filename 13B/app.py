"""
Day 13: Shuttle Search
"""
#with open("test3.txt", "r") as file:
with open("Q13input.txt", "r") as file:
    data = file.readlines()
    # data[0] is NOT required for this question
    # get the bus ids into list from the data(the 2nd row) - include the 'x's this time
    bus_data = [id for id in data[1].strip().split(",")]

print(bus_data)

# This function ok for small tests - but for actual input it did not finish to calculate
def get_first_buses_aligned_time_slow(bus_data):
    # assume the bus data will never start with an 'x'
    current_attempt = 0
    found_result = False
    while not found_result:
        first = True
        current_attempt += 1
        all_good = True
        for bus_id in bus_data:
            if first:
                first = False
                current_time = int(bus_id) * current_attempt
                current_offset = 0
            else:
                current_offset += 1
                if bus_id == 'x':
                    continue
                else:
                    if (current_time + current_offset) % int(bus_id) != 0:
                        all_good = False
                        break
        if all_good:
            found_result = True

    return current_time

# Much faster algorithm - multiply the step size to ensure previous factors still fit
def get_first_buses_aligned_time_fast(bus_data):
    # assume the bus data will never start with an 'x'
    current_step_size = int(bus_data[0])
    current_time = 0
    current_bus_index = 1
    while current_bus_index < len(bus_data):
        bus_id = bus_data[current_bus_index]
        if bus_id == 'x':
            current_bus_index += 1
        else:
            print(f"Current time = {current_time}, bus index = {current_bus_index}")
            if (current_time + current_bus_index) % int(bus_id) == 0:
                current_step_size = current_step_size * int(bus_id)
                current_bus_index += 1
            else:
                current_time += current_step_size
    return current_time

print(f"2020 Question 13B: First Bus Aligned Time = {get_first_buses_aligned_time_fast(bus_data)}")