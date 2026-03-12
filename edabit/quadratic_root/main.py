def quadratic_equation(a, b, c: int) -> int:
    delta = (b**2) - (4 * a * c)

    if delta > 0:
        x1 = (-b + (delta ** (1 / 2))) / (2 * a)
        x2 = (-b - (delta ** (1 / 2))) / (2 * a)
        return x1 if x1 > x2 else x2
    else:
        return (-b + (delta ** (1 / 2))) / (2 * a)


def main() -> None:
    functions: list[tuple[int, int, int]] = [(1, 2, -3), (2, -7, 3), (1, -12, -28)]

    [print(quadratic_equation(*func)) for func in functions]


if __name__ == "__main__":
    main()
