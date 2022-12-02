# 2022 Day 2


TXT_PATH = "day2.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = [x.split() for x in file.readlines()]


def part1(arr=DATA):
    choices = {"X": 1, "Y": 2, "Z": 3}
    outcomes = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3}
    }

    score = 0

    for a, b in arr:
        score += choices[b]
        score += outcomes[a][b]

    return score


def part2(arr=DATA):
    choices = {"X": 0, "Y": 3, "Z": 6}
    outcomes = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1}
    }

    score = 0

    for a, b in arr:
        score += choices[b]
        score += outcomes[a][b]

    return score


if __name__ == "__main__":
    print(part1())
    print(part2())
