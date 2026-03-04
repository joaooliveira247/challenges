def cubes(x: int) -> int:
    return x**3


def main() -> None:
    cubes_val: list[int] = [3, 5, 10]

    [print(cubes(cube_val)) for cube_val in cubes_val]


if __name__ == "__main__":
    main()
