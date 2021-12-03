import os

file_path = __file__
# _dir = "\\".join(file_path.split("\\")[0:-1])
_dir = "/".join(file_path.split("/")[0:-1])
os.chdir(_dir)

with open("day3_input.txt") as f:
    input_list = f.readlines()

_length = len(input_list)
bitsum1 = 0

# for line in input_list:
#     for bit in line.replace("\n", ""):
#         bitsum += int(bit)
#     print(f"{bitsum = }")

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
    ]

for i in range(11):
    # line = input_list[i].replace("\n", "")
    line = test_input[i].replace("\n", "")
    print(f"{line = }")
    partbit = []
    for column in range(len(line)):
        partbit.append(0)
        print(f"{partbit =}")
        partbit[column] += int(line[column])
        print(f"{partbit = }")

print(partbit)