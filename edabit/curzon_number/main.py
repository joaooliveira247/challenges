def is_curzon(num: int):
    return ((2**num) + 1) % ((2 * num) + 1) == 0


def main() -> None:
    print(is_curzon(5))
    print(is_curzon(10))
    print(is_curzon(14))


if __name__ == "__main__":
    main()
