def calculate_exponent(x, y: int) -> int:
    return x**y


def main() -> None:
    expoents: list[tuple[int, int]] = [(5, 5), (10, 10), (3, 3)]

    [print(calculate_exponent(*expoent)) for expoent in expoents]


if __name__ == "__main__":
    main()
