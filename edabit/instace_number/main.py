class User:
    user_count: int = 0

    def __new__(cls, *args, **kwargs):
        cls.user_count += 1
        instance = super().__new__(cls)
        return instance

    def __init__(self, username: str) -> None:
        self.username = username


def main() -> None:
    u1 = User("johnsmith10")
    print(User.user_count)

    u2 = User("marysue1989")
    print(User.user_count)

    u3 = User("milan_rodrick")
    print(User.user_count)

    print(u1.username, u2.username, u3.username)


if __name__ == "__main__":
    main()
