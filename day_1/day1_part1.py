with open("./day1_part1_input.txt") as f:
    input_list = f.readlines()


increase = 1
for line_index in range(len(input_list)):
    try:
        if input_list[line_index + 1] > input_list[line_index]:
            increase += 1
    except IndexError:
        pass

print(increase)
