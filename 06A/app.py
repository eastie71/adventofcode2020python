"""
Day 6: Custom Customs
"""
def get_unique_answers(answer_groups):
    answers = []
    for group in answer_groups:
        # use a "set" to get unique answers - set will break string into individual chars -ie. "abc" -> "a","b","c"
        answers.append(set(group))
    return answers

def get_total_yes_answers(answers):
    total_yes_answers = 0
    for answer in answers:
        total_yes_answers += len(answer)
    return total_yes_answers

#with open("test.txt", "r") as file:
with open("Q6input.txt", "r") as file:
    data = file.read().split("\n\n")
answer_groups = [line.replace("\n","") for line in data]
unique_answers = get_unique_answers(answer_groups)

#print(f"Seat Id is: {get_seat_id(seats[0])}")
print(f"2020 Question 6A: Total YES answers = {get_total_yes_answers(unique_answers)}")