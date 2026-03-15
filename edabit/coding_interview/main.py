def interview(questions: list[int], limit_time: int) -> str:
    question_limit_time: dict[str, int] = {
        "very easy": 5,
        "easy": 10,
        "medium": 15,
        "hard": 20,
    }
    questions_level: list[str] = [
        "very easy",
        "very easy",
        "easy",
        "easy",
        "medium",
        "medium",
        "hard",
        "hard",
    ]

    if len(questions) < len(questions_level):
        return "disqualified"

    for question, time in zip(questions_level, questions):
        if time > question_limit_time[question]:
            return "disqualified"

    if sum(questions) > limit_time:
        return "disqualified"
    return "qualified"


def main() -> None:
    test_cases: list[tuple[list[int], int]] = [
        ([5, 5, 10, 10, 15, 15, 20, 20], 120),
        ([2, 3, 8, 6, 5, 12, 10, 18], 64),
        ([5, 5, 10, 10, 25, 15, 20, 20], 120),
        ([5, 5, 10, 10, 15, 15, 20], 120),
        ([5, 5, 10, 10, 15, 15, 20, 20], 130),
    ]

    [print(interview(*test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
