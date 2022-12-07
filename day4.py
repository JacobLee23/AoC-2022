# 2022 Day 4

import typing


# Environment constants
DATA_PATH = {
    "puzzle": "day4.txt",
    "test": "day4-test.txt"
}
DATA = {
    "puzzle": None,
    "test": None
}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = [
            [list(map(int, y.split("-"))) for y in x.split(",")]
            for x in file.readlines()
        ]
    DATA[key] = data


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> typing.Any:
    return sum(
        int((c <= a <= b <= d) or (a <= c <= d <= b))
        for (a, b), (c, d) in arr
    )


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> typing.Any:
    return sum(
        int((c <= a <= d or c <= b <= d) or (a <= c <= b or a <= d <= b))
        for (a, b), (c, d) in arr
    )


if __name__ == "__main__":
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")
