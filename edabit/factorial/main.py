def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


def main() -> None:
    nums: tuple[int, int, int] = 3, 5, 13

    [print(factorial(num)) for num in nums]


if __name__ == "__main__":
    main()
