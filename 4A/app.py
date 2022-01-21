"""
Day 4: Passport Processing
"""
def get_valid_passport_count(passports, attributes_required):
    valid_count = 0
    for passport in passports:
        passport_valid = True
        for attrubute in attributes_required:
            if len(passport[attrubute]) == 0:
                passport_valid = False
                break
        if passport_valid:
            valid_count += 1
    return valid_count

def get_attribute(line, name):
    if line.count(name) == 0:
        return ""
    return line.split(f"{name}:")[1].split(' ')[0]

#with open("test.txt", "r") as file:
with open("Q4input.txt", "r") as file:
    data = file.read().split("\n\n")

passports = []
for line in data:
    line = line.replace("\n", " ")
    byr = get_attribute(line, "byr")
    iyr = get_attribute(line, "iyr")
    
    passports.append({"byr": get_attribute(line, "byr"),
                        "iyr": get_attribute(line, "iyr"),
                        "eyr": get_attribute(line, "eyr"),
                        "hgt": get_attribute(line, "hgt"),
                        "hcl": get_attribute(line, "hcl"),
                        "ecl": get_attribute(line, "ecl"),
                        "pid": get_attribute(line, "pid"),
                        "cid": get_attribute(line, "cid"),
                        })

data_types_required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

print(f"2020 Question 4A: Number of Valid Passports = {get_valid_passport_count(passports, data_types_required)}")