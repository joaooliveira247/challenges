from collections import Counter


def produto_mais_vendido(produtos: list[str]) -> str:
    contagem = Counter(produtos)
    max_produto: tuple[str, int] = contagem.most_common(1)

    return max_produto[0][0].title()


def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:

    produtos = [x.strip().lower() for x in entrada.split(",") if x]

    return produtos


def main() -> None:
    produtos = obter_entrada_produtos()
    print(produto_mais_vendido(produtos))


if __name__ == "__main__":
    main()
