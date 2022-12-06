# 2022 Day 6

import collections


TXT_PATH = "day6.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = list(file.read())


def search(arr: list[str], n: int) -> int:
    q = collections.deque(arr[:n])

    for i, x in enumerate(arr[n:], n):
        if len(set(q)) == n:
            return i

        q.popleft()
        q.append(x)


def part1(arr=DATA):
    return search(arr, 4)


def part2(arr=DATA):
    return search(arr, 14)


if __name__ == "__main__":
    print(part1())
    print(part2())
