# 2022 Day 6

import collections
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
        data = list(file.read())
    DATA[key] = data


# Puzzle constants


# Puzzle constants


def search(arr: typing.List[str], n: int) -> int:
    q = collections.deque(arr[:n])

    for i, x in enumerate(arr[n:], n):
        if len(set(q)) == n:
            return i

        q.popleft()
        q.append(x)


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> int:
    return search(arr, 4)

# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> int:
    return search(arr, 14)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
