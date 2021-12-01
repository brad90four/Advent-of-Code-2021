with open("./day1_part1_input.txt") as f:
    input_list = f.readlines()

modified_list = []
try:
    for i in range(len(input_list)):
#    for i in range(0, 11):
        j = i + 1
        k = i + 2
        part_sum = int(input_list[i]) + int(input_list[j]) + int(input_list[k])
#        print(f"{input_list[i]}")
#        print(f"{input_list[j]}")
#        print(f"{input_list[k]}")
        modified_list.append(part_sum)
except IndexError:
    pass

# print(modified_list[0:11])

increase = 1
for line_index in range(len(modified_list)):
    try:
        if modified_list[line_index + 1] > modified_list[line_index]:
            increase += 1
    except IndexError:
        pass

print(increase)
# 1151 is wrong, too high
