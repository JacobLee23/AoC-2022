# 2022 Day 12

import string
import typing

import networkx


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


def get_start(arr: typing.List[str]) -> typing.Tuple[int, int]:
    for i, line in enumerate(arr):
        try:
            return line.index("S"), i
        except ValueError:
            continue


def get_end(arr: typing.List[str]) -> typing.Tuple[int, int]:
    for i, line in enumerate(arr):
        try:
            return line.index("E"), i
        except ValueError:
            continue


def get_grid(arr: typing.List[str]) -> typing.List[typing.List[int]]:
    return [
        [string.ascii_lowercase.index(c) for c in s]
        for s in [
            x.replace("S", "a").replace("E", "z").strip() for x in arr
        ]
    ]


def get_graph(grid: typing.List[typing.List[int]]) -> networkx.DiGraph:
    dim = (len(grid[0]), len(grid))
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]

    graph = networkx.DiGraph()

    for y in range(dim[1]):
        for x in range(dim[0]):
            for dx, dy in directions:
                if (x + dx) in range(dim[0]) and (y + dy) in range(dim[1]):
                    if grid[y + dy][x + dx] <= grid[y][x] + 1:
                        graph.add_edge((x, y), (x + dx, y + dy))

    return graph


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    start, end, grid = get_start(arr), get_end(arr), get_grid(arr)

    graph = get_graph(grid)
    path = networkx.shortest_path(graph, start, end)

    return len(path) - 1


# Part 2 solution
def part2(arr: typing.List[str]) -> int:
    end, grid = get_end(arr), get_grid(arr)
    dim = (len(grid[0]), len(grid))

    graph = get_graph(grid)

    res = None
    for y in range(dim[1]):
        for x in range(dim[0]):
            if grid[y][x] != 0:
                continue

            try:
                path = networkx.shortest_path(graph, (x, y), end)
            except:
                continue

            res = (len(path) - 1) if res is None else min([res, len(path) - 1])

    return res


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
