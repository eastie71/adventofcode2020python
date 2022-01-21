with open("Q1input.txt", "r") as file:
    entries = [int(line.strip()) for line in file.readlines()]

# entries = [1721,979,366,299,675,1456]
found_it = False
for index1 in range(0,len(entries)):
    for index2 in range(0,len(entries)):
        if entries[index1] + entries[index2] == 2020:
            found_it = True
            break
    if found_it:
        break

if found_it:
    print(f"2020 Question 1A: Entry values are {entries[index1]} and {entries[index2]}, hence answer is: {entries[index1]*entries[index2]}")