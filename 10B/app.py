"""
Day 10: Adapter Array
"""
#with open("test.txt", "r") as file:
with open("Q10input.txt", "r") as file:
    data = file.readlines()
    adapters = [int(number_str.strip()) for number_str in data]
adapters.sort()
print(adapters)

def get_distinct_adapter_count(adapters):
    current_jolt1_differences = 0
    count3_jolt1_differences = 0
    count2_jolt1_differences = 0
    count1_jolt1_differences = 0
    for i in range(0,len(adapters)-1):
        current = adapters[i]
        next = adapters[i+1]
        if i == 0:
            if current == 1:
                current_jolt1_differences += 1

        print(f"{current} - {next}")
        if next - current == 1:
            current_jolt1_differences += 1
        elif next - current == 3:
            if current_jolt1_differences > 0:
                current_jolt1_differences -= 1
            print(f"Current jolt1 differences = {current_jolt1_differences}")
            if current_jolt1_differences == 1:
                count1_jolt1_differences += 1
            elif current_jolt1_differences == 2:
                count2_jolt1_differences += 1
            elif current_jolt1_differences == 3:
                count3_jolt1_differences += 1
            current_jolt1_differences = 0
        else:
            print(f"Something went wrong - unexpected jolt difference: {next} - {current}")

        if current_jolt1_differences == 4:
            print("Add count3 jolt1 difference")
            count3_jolt1_differences += 1
            current_jolt1_differences = 1

    print(f"Count of 1 Jolt difference = {count1_jolt1_differences}, Count of 2 Jolt difference = {count2_jolt1_differences}, Count of 3 Jolt difference = {count3_jolt1_differences}")
    
    # Set of 3 1Jolt Diffs have 7 different combinations, Set of 2 1Jolt Diff 4 combinations, 1Jolt Diff has 2 combinations (either off or on)
    # So answers is: 7^count3jolt1Diffs * 4^count2jolt1Diffs * 2^count1joltDiffs
    return 7**count3_jolt1_differences * 4**count2_jolt1_differences * 2**count1_jolt1_differences

print(f"2020 Question 10B: Total Distinct Possible Adapter Ways = {get_distinct_adapter_count(adapters)}")