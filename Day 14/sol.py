# 2022 Day 14

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
        data = [
            [tuple(map(int, x.split(","))) for x in ln.split(" -> ")]
            for ln in file.readlines()
        ]
    DATA[key] = data


# Puzzle constants
START = (500, 0)


def get_grid(arr: typing.List[typing.List[typing.Tuple[int]]]) -> typing.Dict[typing.Tuple[int], str]:
    grid = {}
    
    for points in arr:
        x, y = points[0]
        grid[x, y] = "#"

        for nx, ny in points[1:]:
            while x != nx or y != ny:
                dx, dy = (nx > x) - (x > nx), (ny > y) - (y > ny)
                x, y = x + dx, y + dy
                grid[x, y] = "#"

    return grid


def print_grid(grid: typing.Dict[typing.Tuple[int], str]) -> None:
    for y in range(max(k[1] for k in grid) + 2):
        for x in range(min(k[0] for k in grid), max(k[0] for k in grid) + 1):
            print(grid[x, y] if (x, y) in grid else ".", end="")
        print()
    print()


def trim_grid(grid: typing.Dict[typing.Tuple[int], str]) -> typing.Dict[typing.Tuple[int], str]:
    max_y = max(a[1] for a in grid)

    xvalues = (
        x for (x, y) in zip((a[0] for a in grid), (a[1] for a in grid)) if (x, y) in grid
    )
    min_x = min(
        x for (x, y) in zip((a[0] for a in grid), (a[1] for a in grid)) if (x, y) in grid
    )
    max_x = max(
        x for (x, y) in zip((a[0] for a in grid), (a[1] for a in grid)) if (x, y) in grid
    )

    return {
        (x, y): grid[x, y]
        for x in range(min(xvalues), max(xvalues) + 1) for y in range(max_y + 1)
        if (x, y) in grid
    }


def pour(grid: typing.Dict[typing.Tuple[int], str]) -> typing.Dict[typing.Tuple[int], str]:
    limits_x = min(a[0] for a in grid), max(a[0] for a in grid)
    limits_y = min(a[1] for a in grid), max(a[1] for a in grid)

    done = False
    while not done:
        sx, sy = START[0], START[1]

        if grid.get((sx, sy)) == "o":
            break

        while True:
            if sx < limits_x[0] or sx > limits_x[1]:
                done = True
                break
            elif sy > limits_y[1]:
                done = True
                break
            
            if grid.get((sx, sy + 1)) is None:
                sy = sy + 1
            elif grid.get((sx - 1, sy + 1)) is None:
                sx, sy = sx - 1, sy + 1
            elif grid.get((sx + 1, sy + 1)) is None:
                sx, sy = sx + 1, sy + 1
            else:
                grid[sx, sy] = "o"
                break

    return grid


# Part 1 solution
def part1(arr: typing.List[typing.List[typing.Tuple[int]]]) -> int:
    grid = get_grid(arr)
    res = pour(grid)
    print_grid(trim_grid(res))

    return list(res.values()).count("o")


# Part 2 solution
def part2(arr: typing.List[typing.List[typing.Tuple[int]]]) -> int:
    grid = get_grid(arr)

    base = max(a[1] for a in grid)
    for x in range(-1000, 1001):
        grid[x, base + 2] = "#"

    res = pour(grid)
    print_grid(trim_grid(res))

    return list(res.values()).count("o")


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
