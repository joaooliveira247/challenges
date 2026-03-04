def relation_to_luke(person: str) -> str:
    relationship: dict[str, str] = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
    }

    relation: str = relationship[person]

    return "Luke I am your %s." % relation


def main() -> None:
    peoples: list[str] = ["Darth Vader", "Leia", "Han"]

    [print(relation_to_luke(people)) for people in peoples]


if __name__ == "__main__":
    main()
