import os

import numpy as np
import pandas as pd


file_path = __file__
_dir = "\\".join(file_path.split("\\")[0:-1])  # windows
# _dir = "/".join(file_path.split("/")[0:-1])  # linux
os.chdir(_dir)

with open("day3_input.txt") as f:
    input_list = f.readlines()

array_list = [[x for x in line] for line in input_list]
df = pd.DataFrame(array_list)
df.drop(columns=df.columns[-1], axis=1, inplace=True)  # remove new line character
df = df.astype(int)
original_df = df

test_list = [
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
    "01010",
]

test_array = [[x for x in line] for line in test_list]
test_df = pd.DataFrame(test_array)
test_df = test_df.astype(int)


def filter_bits(dataframe, mode):
    _len = len(dataframe.index)

    bit_sum = []
    for col in dataframe:
        bit_sum.append(dataframe[col].sum())

    filter = []
    if mode == "oxygen":
        for item in bit_sum:
            if _len == 2:
                filter.append(1)
            elif item >= 0.5 * _len:
                filter.append(1)
            else:
                filter.append(0)
        return filter
    elif mode == "co2":
        for item in bit_sum:
            if _len == 2:
                filter.append(0)
            elif item >= 0.5 * _len:
                filter.append(0)
            else:
                filter.append(1)
        return filter


def find_value(dataframe, mode):
    for i in range(len(dataframe.columns)):
        _len = len(dataframe.index)
        if _len > 1:
            filter_list = filter_bits(dataframe, mode)
            dataframe = dataframe[dataframe[i] == filter_list[i]]
            print(dataframe.head())
        else:
            break
    return int("".join([str(val) for val in dataframe.iloc[0]]), 2)


if __name__ == "__main__":
    o2 = find_value(df, "oxygen")
    co2 = find_value(original_df, "co2")
    print(f"{o2 = }\n{co2 = }\nLife Support: {o2 * co2}")
