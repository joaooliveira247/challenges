def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:

    total_vendas: int = sum(vendas)
    media_vendas: int = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"


def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas: list[int] = [int(x) for x in entrada.split(",") if x]

    return vendas


def main() -> None:
    vendas = obter_entrada_vendas()
    print(analise_vendas(vendas))


if __name__ == "__main__":
    main()
