def difference(n: int) -> int:
    square_sum = [a for a in range(1, 11)]
    sum_square = [a**2 for a in range(1, 11)]
    return (sum(square_sum)**2) - sum(sum_square)

def main() -> None:
    answ = difference(10)
    print(f"Answer: {answ}")

if __name__ == "__main__":
    main()