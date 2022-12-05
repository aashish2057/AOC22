import fileinput

calories = []
with fileinput.input(files=("input1-1.txt")) as file:
    for line in file:
        calories.append(line)

elves = []
highest = 0
for index in range(len(calories)):
    total = 0
    while index < len(calories) and calories[index] != "\n":
        total += int(calories[index])
        index += 1
    if total > highest:
        highest = total
    elves.append(total)

elves.sort()
print(sum(elves[len(elves)-3:]))
        