# 2022 Day 2

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
        data = [x.split() for x in file.readlines()]
    DATA[key] = data


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> int:
    choices = {"X": 1, "Y": 2, "Z": 3}
    outcomes = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3}
    }

    return sum(choices[b] + outcomes[a][b] for a, b in arr)


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> int:
    choices = {"X": 0, "Y": 3, "Z": 6}
    outcomes = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1}
    }

    return sum(choices[b] + outcomes[a][b] for a, b in arr)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
