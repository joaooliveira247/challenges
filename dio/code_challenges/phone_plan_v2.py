class Plan:
    def __init__(self, balance: float) -> None:
        self.balance = balance


class UserPhone:
    def __init__(self, name: str, phone_num: str, plan: Plan) -> None:
        self.name = name
        self.phone_num = phone_num
        self.plan = plan


class UserPrepaid(UserPhone):
    TAX: float = 0.10

    def __init__(self, name: str, phone_num: str, balance: float) -> None:
        super().__init__(name, phone_num, Plan(balance))

    def _deduce(self, value: float) -> float:
        self.plan.balance -= value
        return self.plan.balance

    def call(self, dest: str, time: int) -> str:
        coast = float(self.TAX * time)
        if coast > self.plan.balance:
            return "Saldo insuficiente para fazer a chamada."
        return "Chamada para {} realizada com sucesso. Saldo: ${:.2f}".format(
            dest, self._deduce(float(self.TAX * time))
        )


def main() -> None:
    name = input()
    user_num = input()
    balance = float(input())

    user_prepaid = UserPrepaid(name, user_num, balance)
    dest = input()
    time = int(input())

    print(user_prepaid.call(dest, time))


if __name__ == "__main__":
    main()
