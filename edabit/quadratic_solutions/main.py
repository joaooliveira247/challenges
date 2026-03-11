def solutions(a, b, c: int) -> int:
    delta: int = (b**2) - (4 * a * c)

    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0


def main() -> None:
    quadratic_functions: list[tuple[int, int, int]] = [
        (1, 0, -1),
        (1, 0, 0),
        (1, 0, 1),
    ]

    [print(solutions(*func)) for func in quadratic_functions]


if __name__ == "__main__":
    main()
