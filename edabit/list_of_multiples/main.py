def list_of_multiples(num, length: int) -> list[int]:
    if length <= 1:
        return [num * length]
    return list_of_multiples(num, length - 1) + [num * length]


def main() -> None:

    nums: list[tuple[int, int]] = [(7, 5), (12, 10), (17, 6)]

    [print(list_of_multiples(*args)) for args in nums]


if __name__ == "__main__":
    main()
