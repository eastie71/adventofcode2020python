"""
Day 8: Handheld Halting
"""
#with open("test.txt", "r") as file:
with open("Q8input.txt", "r") as file:
    data = file.readlines()
instructions = []
for line in data:
    instruction_data = line.strip().split(" ")
    # The color is just the color - ie. remove the " bags" from the color name
    instruction_line = {"operation": instruction_data[0], "value": int(instruction_data[1].strip())}
    instructions.append(instruction_line)    

#print(instructions)

def get_accumulated_value_of_valid_instructions(instructions):
    accumulated_value = 0
    instruction_read = [False for i in range(len(instructions))]
    current_pos = 0
    error = False
    # print(f"start get value, length = {len(instructions)}")
    while (current_pos >= 0 and current_pos < len(instructions) and not instruction_read[current_pos]):
        instruction_read[current_pos] = True
        current_instruction = instructions[current_pos]
        # print(f"pos: {current_pos} {current_instruction}")
        match current_instruction["operation"]:
            case "nop":
                current_pos += 1
            case "acc":
                accumulated_value += current_instruction["value"]
                current_pos += 1
            case "jmp":
                current_pos += current_instruction["value"]
            case _:
                print(f"Unexepected instruction type: {current_instruction['operation']}")
                error = True
    # if current_pos is at last instruction then we have a valid instructions list
    if (not error and current_pos == len(instructions)):
        return accumulated_value
    # otherwise not valid instruction list so return None
    return None

def get_correct_accumulated_value(instructions):
    index = 0
    for instruction in instructions:
        result = None
        # Swap the operation from nop => jmp and try to get value 
        if (instruction["operation"] == "nop"):
            instructions[index]["operation"] = "jmp"
            result = get_accumulated_value_of_valid_instructions(instructions)
            # set the operation back anyway
            instructions[index]["operation"] = "nop"
        elif (instruction["operation"] == "jmp"):
            instructions[index]["operation"] = "nop"
            result = get_accumulated_value_of_valid_instructions(instructions)
            # set the operation back anyway
            instructions[index]["operation"] = "jmp"
        index += 1
        if (result != None):
            return result
    print("Something went wrong - could not get valid instructions")
    return None

print(f"2020 Question 8B: Valid Instructions Accumulater value = {get_correct_accumulated_value(instructions)}")