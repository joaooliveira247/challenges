def main() -> None:
    itens: list[str] = []
    for _ in range(3):
        user_input: str = input()
        itens.append(user_input)
    print("Lista de Equipamentos:")
    for item in itens:
        print(f"- {item}")


if __name__ == "__main__":
    main()
