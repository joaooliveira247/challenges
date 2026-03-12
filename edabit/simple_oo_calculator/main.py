class Calculator:
    @classmethod
    def add(cls, a, b: int) -> int:
        return a + b

    @classmethod
    def sub(cls, a, b: int) -> int:
        return a - b

    @classmethod
    def mult(cls, a, b: int) -> int:
        return a * b

    @classmethod
    def div(cls, a, b: int) -> int:
        return a // b


def main() -> None:
    calc = Calculator()

    print(calc.add(10, 5))
    print(calc.sub(10, 5))
    print(calc.mult(10, 5))
    print(calc.div(10, 5))


if __name__ == "__main__":
    main()
