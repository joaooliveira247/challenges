def invert(dct: dict) -> dict:
    new_dct = {}
    for k, v in dct.items():
        new_dct[v] = k

    return new_dct


def main() -> None:
    test_cases: list[dict] = [
        {"z": "q", "w": "f"},
        {"a": 1, "b": 2, "c": 3},
        {"zebra": "koala", "horse": "camel"},
    ]

    [print(test_case, invert(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
