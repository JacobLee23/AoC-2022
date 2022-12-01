# 2022 Day 1


TXT_PATH = "day1.txt"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = [list(map(int, x.split())) for x in file.read().split("\n\n")]


def part1(arr=DATA):
    return max(list(map(sum, arr)))



def part2(arr=DATA):
    return sum(sorted(list(map(sum, arr)))[-3:])



if __name__ == "__main__":
    print(part1())
    print(part2())
