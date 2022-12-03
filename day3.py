# 2022 Day 3

import functools
import string


TXT_PATH = "day3.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = [x.strip() for x in file.readlines()]


def part1(arr=DATA):
    items = []

    for line in arr:
        sets = map(set, [line[:(len(line) // 2)], line[(len(line) // 2):]])

        intersect = functools.reduce(lambda x, y: x.intersection(y), sets)

        items.extend(intersect)

    return sum(string.ascii_letters.index(x) + 1 for x in items)


def part2(arr=DATA):
    items = []

    for i in range(0, len(arr), 3):
        sets = map(set, arr[i:(i + 3)])

        intersect = functools.reduce(lambda x, y: x.intersection(y), sets)

        items.extend(intersect)

    return sum(string.ascii_letters.index(x) + 1 for x in items)


if __name__ == "__main__":
    print(part1())
    print(part2())
