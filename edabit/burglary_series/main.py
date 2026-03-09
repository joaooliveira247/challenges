def find_it(items: dict[str, int], name: str) -> str:
    return (
        f"{name.title()} is gone ..." if name in items else f"{name.title()} is here !"
    )


def main() -> None:
    test_cases: list[tuple[dict[str, int], str]] = [
        (
            {
                "tv": 30,
                "timmy": 20,
                "stereo": 50,
            },
            "timmy",
        ),
        (
            {
                "tv": 30,
                "stereo": 50,
            },
            "timmy",
        ),
        ({}, "timmy"),
    ]

    [print(find_it(*test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
