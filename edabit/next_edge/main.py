def next_edge(x, y: int) -> int:
    return (x + y) - 1


def main() -> None:

    edges: list[tuple[int, int]] = [(8, 10), (5, 7), (9, 2)]

    [print(next_edge(*edge)) for edge in edges]


if __name__ == "__main__":
    main()
