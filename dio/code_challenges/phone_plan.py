class PhonePlan:
    def __init__(self, plan_name: str, balance: float) -> None:
        self.plan_name = plan_name
        self.balance = balance


class PhoneUser:
    def __init__(self, name: str, plan: PhonePlan):
        self.name = name
        self.plan = plan

    def balance(self) -> tuple[float, str]:
        if self.plan.balance < 10:
            return (
                self.plan.balance,
                """
                Seu saldo está baixo. Recarregue e use os serviços do seu plano.
                """.strip(),
            )
        if self.plan.balance >= 10 and self.plan.balance < 50:
            return (
                self.plan.balance,
                """
                Seu saldo está razoável. Aproveite o uso moderado do seu plano.
                """.strip(),
            )
        if self.plan.balance >= 50:
            return (
                self.plan.balance,
                """
                Parabéns! Continue aproveitando seu plano sem preocupações.
                """.strip(),
            )


def main() -> None:
    user_name = input()
    plan_name = input()
    balance = float(input())
    user_plan = PhonePlan(plan_name, balance)
    user = PhoneUser(user_name, user_plan)
    _, msg = user.balance()
    print(msg)


if __name__ == "__main__":
    main()
