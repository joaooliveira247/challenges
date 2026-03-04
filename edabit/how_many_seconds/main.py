type Hour = int
type Second = int


def how_many_seconds(hour: Hour) -> Second:
    return hour * 3600


def main():
    hours = [2, 10, 24]

    for hour in hours:
        print(how_many_seconds(hour))


if __name__ == "__main__":
    main()
