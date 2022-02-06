"""
Day 12: Rain Risk
"""

#with open("test.txt", "r") as file:
with open("Q12input.txt", "r") as file:
    data = file.readlines()
    instructions = [line.strip() for line in data]

def get_manhatten_distance(instructions):
    ship_north_south_pos = 0
    ship_east_west_pos = 0
    # waypoint starting position is 10 units east, 1 unit north
    waypoint_north_south_pos = 1
    waypoint_east_west_pos = 10

    for instruction in instructions:
        action = instruction[0]
        units = int(instruction[1:])
        # print(f"action: {action}, units: {units}")

        match action:
            case 'L':
                change_direction = units/90
                match change_direction:
                    case 1:
                        swap = waypoint_north_south_pos
                        waypoint_north_south_pos = waypoint_east_west_pos
                        waypoint_east_west_pos = swap
                        waypoint_east_west_pos *= -1
                    case 2:
                        waypoint_north_south_pos *= -1
                        waypoint_east_west_pos *= -1
                    case 3:
                        swap = waypoint_north_south_pos
                        waypoint_north_south_pos = waypoint_east_west_pos
                        waypoint_east_west_pos = swap
                        waypoint_north_south_pos *= -1
                    case _:
                        print(f"Something went wrong - invalid change L direction = {change_direction}")
            case 'R':
                change_direction = units/90
                match change_direction:
                    case 1:
                        swap = waypoint_north_south_pos
                        waypoint_north_south_pos = waypoint_east_west_pos
                        waypoint_east_west_pos = swap
                        waypoint_north_south_pos *= -1
                    case 2:
                        waypoint_north_south_pos *= -1
                        waypoint_east_west_pos *= -1
                    case 3:
                        swap = waypoint_north_south_pos
                        waypoint_north_south_pos = waypoint_east_west_pos
                        waypoint_east_west_pos = swap
                        waypoint_east_west_pos *= -1
                    case _:
                        print(f"Something went wrong - invalid change R direction = {change_direction}")
            case 'N':
                waypoint_north_south_pos += units
            case 'E':
                waypoint_east_west_pos += units
            case 'S':
                waypoint_north_south_pos -= units
            case 'W':
                waypoint_east_west_pos -= units
            case 'F':
               ship_north_south_pos += units * waypoint_north_south_pos
               ship_east_west_pos += units * waypoint_east_west_pos
            case _:
                print(f"Something went wrong - invalid action = {action}")
    print(f"Position = {ship_north_south_pos} North/South, {ship_east_west_pos} East/West")
    return abs(ship_north_south_pos) + abs(ship_east_west_pos)

# print(seating_map)
print(f"2020 Question 12B: Manhatten Distance = {get_manhatten_distance(instructions)}")