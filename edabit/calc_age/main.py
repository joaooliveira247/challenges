def calc_age(years: int) -> int:
    return years * 365


def main():
    ages: list[int] = [65, 0, 20]

    for age in ages:
        print(calc_age(age))


if __name__ == "__main__":
    main()
