def V_DAC(DAC: int) -> float:
    return round((5 * DAC) / 1023, 2)


def main() -> None:
    values: list[int] = [0, 1023, 400]

    [print(V_DAC(val)) for val in values]


if __name__ == "__main__":
    main()
