# 2022 Day 1

import typing


# Environment constants
DATA_PATH = {
    "puzzle": "day1.txt",
    "test": "day1-test.txt"
}
DATA = {
    "puzzle": None,
    "test": None
}
for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = [list(map(int, x.split())) for x in file.read().split("\n\n")]
    DATA[key] = data


# Puzzle constants
N = 3


# Part 1 solution
def part1(arr: typing.List[typing.List[int]] = DATA) -> int:
    return max(list(map(sum, arr)))


# Part 2 solution
def part2(arr: typing.List[typing.List[int]] = DATA) -> int:
    return sum(sorted(list(map(sum, arr)))[-N:])


if __name__ == "__main__":
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")
