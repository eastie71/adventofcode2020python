"""
Day 7: Handy Haversacks
"""
#with open("test.txt", "r") as file:
with open("Q7input.txt", "r") as file:
    data = file.readlines()
bag_data = []
for line in data:
    bag_data_line = line.split(" contain ")
    # The [:-1] removes the last char from the string - in this case its the "s" character
    bag_dict_line = {"color": bag_data_line[0][:-1], "contains": bag_data_line[1].strip()}
    bag_data.append(bag_dict_line)
#print(bag_data)    

def get_total_bags(bag_color):
    for bag in bag_data:
        if bag_color in bag["contains"] and bag["color"] not in bags_counted:
            bags_counted.append(bag["color"])
            get_total_bags(bag["color"])
    return len(bags_counted)

bags_counted = []
print(f"2020 Question 7A: Number of Bags containing 'Shiny Gold Bag' = {get_total_bags('shiny gold bag')}")
#print(bags_counted)