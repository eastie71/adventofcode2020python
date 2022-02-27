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

def get_masked_address(mask, binary_string):
    masked_value = ""
    for j in range(0, len(mask)):
        match mask[j]:
            case '0':
                masked_value += binary_string[j]
            case _:
                if mask[j] != '1' and mask[j] != 'X':
                    print(f"Something went wrong - invalid mask value: {mask[j]}")
                    return None
                else:
                    masked_value += mask[j]
    return masked_value

def get_binary_address_value(masked_address, binary_string):
    current_binary_pos = len(binary_string) - 1
    new_binary_address = ""
    for i in range(0, len(masked_address)):
        if masked_address[i] == 'X':
            new_binary_address += binary_string[current_binary_pos]
            current_binary_pos -= 1
        else:
            new_binary_address += masked_address[i]
    return new_binary_address

def get_program_memory_sum(instructions):
    # program memory example - [{"10": 101}, {"12": 15}]
    program_memory = {}
    current_mask = ""
    for instruction in instructions:
        match instruction["type"]:
            case "mem":
                binary_string = get_binary_string(instruction["address"])
                # print(f"binary string = {binary_string}")
                binary_masked_address = get_masked_address(current_mask, binary_string)
                addresses_to_update_count = 2 ** binary_masked_address.count("X") 
                # print(f"address = {instruction['address']}, value = {int(masked_value,2)}")

                for j in range(0, addresses_to_update_count):
                    current_binary_string = get_binary_string(j)
                    binary_address_value = get_binary_address_value(binary_masked_address, current_binary_string) 
                    program_memory[int(binary_address_value,2)] = int(instruction["value"])

            case "mask":
                current_mask = instruction["value"]
    memory_total_value = 0
    for value in program_memory.values():
        memory_total_value += value
    return memory_total_value
               
# print(data)
instructions = setup_instructions(data)
# print(instructions)

print(f"2020 Question 14B: Memory Value Sum = {get_program_memory_sum(instructions)}")