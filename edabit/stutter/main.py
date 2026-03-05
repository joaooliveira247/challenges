def stutter(word: str) -> str:
    return "%s... %s... %s?" % (word[:2], word[:2], word)


def main() -> None:
    words: list[str] = ["incredible", "enthusiastic", "outstanding"]

    [print(stutter(word)) for word in words]


if __name__ == "__main__":
    main()
