def total_overs(balls: int) -> float:
    return balls // 6 + ((balls % 6) / 10)


def main() -> None:
    matches: list[int] = [2400, 164, 945, 5]

    [print(total_overs(match)) for match in matches]


if __name__ == "__main__":
    main()
