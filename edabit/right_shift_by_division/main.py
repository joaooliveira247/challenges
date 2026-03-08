def shift_to_right(x, y: int) -> int:
    return x // (2**y)


def main() -> None:
    operations: list[tuple[int, int]] = [
        (80, 3),
        (-24, 2),
        (-5, 1),
        (4666, 6),
        (3777, 6),
        (-512, 10),
    ]

    [print(f"Args: {opr}| Result: {shift_to_right(*opr)}") for opr in operations]


if __name__ == "__main__":
    main()
