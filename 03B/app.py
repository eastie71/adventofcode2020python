"""
Day 3: Toboggan Trajectory
"""
def get_trees_hit_count(terrain, right_amount, down_amount):
    hit_count = 0
    terrain_width = len(terrain[0])
    current_y_pos = 0
    current_x_pos = 0
    while (current_y_pos < len(terrain)-1):
        current_y_pos += down_amount
        current_x_pos += right_amount
        current_x_pos %= terrain_width
        if terrain[current_y_pos][current_x_pos] == "#":
            hit_count += 1
    return hit_count

with open("Q3input.txt", "r") as file:
    terrain = [line.strip() for line in file.readlines()]

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
answer = 1
for slope in slopes:
    hit_count = get_trees_hit_count(terrain,slope[0],slope[1])
    print(f"Slope: {slope} hit count is: {hit_count}")
    answer *= hit_count
print(f"2020 Question 3B: Answer = {answer}")