WORLD_SIZE: int = 148_940_000


def area_of_country(country: str, area: int) -> str:
    #  world_size -> 100% | area -> x | x = (area * 100) / world_size
    return f"{country} is {round((area * 100) / WORLD_SIZE, 2)}% of the total world's"


def main() -> None:
    countries: list[tuple[str, int]] = [
        ("Russia", 17098242),
        ("USA", 9372610),
        ("IRAN", 1648195),
    ]

    [print(area_of_country(*country)) for country in countries]


if __name__ == "__main__":
    main()
