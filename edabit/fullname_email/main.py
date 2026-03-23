class Employee:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self) -> str:
        return f"{self.first_name}.{self.last_name}@company.com"


def main() -> None:
    emp_1 = Employee("John", "Smith")
    emp_2 = Employee("Mary", "Sue")
    emp_3 = Employee("Antony", "Walker")

    print(emp_1.fullname)
    print(emp_2.email)
    print(emp_3.first_name)


if __name__ == "__main__":
    main()
