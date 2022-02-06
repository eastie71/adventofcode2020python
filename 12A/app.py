"""
Day 12: Rain Risk
"""

#with open("test.txt", "r") as file:
with open("Q12input.txt", "r") as file:
    data = file.readlines()
    instructions = [line.strip() for line in data]

def get_manhatten_distance(instructions):
    north_south_pos = 0
    east_west_pos = 0

    current_direction = 1 # north = 0, east = 1, south = 2, west = 3
    for instruction in instructions:
        action = instruction[0]
        units = int(instruction[1:])
        # print(f"action: {action}, units: {units}")

        match action:
            case 'L':
                current_direction -= units/90
                if current_direction < 0:
                    current_direction += 4
            case 'R':
                current_direction += units/90
                if current_direction > 3:
                    current_direction -= 4
            case 'N':
                north_south_pos += units
            case 'E':
                east_west_pos += units
            case 'S':
                north_south_pos -= units
            case 'W':
                east_west_pos -= units
            case 'F':
                match current_direction:
                    case 0:
                        north_south_pos += units
                    case 1:
                        east_west_pos += units
                    case 2:
                        north_south_pos -= units
                    case 3:
                        east_west_pos -= units
                    case _:
                        print(f"Something went wrong - invalid direction = {current_direction}")
            case _:
                print(f"Something went wrong - invalid action = {action}")
    print(f"Position = {north_south_pos} North/South, {east_west_pos} East/West")
    return abs(north_south_pos) + abs(east_west_pos)

# print(seating_map)
print(f"2020 Question 12A: Manhatten Distance = {get_manhatten_distance(instructions)}")