def main() -> None:
    MENU: str = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
    saldo: int = 0
    limite: int = 500
    saques: int = 3
    extrado: str = ""

    while True:
        option: str = input(MENU)
        match option:
            case "d":
                value: int = float(input("Digite o valor\n"))
                if value < 0:
                    print("Valor invalido")
                    continue
                saldo += value
                extrado += "Deposito: {:.2f}\n".format(value)
            case "s":
                value: int = float(input("Digite o valor\n"))
                if value < 0:
                    print("Valor invalido")
                    continue
                if value > limite:
                    print("Limite excedido")
                    continue
                if saques < 0:
                    print("Número de saques excedido")
                    continue
                if saldo < value:
                    print("Saldo invalido para operação")
                    continue
                saldo += value
                saques -= 1
                extrado += "Saque: {:.2f}\n".format(value)
            case "e":
                print(extrado)
            case "q":
                break
            case _:
                print("Opção invalida")


if __name__ == "__main__":
    main()
