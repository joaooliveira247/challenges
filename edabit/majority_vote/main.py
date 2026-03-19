from collections import Counter


def majority_vote(votes: list[str]) -> str | None:
    votes_counter: Counter = Counter(votes)

    winner = votes_counter.most_common(1)[0]

    return winner[0] if ((winner[1] / votes_counter.total()) > 1 / 2) else None


def main() -> None:

    test_cases: list[list[str]] = [
        ["A", "A", "B"],
        ["A", "A", "A", "B", "C", "A"],
        ["A", "B", "B", "A", "C", "C"],
    ]

    [print(majority_vote(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
