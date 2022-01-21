"""
Day 7: Handy Haversacks
"""
#with open("test.txt", "r") as file:
with open("Q7input.txt", "r") as file:
    data = file.readlines()
bag_data = []
for line in data:
    bag_data_line = line.split(" contain ")
    # The color is just the color - ie. remove the " bags" from the color name
    bag_dict_line = {"color": bag_data_line[0].replace(" bags",""), "contains": bag_data_line[1].strip()}
    bag_data.append(bag_dict_line)    

def find_bag_with_color(bag_data, bag_color):
    for bag in bag_data:
        if bag["color"] == bag_color:
            return bag
    return None
#    return next((bag for bag in bag_data if bag["color"] == bag_color), None)

def get_total_bags_inside(selected_bag_color):
    current_bag = find_bag_with_color(bag_data, selected_bag_color)
    current_bag_tokens = current_bag["contains"].split(" ")
    bag_count_total = 0
    for index in range(0,len(current_bag_tokens)):
        if current_bag_tokens[index].isnumeric():
            bag_count = int(current_bag_tokens[index])
            # Assume next 2 tokens make up the bag color
            bag_color = f"{current_bag_tokens[index+1]} {current_bag_tokens[index+2]}"
            bag_count_total += bag_count + bag_count*(get_total_bags_inside(bag_color))
            index += 2
    return bag_count_total

print(f"2020 Question 7A: Number of Bags inside a 'Shiny Gold Bag' = {get_total_bags_inside('shiny gold')}")
#print(bags_counted)