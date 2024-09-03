def extrair_anos(datas: str) -> str:
    lista_datas = datas.split(", ")

    years: list[str] = [date.split("-")[0] for date in lista_datas]

    return ", ".join(years)


def main() -> None:
    entrada = input()

    saida = extrair_anos(entrada)

    print(saida)


if __name__ == "__main__":
    main()
