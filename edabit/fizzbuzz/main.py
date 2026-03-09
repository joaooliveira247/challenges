def fizz_buzz(n: int) -> str:
    match n:
        case _ if n % 15 == 0:
            return "FizzBuzz"
        case _ if n % 5 == 0:
            return "Buzz"
        case _ if n % 3 == 0:
            return "Fizz"
        case _:
            return f"{n}"

def main() -> None:
    nums: list[int] = [3, 5, 15, 4, 7]
    
    [print(f"{fizz_buzz(num)}") for num in nums]


if __name__ == "__main__":
    main()
