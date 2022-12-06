# 2022 Day 5

import collections
import re


TXT_PATH = "day5.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = file.readlines()


def get_columns(arr: list[str], a: int = None, b: int = None):
    crates = [
        [x[i + 1].strip() for i in range(0, len(x), 4)]
        for x in arr.__getitem__(slice(a, b))
    ]
    stacks = [
        reversed([crates[i][j] for i in range(len(crates))])
        for j in range(len(crates[0]))
    ]
    columns = [collections.deque(filter(bool, c)) for c in stacks]

    return columns


def get_moves(arr: list[str], a: int = None, b: int = None):
    moves = [
        map(int, re.findall(r"\d+", x))
        for x in arr.__getitem__(slice(a, b))
    ]

    return moves


def part1(arr: list[str] = DATA):
    columns = get_columns(arr, None, 8)
    moves = get_moves(arr, 10, None)

    for n, a, b in moves:
        for _ in range(n):
            columns[b - 1].append(columns[a - 1].pop())

    return "".join(x[-1] for x in columns if x)


def part2(arr: list[str] = DATA):
    columns = get_columns(arr, None, 8)
    moves = get_moves(arr, 10, None)

    for n, a, b in moves:
        columns[a - 1].rotate(n)
        for _ in range(n):
            columns[b - 1].append(columns[a - 1].popleft())

    return "".join(x[-1] for x in columns if x)


if __name__ == "__main__":
    print(part1())
    print(part2())
