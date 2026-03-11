def squares_areas_diff(r: int) -> int:
    return (4 * (r**2)) - (2 * (r**2))


def main() -> None:
    circles_radius: list[int] = [5, 6, 7]

    [print(squares_areas_diff(circle_radius)) for circle_radius in circles_radius]


if __name__ == "__main__":
    main()
