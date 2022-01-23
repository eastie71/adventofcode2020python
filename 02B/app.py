"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
def get_valid_password_count(entries):
    valid_password_count = 0
    for line in entries:
        position1 = int(line.split('-')[0])-1
        position2 = int(line.split('-')[1].split(' ')[0])-1
        char_required = line.split('-')[1].split(' ')[1].split(':')[0]
        password = line.split(':')[1].strip()

        if (position1 >= 0 and position2 >= 0 and position1 < len(password) and position2 < len(password)):
            if ((password[position1] == char_required and password[position2] != char_required) or
                (password[position1] != char_required and password[position2] == char_required)):
                valid_password_count += 1
    return valid_password_count

with open("Q2input.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]
print(f"2020 Question 2B: Total Valid Passwords = {get_valid_password_count(entries)}")