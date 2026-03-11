def divisible_b(a, b: int) -> int:
    return ((a // b) * b) + b


def main() -> None:
    operations: list[tuple[int, int]] = [
        (17, 8),
        (98, 3),
        (14, 11),
    ]

    [print(divisible_b(*opr)) for opr in operations]


if __name__ == "__main__":
    main()
