"""
Day 10: Adapter Array
"""
#with open("test.txt", "r") as file:
with open("Q10input.txt", "r") as file:
    data = file.readlines()
    adapters = [int(number_str.strip()) for number_str in data]
adapters.sort()
print(adapters)

def get_jolt_differences(adapters):
    jolt1_difference_count = 0
    jolt3_difference_count = 0
    for i in range(0,len(adapters)-1):
        current = adapters[i]
        next = adapters[i+1]
        if i == 0:
            if current == 1:
                jolt1_difference_count += 1
            elif current == 3:
                jolt3_difference_count += 1
        if next - current == 1:
            jolt1_difference_count += 1
        elif next - current == 3:
            jolt3_difference_count += 1
        else:
            print(f"Something went wrong - unexpected jolt difference: {next} - {current}")
    # Alway add the last difference as a jolt3 difference
    jolt3_difference_count += 1
    print(f"Total 1 Jolt difference = {jolt1_difference_count}, Total 3 Jolt difference = {jolt3_difference_count}")
    return jolt1_difference_count * jolt3_difference_count

print(f"2020 Question 10A: Total Jolt Differences = {get_jolt_differences(adapters)}")