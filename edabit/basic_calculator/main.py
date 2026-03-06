from typing import Callable


def calculator(val_1: int, opr: str, val_2: int) -> int | float | str:
    oprs: dict[str, Callable[[int, int], int | float]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    if opr == "/" and val_2 == 0:
        return "Can't divide by 0!"

    return oprs[opr](val_1, val_2)


def main() -> None:
    operations: list[tuple[int, str, int]] = [
        (2, "+", 2),
        (5, "-", 2),
        (10, "*", 2),
        (2, "/", 2),
        (2, "/", 0),
    ]

    [print(calculator(*operation)) for operation in operations]


if __name__ == "__main__":
    main()
