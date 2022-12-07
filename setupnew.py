import pathlib
import sys


YEAR = 2022


def py_template(day: int, py_path: str, data_path: str, test_path: str) -> None:
    with open(py_path, "w", encoding="utf-8") as file:
        file.write(
            f"""# {YEAR} Day {day}

import typing


# Environment constants
DATA_PATH = {{
    "puzzle": "{data_path}",
    "test": "{test_path}"
}}
DATA = {{
    "puzzle": None,
    "test": None
}}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = file.readlines()
    DATA[key] = data


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> typing.Any:
    pass


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> typing.Any:
    pass


if __name__ == "__main__":
    print("Test data:")
    print(f"\\tPart 1:\\t{{part1(DATA['test'])}}")
    print(f"\\tPart 2:\\t{{part2(DATA['test'])}}")
    print("Puzzle data:")
    print(f"\\tPart 1:\\t{{part1(DATA['puzzle'])}}")
    print(f"\\tPart 2:\\t{{part2(DATA['puzzle'])}}")
"""
        )


def main(*args):
    day = int(args[0])

    # Construct file paths
    py_path = pathlib.Path(f"day{day}.py")
    data_path = pathlib.Path(f"day{day}.txt")
    test_path = pathlib.Path(f"day{day}-test.txt")
    paths = [data_path, test_path, py_path]

    # Verify that both file do not already exists
    for path in paths:
        if path.exists():
            continue
        
        open(path, "w", encoding="utf-8").close()

        if path == py_path:
            py_template(day, py_path, data_path, test_path)

    print(day, py_path, data_path, test_path)


if __name__ == "__main__":
    main(*sys.argv[1:])
