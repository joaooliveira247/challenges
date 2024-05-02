class UsuarioTelefone:
    def __init__(self, name: str, phone_number: str, plan: str) -> None:
        self.name = name
        self.phone_number = phone_number
        self.plan = plan

    def __str__(self) -> str:
        return f"Usuário {self.name} criado com sucesso."
    
def main() -> None:
    name = input()
    num = input()
    plan = input()
    user = UsuarioTelefone(name, num, plan)
    print(user)


if __name__ == "__main__":
    main()
