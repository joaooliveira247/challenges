def int_to_str(n: int) -> str:
    return f"{n}"


def str_to_int(s: str) -> int:
    int_num = 0

    for i, n in enumerate(reversed(s)):
        if i < 1:
            int_num += ord(n) - 48
            continue
        int_num += (ord(n) - 48) * (10**i)

    return int_num


def main() -> None:
    int_test: tuple[int, int] = 4, 2956

    str_test: tuple[str, str, str] = "4", "2956", "4000"

    [
        print(
            f"Function: {int_to_str.__name__} | Type: {int_to_str.__annotations__['return']}, Result: {int_to_str(num)}"
        )
        for num in int_test
    ]

    [
        print(
            f"Function: {str_to_int.__name__} | Type: {str_to_int.__annotations__['return']}, Result: {str_to_int(num)}"
        )
        for num in str_test
    ]


if __name__ == "__main__":
    main()
