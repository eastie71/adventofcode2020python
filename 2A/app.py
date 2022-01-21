"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
def get_valid_password_count(entries):
    valid_password_count = 0
    for line in entries:
        min_count = int(line.split('-')[0])
        max_count = int(line.split('-')[1].split(' ')[0])
        char_required = line.split('-')[1].split(' ')[1].split(':')[0]
        password = line.split(':')[1].strip()

        char_count = password.count(char_required)
        if (char_count >= min_count and char_count <= max_count):
            valid_password_count += 1
    return valid_password_count

with open("Q2input.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]
print(f"2020 Question 2A: Total Valid Passwords = {get_valid_password_count(entries)}")