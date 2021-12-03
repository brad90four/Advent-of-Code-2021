import os

file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])  # windows
# _dir = "/".join(file_path.split("/")[0:-1])  # linux
os.chdir(_dir)

with open("day3_input.txt") as f:
    input_list = f.readlines()

_length = len(input_list)


def bit_values(input_list):
    bit_values = [0 for _ in range(len(input_list[0]) - 1)]
    for i in range(_length):
        line = input_list[i].replace("\n", "")
        bit_pos = 0
        for bit in line:
            bit_values[bit_pos] += int(bit)
            bit_pos += 1
    print(bit_values)
    return bit_values


def bit_criteria(bit_values):
    most_common = []
    least_common = []
    for bit in bit_values:
        if bit >= _length * 0.5:
            most_common.append("1")
            least_common.append("0")
        else:
            most_common.append("0")
            least_common.append("1")

    print(f"{most_common = }\n{least_common = }")
    return most_common, least_common


bit_criteria(bit_values(input_list))

def filter(list, mode):
    if mode == "oxygen":
        for i in range(_length):
            line = input_list[i].replace("\n", "")
            bit_pos = 0
            for bit in line:

