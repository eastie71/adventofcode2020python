"""
Day 12: Rain Risk
"""
#with open("test.txt", "r") as file:
with open("Q13input.txt", "r") as file:
    data = file.readlines()
    # get the requested arrival time from the 1st line
    arrival_time = int(data[0].strip())
    # get the bus ids into list from the data(the 2nd row) (ignoring the 'x' bus ids) and convert to integers
    bus_data = [int(id) for id in data[1].strip().split(",") if id != 'x']

print(arrival_time)
print(bus_data)

def get_wait_time_for_bus(id, arrival_time):
    next_bus_time = (arrival_time // id + 1) * id
    return next_bus_time - arrival_time

def get_bus_id_result(bus_data, arrival_time):
    best_wait_time = -1
    for bus_id in bus_data:
        wait_time = get_wait_time_for_bus(bus_id, arrival_time)
        if best_wait_time == -1 or wait_time < best_wait_time:
            best_wait_time = wait_time
            best_bus_id = bus_id
    print(f"Best bus id = {best_bus_id}, with wait time = {best_wait_time}")
    return best_wait_time*best_bus_id

# print(seating_map)
print(f"2020 Question 13A: Bus Id Result = {get_bus_id_result(bus_data, arrival_time)}")