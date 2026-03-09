from dataclasses import dataclass


@dataclass
class Stock:
    cost_price: float
    sell_price: float
    inventory: int


def profit(stock: Stock) -> float:
    return round((stock.sell_price - stock.cost_price) * stock.inventory, 2)


def main() -> None:
    test_cases = [
        Stock(cost_price=32.67, sell_price=45.00, inventory=1200),
        Stock(cost_price=225.89, sell_price=550.00, inventory=100),
        Stock(cost_price=2.77, sell_price=7.95, inventory=8500),
    ]

    [print(profit(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
