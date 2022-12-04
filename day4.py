# 2022 Day 4

import functools


TXT_PATH = "day4.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = [
        [list(map(int, y.split("-"))) for y in x.split(",")]
        for x in file.readlines()
    ]


def part1(arr=DATA):
    return sum(
        int((c <= a <= b <= d) or (a <= c <= d <= b))
        for (a, b), (c, d) in arr
    )


def part2(arr=DATA):
    return sum(
        int((c <= a <= d or c <= b <= d) or (a <= c <= b or a <= d <= b))
        for (a, b), (c, d) in arr
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
