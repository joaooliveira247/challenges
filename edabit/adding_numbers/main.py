def parse_int(x: str) -> int:
    num = 0

    for i, letter in enumerate(reversed(x)):
        if i < 1:
            num += ord(letter) - 48
        else:
            num += (ord(letter) - 48) * (10**i)

    return num


def add(x, y: str) -> str:
    if x == "" or y == "":
        return "Invalid Operation"

    return f"{parse_int(x) + parse_int(y)}"


def main() -> None:
    numbers: list[tuple[str, str]] = [("111", "111"), ("10", "80"), ("", "20")]

    [print(add(*num)) for num in numbers]


if __name__ == "__main__":
    main()
