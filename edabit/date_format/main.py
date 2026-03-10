def format_date(date: str) -> str:
    day, month, year = date.split("/")
    return f"{year}{month}{day}"


def main() -> None:
    dates: list[str] = [
        "11/12/2019",
        "12/31/2019",
        "01/15/2019",
    ]

    [print(format_date(date)) for date in dates]


if __name__ == "__main__":
    main()
