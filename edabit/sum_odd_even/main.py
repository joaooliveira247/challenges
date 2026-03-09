def sum_odd_and_even(nums: list[int]) -> list[int]:
    even, odd = 0, 0

    for num in nums:
        if num % 2 == 0:
            even += num
        else:
            odd += num

    return [even, odd]


def main() -> None:
    num_set: list[list[int]] = [[1, 2, 3, 4, 5, 6], [-1, -2, -3, -4, -5, -6], [0, 0]]

    [print(sum_odd_and_even(nums)) for nums in num_set]


if __name__ == "__main__":
    main()
