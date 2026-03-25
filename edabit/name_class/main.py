class Name:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname.title()
        self.lname = lname.title()

    @property
    def full_name(
        self,
    ) -> str:
        return f"{self.fname} {self.lname}"

    @property
    def initials(
        self,
    ) -> str:
        return f"{self.fname[0]}.{self.lname[0]}"


def main() -> None:
    a1 = Name("john", "SMITH")

    print(a1.fname)
    print(a1.lname)
    print(a1.full_name)
    print(a1.initials)


if __name__ == "__main__":
    main()
