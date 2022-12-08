# 2022 Day 8

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
        data = [list(map(int, list(x))) for x in file.read().split("\n")]
    DATA[key] = data


# Puzzle constants


def is_visible(arr: typing.List[typing.List[int]], i: int, j: int) -> bool:
    directions = [
        [a[j] for a in arr[(i + 1):]],
        [a[j] for a in arr[:i]],
        arr[i][(j + 1):],
        arr[i][:j],
    ]
    return any(all(arr[i][j] > x for x in d) for d in directions)


def viewing_score(arr: typing.List[typing.List[int]], i: int, j: int) -> int:
    directions = [
        [a[j] for a in arr[(i + 1):]],
        [a[j] for a in arr[:i][::-1]],
        arr[i][(j + 1):],
        arr[i][:j][::-1],
    ]

    score = 1
    for d in directions:
        distance = 0
        for x in d:
            distance += 1
            if not arr[i][j] > x:
                break
        score *= distance

    return score

# Part 1 solution
def part1(arr: typing.List[typing.List[int]] = DATA) -> int:
    return sum(
        is_visible(arr, i, j)
        for i in range(1, len(arr) - 1)
        for j in range(1, len(arr[i]) - 1)
    ) + (2 * (len(arr) + len(arr[0])) - 4)


# Part 2 solution
def part2(arr: typing.List[typing.List[int]] = DATA) -> int:
    return max(
        viewing_score(arr, i, j)
        for i in range(1, len(arr) - 1)
        for j in range(1, len(arr[0]) - 1)
    )


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
