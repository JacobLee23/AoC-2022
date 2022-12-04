# 2022 Day 4


TXT_PATH = "day4.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = [
        [list(map(int, y.split("-"))) for y in x.split(",")]
        for x in file.readlines()
    ]


def part1(arr=DATA):
    count = 0

    for pair in arr:
        (a, b), (c, d) = pair
        m, n = range(a, b + 1), range(c, d + 1)

        if all(x in n for x in m) or all(x in m for x in n):
            count += 1

    return count


def part2(arr=DATA):
    count = 0

    for pair in arr:
        (a, b), (c, d) = pair
        m, n = range(a, b + 1), range(c, d + 1)

        if any(x in n for x in m) or any(x in m for x in n):
            count += 1

    return count


if __name__ == "__main__":
    print(part1())
    print(part2())
