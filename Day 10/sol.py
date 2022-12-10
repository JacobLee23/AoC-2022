# 2022 Day 10

import re
import textwrap
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
        data = file.readlines()
    DATA[key] = data


# Puzzle constants
N = [
    20, 60, 100, 140, 180, 220
]


def parse_data(arr: typing.List[str]) -> typing.List[int]:
    a = [1]

    for line in arr:
        if re.search(r"^noop$", line):
            a.append(a[-1])
        elif (m := re.search(r"^addx ([0-9-]+)$", line)):
            a.extend([a[-1], a[-1] + int(m.group(1))])

    return a


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    d = parse_data(arr)
    return sum(x * d[x - 1] for x in map(lambda x: 40 * x + 20, range(6)))


# Part 2 solution
def part2(arr: typing.List[str]) -> str:
    d = parse_data(arr)
    s = "".join("#" if (d[i] - 1 <= (i % 40) <= d[i] + 1) else "." for i in range(len(d)))
    return "\n" + "\n".join(textwrap.wrap(s, 40))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
