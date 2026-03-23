class Player:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(
        self,
    ) -> str:
        return f"{self.name} is age {self.age}"

    def get_height(
        self,
    ) -> str:
        return f"{self.name} is {self.height} cm"

    def get_weight(
        self,
    ) -> str:
        return f"{self.name} is {self.weight} kg"


def main() -> None:
    p1: Player = Player("David Jones", 25, 175, 75)

    print(p1.get_age())
    print(p1.get_height())
    print(p1.get_weight())


if __name__ == "__main__":
    main()
