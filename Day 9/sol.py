# 2022 Day 9

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
DIRECTIONS = {
    "R": lambda x, y: [x + 1, y],
    "L": lambda x, y: [x - 1, y],
    "U": lambda x, y: [x, y + 1],
    "D": lambda x, y: [x, y - 1]
}


def move(head: typing.List[int], tail: typing.List[int]) -> typing.List[int]:
    if head[0] - tail[0] < -1 and head[1] - tail[1] < -1:
        return [head[0] + 1, head[1] + 1]
    elif head[0] - tail[0] > 1 and head[1] - tail[1] < -1:
        return [head[0] - 1, head[1] + 1]
    elif head[0] - tail[0] > 1 and head[1] - tail[1] > 1:
        return [head[0] - 1, head[1] - 1]
    elif head[0] - tail[0] < -1 and head[1] - tail[1] > 1:
        return [head[0] + 1, head[1] - 1]
    elif head[0] - tail[0] < -1 and abs(head[1] - tail[1]) <= 1:
        return [head[0] + 1, head[1]]
    elif abs(head[0] - tail[0]) <= 1 and head[1] - tail[1] < -1:
        return [head[0], head[1] + 1]
    elif head[0] - tail[0] > 1 and abs(head[1] - tail[1]) <= 1:
        return [head[0] - 1, head[1]]
    elif abs(head[0] - tail[0]) <= 1 and head[1] - tail[1] > 1:
        return [head[0], head[1] - 1]
    return tail


# Part 1 solution
def part1(arr: typing.List[str]) -> typing.Any:
    head, tail = [0, 0], [0, 0]

    positions = {tuple(tail)}
    for d, x in arr:
        for _ in range(int(x)):
            head = DIRECTIONS[d](*head)
            tail = move(head, tail)
            positions.add(tuple(tail))

    return len(positions)


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    knots = [[0, 0] for _ in range(10)]

    positions = {tuple(knots[-1])}
    for d, x in arr:
        for _ in range(int(x)):
            knots[0] = DIRECTIONS[d](*knots[0])
            for i in range(1, len(knots)):
                knots[i] = move(knots[i - 1], knots[i])
            positions.add(tuple(knots[-1]))

    return len(positions)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
