"""
Day 4: Passport Processing
"""
import re

data_types_required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validate_passport_details(passport):
    valid = True
    for data_type in data_types_required:
        match data_type:
            case "byr":
                try:
                    year = int(passport["byr"])
                    if year < 1920 or year > 2002:
                        valid = False
                except:
                    valid = False
            case "iyr": 
                try:
                    year = int(passport["iyr"])
                    if year < 2010 or year > 2020:
                        valid = False
                except:
                    valid = False
            case "eyr": 
                try:
                    year = int(passport["eyr"])
                    if year < 2020 or year > 2030:
                        valid = False
                except:
                    valid = False                    
            case "hgt": 
                try:
                    if passport["hgt"].count("cm") == 1:
                        height = int(passport["hgt"].split("cm")[0])
                        if height < 150 or height > 193:
                            valid = False
                    elif passport["hgt"].count("in") == 1:
                        height = int(passport["hgt"].split("in")[0])
                        if height < 50 or height > 76:
                            valid = False
                    else:
                        valid = False
                except:
                    valid = False    
            case "hcl": 
                valid = False
                if passport["hcl"][0] == "#" and len(passport["hcl"]) == 7:
                    if re.search(r"[#a-fA-F0-9]+$", passport["hcl"]):
                        valid = True
            case "ecl": 
                valid = False
                for ecl in valid_ecl:
                    if passport["ecl"] == ecl:
                        valid = True
                        break
            case "pid": 
                try:
                    if len(passport["pid"]) != 9 or re.search(r"[0-9]+$", passport["pid"]) == None:
                        valid = False
                except:
                    valid = False 
            case _:
                break
        if not valid:
            return False         
    return valid

def get_valid_passport_count(passports, attributes_required):
    valid_count = 0
    for passport in passports:
        passport_valid = True
        for attrubute in attributes_required:
            if len(passport[attrubute]) == 0:
                passport_valid = False
                break
        if passport_valid:
            if validate_passport_details(passport):
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

print(f"2020 Question 4B: Number of Valid Passports = {get_valid_passport_count(passports, data_types_required)}")