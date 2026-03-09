from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def line_length(a, b: Point) -> float:
    return round((((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)) ** (1 / 2), 2)


def main():
    coords: list[tuple[Point, Point]] = [
        (Point(15, 7), Point(22, 11)),
        (Point(0, 0), Point(0, 0)),
        (Point(0, 0), Point(0, 1)),
    ]

    [print(line_length(*points)) for points in coords]


if __name__ == "__main__":
    main()
