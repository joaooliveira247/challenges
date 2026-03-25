class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return f"Title: {self.title}"

    def get_author(self) -> str:
        return f"Author: {self.author}"


def main() -> None:
    HP = Book("Harry Potter", "J.K. Rowling")
    print(HP.author)
    print(HP.title)
    print(HP.get_title())
    print(HP.get_author())


if __name__ == "__main__":
    main()
