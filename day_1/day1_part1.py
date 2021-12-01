import os

file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])
os.chdir(_dir)

with open("./day1_part1_input2.txt") as f:
    input_list = f.readlines()


increase = 1
for line_index in range(len(input_list)):
    try:
        if input_list[line_index + 1] > input_list[line_index]:
            increase += 1
    except IndexError:
        pass

print(increase)
