type Ohms = int | float


def series_resistance(circuit: list[Ohms]) -> str:
    total_ohms = sum(circuit)
    return "%s ohm" % total_ohms if total_ohms <= 1 else "%s ohms" % total_ohms


def main() -> None:
    circuits: list[list[Ohms]] = [
        [1, 5, 6, 3],
        [16, 3.5, 6],
        [0.5, 0.5],
    ]

    [print(series_resistance(circuit)) for circuit in circuits]


if __name__ == "__main__":
    main()
