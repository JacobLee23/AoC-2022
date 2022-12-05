# 2022 Day 5

import re


TXT_PATH = "day5.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = file.readlines()


def get_columns(arr, a: int = None, b: int = None):
    crates = [
        [x[i + 1] for i in range(0, len(x), 4)]
        for x in arr.__getitem__(slice(a, b))
    ]
    stacks = [
        [crates[i][j] for i in range(len(crates))]
        for j in range(len(crates[0]))
    ]
    columns = [[x for x in reversed(c) if x != " "] for c in stacks]

    return columns


def get_moves(arr, a: int = None, b: int = None):
    moves = [
        map(int, re.findall(r"\d+", x))
        for x in arr.__getitem__(slice(a, b))
    ]

    return moves


def part1(arr=DATA):
    columns = get_columns(arr, None, 8)
    moves = get_moves(arr, 10, None)

    for n, a, b in moves:
        columns[b - 1] += reversed(columns[a - 1][-n:])
        del columns[a - 1][-n:]

    return "".join(x[-1] for x in columns if x)


def part2(arr=DATA):
    columns = get_columns(arr, None, 8)
    moves = get_moves(arr, 10, None)

    for n, a, b in moves:
        columns[b - 1] += columns[a - 1][-n:]
        del columns[a - 1][-n:]

    return "".join(x[-1] for x in columns if x)


if __name__ == "__main__":
    print(part1())
    print(part2())
