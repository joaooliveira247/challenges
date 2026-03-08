def find_highest(arr: list[int]):
    if len(arr) == 1:
        return arr[0]

    if arr[0] > arr[1]:
        return find_highest(arr[:1] + arr[2:])
    else:
        return find_highest(arr[1:])


def main() -> None:
    test_cases: list[list[int]] = [[-1, 3, 5, 6, 99, 12, 2], [0, 12, 4, 87], [8]]

    [print(find_highest(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
