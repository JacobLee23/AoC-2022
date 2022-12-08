# 2022 Day 7

import collections
import re
import typing
import pathlib


# Environment constants
DATA_PATH = {
    "puzzle": "day7.txt",
    "test": "day7-test.txt"
}
DATA = {
    "puzzle": None,
    "test": None
}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = file.readlines()
    DATA[key] = data


# Puzzle constants
MAX_SIZE = 100000
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000


def get_sizes(arr: typing.List[str]) -> collections.defaultdict:
    d = collections.defaultdict()

    root = pathlib.Path("/")
    d.setdefault(root, 0)

    node = None
    for line in arr:
        if (m := re.search(r"^\$ cd (.*)$", line)):
            if m.group(1) == "/":
                node = root
            elif m.group(1) == "..":
                d[node.parent] += d[node]
                node = node.parent
            else:
                node = node / m.group(1)
        elif (m := re.search(r"^\$ ls$", line)):
            continue
        elif (m := re.search(r"^dir (.+)$", line)):
            d.setdefault((node / m.group(1)), 0)
        elif (m := re.search(r"^(\d+) (.+)$", line)):
            d[node] += int(m.group(1))
        else:
            raise ValueError

    return d


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> int:
    sizes = get_sizes(arr)

    return sum(filter(lambda d: d <= MAX_SIZE, sizes.values()))


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> int:
    sizes = get_sizes(arr)

    options = filter(
        lambda x: TOTAL_SPACE - sizes[pathlib.Path("/")] + sizes[x] >= REQUIRED_SPACE, sizes
    )
    return sizes[min(options, key=lambda x: sizes[x])]


if __name__ == "__main__":
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")
