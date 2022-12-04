import os
import pathlib
import sys


YEAR = 2022


def new(day: int, txt_path: str) -> pathlib.Path:
    path = pathlib.Path(f"day{day}.py")

    with open(path, "w", encoding="utf-8") as file:
        file.write(
            f"""# {YEAR} Day {day}


TXT_PATH = "{txt_path}"


with open(TXT_PATH, "r", encoding="utf-8") as file:
    DATA = file.readlines()


def part1(arr=DATA):
    pass


def part2(arr=DATA):
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
"""
        )

    return path


def main(*args):
    day = int(args[0])

    # Construct file paths
    txt_path = pathlib.Path(f"day{day}.txt")
    py_path = pathlib.Path(f"day{day}.py")

    # Verify that both file do not already exists
    if txt_path.exists() and py_path.exists():
        raise os.error("[Errno 17] File exists")

    # Create .txt file
    open(txt_path, "w", encoding="utf-8").close()

    # Create .py file
    py_path = new(day, txt_path)

    print(py_path, txt_path)


if __name__ == "__main__":
    main(*sys.argv[1:])
