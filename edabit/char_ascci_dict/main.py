def to_dict(lst: list[str]) -> list[dict[str, int]]:
    return [{letter: ord(letter)} for letter in lst]


def main() -> None:
    test_cases: list[list[str]] = [
        ["a", "b", "c"],
        ["^"],
        [],
    ]

    [print(to_dict(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
