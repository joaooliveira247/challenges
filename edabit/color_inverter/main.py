def color_invert(colors: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple([(255 - x) for x in colors])


def main() -> None:
    colors_set: list[tuple[int, int, int]] = [
        (0, 0, 0),
        (255, 255, 255),
        (165, 170, 221),
    ]

    [print(color_invert(colors)) for colors in colors_set]


if __name__ == "__main__":
    main()
