import os

file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])  # windows
# _dir = "/".join(file_path.split("/")[0:-1])  # linux
os.chdir(_dir)

with open("day3_input.txt") as f:
    input_list = f.readlines()


_length = len(input_list)


def bit_count(input_list: list[str]) -> list[int]:
    """Count the total value of each bit position from the input.

    Args:
        input_list (list[str]): The provided source for the puzzle.

    Returns:
        bit_count_list (list[int]): A list of the total values of the input list bit positions.

    """
    bit_count_list = [
        0 for _ in range(len(input_list[0]) - 1)
    ]  # -1 to handle new line character
    for i in range(_length):
        line = input_list[i].replace("\n", "")
        bit_pos = 0
        for bit in line:
            bit_count_list[bit_pos] += int(bit)
            bit_pos += 1
    return bit_count_list


def reduce_bit_count(bit_count_list: list[int]) -> list[int]:
    """Determine the most common bit value is 1 or 0.

    This is done by checking if the bit position value is greater than or equal to
    half of the length of the input list.

    Args:
        bit_count_list (list[int]): A list of the total values of the input list bit positions.

    Returns:
        bit_count_list (list[int]): A list of the greatest common bit values.

    """
    bit_pos = 0
    for bit in bit_count_list:
        # if bit >= 0.5 * len(test_input):
        if bit >= 0.5 * _length:
            bit_count_list[bit_pos] = 1
            bit_pos += 1
        else:
            bit_count_list[bit_pos] = 0
            bit_pos += 1
    return bit_count_list


def gamma_epsilon(reduced_list: list[int]) -> tuple[int, int]:
    """Determine the integer value of the input binary code.

    Args:
        reduced_list (list[str]): A list of the greatest common bit values.

    Returns:
        gamma (int): An integer value for the "gamma" rate.
        epsilon (int): An integer value for the "epsilon" rate.

    """
    gamma_list = "".join([str(x) for x in reduced_list])
    gamma = int(gamma_list, 2)
    epsilon_list = "".join(["0" if x == "1" else "1" for x in gamma_list])
    epsilon = int(epsilon_list, 2)
    return gamma, epsilon


if __name__ == "__main__":
    gamma, epsilon = gamma_epsilon(reduce_bit_count(bit_count(input_list)))
    print(f"Power level: {gamma * epsilon}")
    # correct: 4118544
