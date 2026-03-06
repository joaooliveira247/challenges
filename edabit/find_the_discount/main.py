type Money = int | float

type Discount = float


def dis(value: Money, discount: Discount) -> Money:
    return round(value - (value * (discount / 100)), 2)


def main() -> None:
    operations: list[tuple[Money, Discount]] = [
        (1500, 50),
        (89, 20),
        (100, 75),
    ]

    [print(dis(*opr)) for opr in operations]


if __name__ == "__main__":
    main()
