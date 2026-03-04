def remainder(x, y: int) -> int:
    return x % y


def main():
    nums_pairs: list[tuple[int, int]] = [
        (1, 3),
        (3, 4),
        (5, 5),
        (7, 2),
    ]

    [print(remainder(*nums)) for nums in nums_pairs]


if __name__ == "__main__":
    main()
