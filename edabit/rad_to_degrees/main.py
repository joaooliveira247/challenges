from math import pi


def radians_to_degrees(rad: int) -> float:
    return round(rad * (180 / pi), 1)


def main() -> None:
    rads: list[int] = [1, 20, 50]

    [print(radians_to_degrees(rad)) for rad in rads]


if __name__ == "__main__":
    main()
