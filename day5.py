# 2022 Day 5

import collections
import re
import typing


# Environment constants
DATA_PATH = {
    "puzzle": "day5.txt",
    "test": "day5-test.txt"
}
DATA = {
    "puzzle": None,
    "test": None
}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = [x.split("\n") for x in file.read().split("\n\n")]
    DATA[key] = data


# Puzzle constants


def get_columns(arr: typing.List[str]) -> typing.List[str]:
    crates = ((c.strip() for c in x[1::4]) for x in arr[:-1])
    stacks = (filter(bool, reversed(list(x))) for x in zip(*crates))

    return list(map(collections.deque, stacks))


def get_moves(arr: typing.List[str]) -> typing.List[str]:
    return [map(int, re.findall(r"\d+", x)) for x in arr]


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> str:
    columns = get_columns(arr[0])
    moves = get_moves(arr[1])

    for n, a, b in moves:
        columns[b - 1].extend(columns[a - 1].pop() for _ in range(n))

    return "".join(x[-1] for x in columns if x)


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> str:
    columns = get_columns(arr[0])
    moves = get_moves(arr[1])

    for n, a, b in moves:
        columns[a - 1].rotate(n)
        columns[b - 1].extend(columns[a - 1].popleft() for _ in range(n))

    return "".join(x[-1] for x in columns if x)


if __name__ == "__main__":
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")
