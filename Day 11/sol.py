# 2022 Day 11

from dataclasses import dataclass
import functools
import re
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
        data = file.read().split("\n\n")
    DATA[key] = data


# Puzzle constants
NROUNDS = [20, 10000]


@dataclass
class Monkey:
    def __init__(
        self,
        items: typing.List[int],
        operation: typing.List[int],
        test: typing.List[int]
    ):
        self.items = items
        self.operation = operation
        self.test = test

        self.n = 0

    def operate(self, item: int) -> int:
        if self.operation[1] == "old":
            return item ** 2
        elif self.operation[0] == "+":
            return item + int(self.operation[1])
        elif self.operation[0] == "*":
            return item * int(self.operation[1])

    def inspect(self, monkeys: typing.List["Monkey"], item: int, multiple: int, reduc: int):
        n = (self.operate(item) % multiple) // reduc
        monkeys[self.test[1] if n % self.test[0] == 0 else self.test[2]].items.append(n)

    def turn(self, monkeys: typing.List["Monkey"], multiple: int, reduc: int):
        while len(self.items) > 0:
            self.inspect(monkeys, self.items.pop(), multiple, reduc)
            self.n += 1


def parse_data(arr: typing.List[str]) -> typing.List[Monkey]:
    res = []

    for chunk in arr:
        lines = [
            int(re.search(r"Monkey (\d+):", chunk).group(1)),
            map(
                lambda x: x.strip(),
                re.search(r"Starting items: (.*)", chunk).group(1).split(",")
            ),
            re.search(r"Operation: new = old ([+*]) (\d+|old)", chunk).groups(),
            int(re.search(r"Test: divisible by (\d+)", chunk).group(1)),
            int(re.search(r"If true: throw to monkey (\d+)", chunk).group(1)),
            int(re.search(r"If false: throw to monkey (\d+)", chunk).group(1))
        ]

        res.append(
            Monkey(items=list(map(int, lines[1])), operation=lines[2], test=lines[3:])
        )

    return res


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    monkeys = parse_data(arr)
    multiple = functools.reduce(lambda a, b: a * b, [m.test[0] for m in monkeys])

    for _ in range(NROUNDS[0]):
        for m in monkeys:
            m.turn(monkeys, multiple, 3)

    monkeys.sort(key=lambda x: x.n)
    return monkeys[-1].n * monkeys[-2].n


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    monkeys = parse_data(arr)
    multiple = functools.reduce(lambda a, b: a * b, [m.test[0] for m in monkeys])

    for _ in range(NROUNDS[1]):
        for m in monkeys:
            m.turn(monkeys, multiple, 1)

    monkeys.sort(key=lambda x: x.n)
    return monkeys[-1].n * monkeys[-2].n


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
