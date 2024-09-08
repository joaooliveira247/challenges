from typing import TypeVar

"""Functions for organizing and calculating student exam scores."""

T = TypeVar("T", str, float)


def round_scores(student_scores: list[T]) -> list[T]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    return [round(x) for x in student_scores]


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    return len([x for x in student_scores if x <= 40])


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best'
    based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best"
    threshold.
    """

    return [x for x in student_scores if x >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade
     interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55 - 15
            56 <= "C" <= 70 - 15
            71 <= "B" <= 85 - 15
            86 <= "A" <= 100 - 15

            0 - 15
            3 - 14
            8 - 13
            15 - 11
            12 - 11
            19 - 10
    """

    value_sum: int = round((highest - 41) / 4)

    return [41 + (value_sum * i) if i != 0 else 41 for i in range(4)]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in descending
      order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending
    order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    scores: list[tuple[int, tuple[int, str]]] = list(
        enumerate(sorted(zip(student_scores, student_names), reverse=True), 1)
    )

    return [f"{rank}. {name}: {score}" for rank, (score, name) in scores]


def perfect_score(
    student_info: list[list[str, int]]
) -> list[list[str, int]] | list[None]:
    """Create a list that contains the name and grade of the first student to
    make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score
    of 100 is found.
    """

    for single in student_info:
        if 100 in single:
            return single
    return []
