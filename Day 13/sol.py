# 2022 Day 13

import functools
import json
import math
import typing


# Environment constants
DATA_PATH = {
    "puzzle": "puzzle-data.txt",
    "test": "test-data.txt"
}
DATA = {
    "puzzle": None,
    "test": None
}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = file.read().split("\n\n")
    DATA[key] = data


# Puzzle constants


def compare(left: typing.Union[typing.List, int], right: typing.Union[typing.List, int]) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            cmp = compare(a, b)
            if cmp == 1:
                return 1
            elif cmp == -1:
                return -1

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
        
    else:
        raise TypeError(a, b)


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    packets = [list(map(json.loads, x.split("\n"))) for x in arr]
    return sum(i for i, x in enumerate(packets) if compare(*x) == 1)


# Part 2 solution
def part2(arr: typing.List[str]) -> int:
    dividers = [[[2]], [[6]]]

    packets = []
    for line in arr:
        packets.extend(map(json.loads, line.split("\n")))
    packets.extend(dividers)

    s_packets = sorted(
        packets,
        key=functools.cmp_to_key(lambda a, b: -compare(a, b))
    )

    return math.prod(i for i, x in enumerate(s_packets, 1) if x in dividers)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
