import os

file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])
os.chdir(_dir)

with open("day2_input.txt") as f:
    input_list = f.readlines()

distance = 0
depth = 0
aim = 0
for line in input_list:
    direction, magnitude = line.split()
    if direction == "forward":
        distance += int(magnitude)
        depth += aim * int(magnitude)
    elif direction == "down":
        aim += int(magnitude)
    else:
        aim -= int(magnitude)

print(f"{distance = }, {depth = }")
print(f"{distance * depth}")