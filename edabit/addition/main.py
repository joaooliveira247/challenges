def addition(num: int) -> int:
    return num + 1


def main() -> None:
    nums: list[int] = [9, 0, -3]

    [print(addition(num)) for num in nums]


if __name__ == "__main__":
    main()
