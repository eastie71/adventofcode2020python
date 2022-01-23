"""
Day 8: Handheld Halting
"""
#with open("test.txt", "r") as file:
with open("Q8input.txt", "r") as file:
    data = file.readlines()
instructions = []
for line in data:
    instruction_data = line.strip().split(" ")
    instruction_line = {"operation": instruction_data[0], "value": int(instruction_data[1].strip())}
    instructions.append(instruction_line)    

print(instructions)


def get_accumulated_value(instructions):
    accumulated_value = 0
    instruction_read = [False for i in range(len(instructions))]
    current_pos = 0
    error = False
    while (not instruction_read[current_pos]):
        instruction_read[current_pos] = True
        current_instruction = instructions[current_pos]
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
    if (not error and current_pos > 0 and current_pos < len(instructions)):
        return accumulated_value

print(f"2020 Question 8A: Accumulater value = {get_accumulated_value(instructions)}")