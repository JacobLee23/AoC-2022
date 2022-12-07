# 2022 Day 7

import collections
import re
import typing
import pathlib


TXT_PATH = "day7.txt"

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = file.readlines()


def get_sizes(arr: typing.List[str]) -> collections.defaultdict:
    sizes = collections.defaultdict()

    root = pathlib.Path("/")
    sizes.setdefault(root, 0)

    node = None
    for line in arr:
        if (m := re.search(r"^\$ cd (.+)$", line)):
            if m.group(1) == "/":
                node = root
            elif m.group(1) == "..":
                sizes[node.parent] += sizes[node]
                node = node.parent
            else:
                node /= m.group(1)
        elif (m := re.search(r"^\$ ls$", line)):
            continue
        elif (m := re.search(r"^dir (.+)$", line)):
            sizes.setdefault((node / m.group(1)), 0)
        elif (m := re.search(r"^(\d+) (.+)$", line)):
            sizes[node] += int(m.group(1))
        else:
            raise ValueError

    return sizes


def part1(arr=DATA):
    sizes = get_sizes(arr)

    return sum(filter(lambda d: d <= MAX_SIZE, sizes.values()))


def part2(arr=DATA):
    sizes = get_sizes(arr)

    return sizes[
        min(
            filter(
                lambda x: TOTAL_SPACE - sizes[pathlib.Path("/")] + sizes[x] >= REQUIRED_SPACE,
                sizes
            ),
            key=lambda x: sizes[x]
        )
    ]


if __name__ == "__main__":
    print(part1())
    print(part2())
