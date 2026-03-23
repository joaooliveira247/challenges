def lines_are_parallel(x: list[int], y: list[int]) -> bool:
    return x[0] == y[0]


def main() -> None:
    print(lines_are_parallel([1, 2, 3], [1, 2, 4]))

    print(lines_are_parallel([2, 4, 1], [4, 2, 1]))

    print(lines_are_parallel([0, 1, 5], [0, 1, 5]))


if __name__ == "__main__":
    main()
