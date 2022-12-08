# 2022 Day 3

import functools
import string
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
        data = [x.strip() for x in file.readlines()]
    DATA[key] = data


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> typing.Any:
    items = []

    for line in arr:
        items.extend(
            functools.reduce(
                lambda x, y: x.intersection(y),
                map(set, [line[:(len(line) // 2)], line[(len(line) // 2):]])
            )
        )

    return sum(string.ascii_letters.index(x) + 1 for x in items)


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> typing.Any:
    items = []

    for i in range(0, len(arr), 3):
        items.extend(
            functools.reduce(
                lambda x, y: x.intersection(y),
                map(set, arr[i:(i + 3)])
            )
        )

    return sum(string.ascii_letters.index(x) + 1 for x in items)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
