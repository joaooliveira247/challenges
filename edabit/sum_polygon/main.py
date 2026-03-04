def sum_polygon(x: int) -> int:
    return (x - 2) * 180


def main() -> None:
    polygons: list[int] = [3, 4, 6]

    [print(sum_polygon(polygon)) for polygon in polygons]


if __name__ == "__main__":
    main()
