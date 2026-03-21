from decimal import InvalidOperation


def arithmethic_operation(operation: str) -> int:
    args: list[str] = operation.split()

    if len(args) != 3:
        raise InvalidOperation

    a, operator, b = args

    match operator:
        case "+":
            return int(a) + int(b)
        case "-":
            return int(a) - int(b)
        case "*":
            return int(a) * int(b)
        case "//":
            if int(b) == 0:
                return -1
            return int(a) // int(b)
        case _:
            raise InvalidOperation


def main() -> None:
    operations: list[str] = [
        "12 + 12",
        "12 - 12",
        "12 * 12",
        "12 // 0",
        "12 // 3",
    ]

    [print(arithmethic_operation(opr)) for opr in operations]


if __name__ == "__main__":
    main()
