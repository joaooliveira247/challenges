def number_length(n: int) -> int:
    if n // 10 < 1:
        return 1
    return number_length(n // 10) + 1


def main() -> None:
    nums: list[int] = [10, 5000, 0]

    [print(number_length(num)) for num in nums]


if __name__ == "__main__":
    main()
