"""
Day 3: Toboggan Trajectory
"""
def get_trees_hit_count(terrain):
    hit_count = 0
    terrain_width = len(terrain[0])
    current_y_pos = 0
    current_x_pos = 0
    while (current_y_pos < len(terrain)-1):
        current_y_pos += 1
        current_x_pos += 3
        current_x_pos %= terrain_width
        if terrain[current_y_pos][current_x_pos] == "#":
            hit_count += 1
    return hit_count

with open("Q3input.txt", "r") as file:
    terrain = [line.strip() for line in file.readlines()]
print(f"2020 Question 3A: Total Trees Hit = {get_trees_hit_count(terrain)}")