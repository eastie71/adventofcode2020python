"""
Day 14: Docking Data
"""
MASK_SIZE = 36

#with open("test.txt", "r") as file:
with open("Q14input.txt", "r") as file:
    #data = file.readlines()
    data = [line.strip() for line in file.readlines()]

def setup_instructions(data):    
    instructions = []
    for line in data:
        line_type = line[:3]
        if line_type == 'mem':
            mem_address = line.split("[",1)[1].split("]",1)[0].strip()
            mem_value = line.split("=",1)[1].strip()
            instruction = {"type": "mem", "address": mem_address, "value": mem_value }
        elif line_type == 'mas':
            mask_value = line.split("=",1)[1].strip()
            instruction = {"type": "mask", "value": mask_value }
        else:
            print(f"Something went wrong - invalid line type: {line_type}")
            return None
        # print(f"instruction = {instruction}")
        instructions.append(instruction)
    return instructions

def get_binary_string(decimal_value):
    binary_value = bin(int(decimal_value)).replace("0b","")
    zero_padding = ""
    for i in range(0, MASK_SIZE - len(binary_value)):
        zero_padding += "0"
    return zero_padding + binary_value

def get_masked_value(mask, binary_string):
    masked_value = ""
    for j in range(0, len(mask)):
        match mask[j]:
            case 'X':
                masked_value += binary_string[j]
            case _:
                if mask[j] != '0' and mask[j] != '1':
                    print(f"Something went wrong - invalid mask value: {mask[j]}")
                    return None
                else:
                    masked_value += mask[j]
    return masked_value

def get_program_memory_sum(instructions):
    # program memory example - [{"10": 101}, {"12": 15}]
    program_memory = {}
    current_mask = ""
    for instruction in instructions:
        match instruction["type"]:
            case "mem":
                binary_string = get_binary_string(instruction["value"])
                # print(f"binary string = {binary_string}")
                binary_masked_value = get_masked_value(current_mask, binary_string)
                # print(f"address = {instruction['address']}, value = {int(masked_value,2)}")
                program_memory[instruction["address"]] = int(binary_masked_value,2)
            case "mask":
                current_mask = instruction["value"]
    memory_total_value = 0
    for value in program_memory.values():
        memory_total_value += value
    return memory_total_value
               
# print(data)
instructions = setup_instructions(data)
# print(instructions)

print(f"2020 Question 14A: Memory Value Sum = {get_program_memory_sum(instructions)}")