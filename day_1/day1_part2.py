import os

file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])
print(f"{_dir = }")
os.chdir(_dir)

with open("day1_part1_input2.txt") as f:
    input_list = f.readlines()

# testing list
# input_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

modified_list = []
try:
    for i in range(len(input_list)):
        j = i + 1
        k = i + 2
        part_sum = int(input_list[i]) + int(input_list[j]) + int(input_list[k])
        modified_list.append(part_sum)
except IndexError:
    pass


increase = 0
for line_index in range(len(modified_list)):
    try:
        if modified_list[line_index + 1] > modified_list[line_index]:
            increase += 1
    except IndexError:
        pass

print(increase)
