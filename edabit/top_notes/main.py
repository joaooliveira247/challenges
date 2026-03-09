from dataclasses import dataclass


@dataclass
class Student:
    name: str
    notes: list[int]


def top_note(student: Student) -> dict[str, str | int]:
    return {"name": student.name, "top_note": max(student.notes)}


def main() -> None:
    test_cases = [
        Student(name="John", notes=[3, 5, 4]),
        Student(name="Max", notes=[1, 4, 6]),
        Student(name="Zygmund", notes=[1, 2, 3]),
    ]
    
    [print(top_note(test_case)) for test_case in test_cases]


if __name__ == "__main__":
    main()
