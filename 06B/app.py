"""
Day 6: Custom Customs
"""
def get_unique_answers(answer_groups):
    unique_answers = []
    for answer_group in answer_groups:
        # initialise intersection with FIRST answer group
        intersection = answer_group[0]
        for answers in answer_group:
            intersection = [value for value in answers if value in intersection]
        unique_answers.append(intersection)
    return unique_answers

# See also https://replit.com/@eastie/SetsPlay#main.py
def get_split_answer_groups(answer_groups):
    split_answer_groups = []
    for groups in answer_groups:
        # split up the individual answers in each group
        split_answer_group = []
        for group in groups:
            # split out the individual answers ie. ["abc"] -> ["a","b","c"]
            split_answers = [answer for answer in group]
            split_answer_group.append(split_answers)
        split_answer_groups.append(split_answer_group)
    return split_answer_groups

def get_total_yes_answers(answers):
    total_yes_answers = 0
    for answer in answers:
        total_yes_answers += len(answer)
    return total_yes_answers

#with open("test.txt", "r") as file:
with open("Q6input.txt", "r") as file:
    data = file.read().split("\n\n")

answer_groups = [line.split("\n") for line in data]
split_answer_groups = get_split_answer_groups(answer_groups)
#print(split_answer_groups)
unique_answers = get_unique_answers(answer_groups)
#print(unique_answers)
print(f"2020 Question 6B: Total YES answers = {get_total_yes_answers(unique_answers)}")